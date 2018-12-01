#!/usr/bin/env python2.7
from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify, flash, make_response
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database_setup import Base, Category, ToolItem, User
from flask import session as login_session
import random
import string
import requests
import httplib2
import json
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError


app = Flask(__name__)
app.secret_key = 'super secret key'

# referecing client secret file to client_ID
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

# identify the working DB and create a session to it
engine = create_engine(
    'sqlite:///catalogtool.db',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(
        random.choice(
            string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# create gconnect method to login using google account.
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorizationcode.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = (
        'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
        % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px; border-radius:150px;'
    output += '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# User Helper Functions
def createUser(login_session):
    session = DBSession()
    newUser = User(
        name=login_session['username'], email=login_session['email'],
        picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    session.close()
    return user.id


def getUserInfo(user_id):
    session = DBSession()
    user = session.query(User).filter_by(id=user_id).one()
    session.close()
    return user


def getUserID(email):
    session = DBSession()
    try:
        user = session.query(User).filter_by(email=email).one()
        session.close()
        return user.id
    except:
        session.close()
        return None


def checklogin():
    if 'username' in login_session:
        return True
    else:
        return False


# create disconnect method from google account
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' \
        % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        print 'Successfully disconnected.'
        result = redirect('/Categories')
        flash("You are now logged out.")
        return result
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# Show all categories and last added items
@app.route('/')
@app.route('/Categories')
def showCategories():
    session = DBSession()
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(ToolItem).order_by(desc(ToolItem.id)).limit(10)
    if 'username' not in login_session:
        result = render_template(
            'main_public.html', categories=categories, items=items)
    else:
        result = render_template(
            'main.html', categories=categories, items=items)
    session.close()
    return result


# Show a specific category Items
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/tool/')
def showTool(category_id):
    session = DBSession()
    categories = session.query(Category).order_by(asc(Category.name))
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(ToolItem).filter_by(category_id=category_id).all()
    count = len(items)
    if 'username' not in login_session:
        result = render_template(
            'tool_public.html',
            categories=categories,
            items=items,
            category=category,
            count=count)
    else:
        result = render_template(
            'tool.html',
            categories=categories,
            items=items,
            category=category,
            count=count)
    session.close()
    return result


# Show description of specific Items
@app.route('/category/<int:category_id>/tool/<int:item_id>')
def ShowDesc(category_id, item_id):
    session = DBSession()
    categories = session.query(Category).order_by(asc(Category.name))
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(ToolItem).filter_by(id=item_id).all()
    if 'username' not in login_session:
        result = render_template(
            'ItemDesc_public.html',
            categories=categories,
            item=item,
            category=category)
    else:
        result = render_template(
            'ItemDesc.html',
            categories=categories,
            item=item,
            category=category)
    session.close()
    return result


# add new item to catalogtool
@app.route('/category/newItem', methods=['GET', 'POST'])
def newToolItem():
    session = DBSession()
    if checklogin() is False:
        return redirect('/login')
    if request.method == 'POST':
        print login_session['email']
        print getUserID(login_session['email'])
        newItem = ToolItem(
            name=request.form['name'],
            description=request.form['description'],
            category_id=request.form['category_id'],
            user_id=getUserID(login_session['email']))
        session.add(newItem)
        session.commit()
        print ('New Menu %s Item Successfully Created' % (newItem.name))
        print newItem.user_id
        result = redirect(
            url_for(
                'ShowDesc',
                category_id=newItem.category_id,
                item_id=newItem.id))
        session.close()
        return result
    else:
        categories = session.query(Category).order_by(asc(Category.name))
        result = render_template('newToolitem.html', categories=categories)
        session.close()
        return result


# Edit specific item data
@app.route(
    '/category/<int:category_id>/tool/<int:item_id>/edit',
    methods=['GET', 'POST'])
def editToolItem(category_id, item_id):
    session = DBSession()
    if checklogin() is False:
        return redirect('/login')
    editItem = session.query(ToolItem).filter_by(id=item_id).one()
    print editItem.user_id
    print getUserID(login_session['email'])
    if editItem.user_id != getUserID(login_session['email']):
        return "<script>function myFunction()"\
            "{alert('You are not authorized to edit this Item. "\
            "Please create your own Items in order to edit.');}"\
            "</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editItem.name = request.form['name']
        if request.form['description']:
            editItem.description = request.form['description']
        if request.form['category_id']:
            editItem.category_id = request.form['category_id']
        session.add(editItem)
        session.commit()
        print ('Item %s had been updated' % (editItem.name))
        result = redirect(
            url_for(
                'ShowDesc',
                category_id=editItem.category_id,
                item_id=item_id))
        session.close()
        return result
    else:
        categories = session.query(Category).order_by(asc(Category.name))
        item = session.query(ToolItem).filter_by(id=item_id).one()
        result = render_template(
            'EditToolItem.html', item=item, categories=categories)
        session.close()
        return result


# Delete specific item data
@app.route(
    '/category/<int:category_id>/tool/<int:item_id>/delete',
    methods=['GET', 'POST'])
def deleteToolItem(category_id, item_id):
    session = DBSession()
    if checklogin() is False:
        return redirect('/login')
    deletedItem = session.query(ToolItem).filter_by(id=item_id).one()
    if deletedItem.user_id != getUserID(login_session['email']):
        return "<script>function myFunction() "\
            "{alert('You are not authorized to delete this Item. "\
            "Please create your own Items in order to delete.');}"\
            "</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        print ('Item %s had been deleted' % (deletedItem.name))
        result = redirect(url_for('showCategories'))
        session.close()
        return result
    else:
        item = session.query(ToolItem).filter_by(id=item_id).one()
        result = render_template('DeleteToolItem.html', item=item)
        session.close()
        return result


# JSON APIs to view catalog Information
@app.route('/category.json')
def showCategoriesJSON():
    session = DBSession()
    if 'username' not in login_session:
        return redirect('/login')
    categories = session.query(Category).order_by(asc(Category.name)).all()
    category_dict = [c.serialize for c in categories]
    for c in range(len(category_dict)):
        items = [i.serialize for i in session.query(ToolItem).filter_by(
            category_id=category_dict[c]["id"]).all()]
        if items:
            category_dict[c]["Item"] = items
    session.close()
    return jsonify(Category=category_dict)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
