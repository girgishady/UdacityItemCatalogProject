from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, ToolItem, User

engine = create_engine('sqlite:///catalogtool.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session wont be persisted into the database until you call
# session.commit(). If youre not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(
    id=1,
    name="Robo Barista",
    email="tinnyTim@udacity.com",
    picture="https://pbs.twimg.com/profile_images/"
    "2671170543/18debd694829ed78203a5a36dd364160_400x400.png")
session.add(User1)
session.commit()


# Items for Soccer
category1 = Category(name="Soccer")

session.add(category1)
session.commit()


toolItem1 = ToolItem(
    user_id=1,
    name="Shoes",
    description="Footballers wear lightweight, comfortable and durable shoes"
    "that are usually studded to provide good grip on muddy or"
    "slippery surfaces.",
    category=category1)

session.add(toolItem1)
session.commit()

toolItem2 = ToolItem(
    user_id=1,
    name="Football",
    description="Balls are made from synthetic material that has a "
    "circumference of 68 to 70 cm, weighs around 410 to 450 grams and has "
    "inflation pressure between 600 to 1100 g/sq. cm. at sea level. These"
    "balls have a covering of synthetic leather panels stitched together and"
    "have latex or butyl air bladder inside.",
    category=category1)

session.add(toolItem2)
session.commit()

toolItem3 = ToolItem(
    user_id=1,
    name="Goal Post",
    description="A goal post is a frame which should not be more than 24"
    "feet in width and 8 feet in length with a net attached to it. The ball"
    "must completely pass the post in order to score a goal by the "
    "opponent team.",
    category=category1)

session.add(toolItem3)
session.commit()

toolItem4 = ToolItem(
    user_id=1,
    name="Shin Guard",
    description="This protective equipment is worn by players and the"
    "goalie to protect their shin bone from any injury.",
    category=category1)

session.add(toolItem4)
session.commit()

toolItem5 = ToolItem(
    user_id=1,
    name="Mouth Guard",
    description="Mouth guard covers teeth and gums and is used by players"
    "to protect their teeth, arches, lips and gums from injuries.",
    category=category1)

session.add(toolItem5)
session.commit()

toolItem6 = ToolItem(
    user_id=1,
    name="Goalie Head Gear",
    description="Goalies are allowed to wear headgears during the play"
    "though it is not mandatory, but many of them opt for it as it protects"
    "them against any head injury.",
    category=category1)

session.add(toolItem6)
session.commit()

toolItem7 = ToolItem(
    user_id=1,
    name="Goalie Gloves",
    description="The goalkeepers wear gloves to protect their hands and"
    "to get a good grip on the ball.",
    category=category1)

session.add(toolItem7)
session.commit()

toolItem8 = ToolItem(
    user_id=1,
    name="Clothing",
    description="Players wear light and breathable polyester T-shirt and"
    "shorts. Each player of the team wears same color shirts "
    "except the goalkeeper.",
    category=category1)

session.add(toolItem8)
session.commit()


# Items for Ski Jumping
category2 = Category(name="Ski Jumping")

session.add(category2)
session.commit()


toolItem1 = ToolItem(
    user_id=1,
    name="Gloves",
    description="Some skiers wear gloves to keep hands warm while skiing.",
    category=category2)

session.add(toolItem1)
session.commit()

toolItem2 = ToolItem(
    user_id=1,
    name="Goggles",
    description=" Well fitting ski goggles are used that help protect the"
    "skiers eyes from the sun as well as keeps the snow out of the eyes. The "
    "eye gear must allow the skier a clear vision so that he can place his "
    "landing accurately. ",
    category=category2)

session.add(toolItem2)
session.commit()

toolItem3 = ToolItem(
    user_id=1,
    name="Helmet",
    description="Skiers wear a helmet with padded chin-strap that covers"
    "the head and ears and consist of a hard plastic or resin shell with inner"
    "padding to withstand several impacts and gives warmth and extra "
    "protection for the head.",
    category=category2)

session.add(toolItem3)
session.commit()

toolItem4 = ToolItem(
    user_id=1,
    name="Ski Boots ",
    description="Flexible boots are used during ski jumping that allows"
    "movement at the ankles and enables a jumper to lean as far forward "
    "as possible during flights.",
    category=category2)

session.add(toolItem4)
session.commit()

toolItem5 = ToolItem(
    user_id=1,
    name="Ski",
    description="Skis made of wood and fiberglass is used in ski jumping "
    "that can be 240-270 cm long and 9-10 cm wide. Bindings are used to secure"
    "the skis with the boots. Skis have five to six grooves on the bottom to"
    "keep the skier straight on the inrun.",
    category=category2)

session.add(toolItem5)
session.commit()

toolItem6 = ToolItem(
    user_id=1,
    name="Bindings",
    description="The device that connects binds a ski boot to the ski is"
    "known as a binding. In ski jumping the skiers heel is not attached and "
    "can move up and down during flights.",
    category=category2)

session.add(toolItem6)
session.commit()


# Items for Road Racing
category3 = Category(name="Road Racing")

session.add(category3)
session.commit()


toolItem1 = ToolItem(
    user_id=1,
    name="Road-Racing Bicycle",
    description="Specially designed bicycles are used in road bicycle racing"
    "that takes place on paved roads. These cycles are built to be light,"
    "strong and comfortable enough to be ridden for hours. ",
    category=category3)

session.add(toolItem1)
session.commit()

toolItem2 = ToolItem(
    user_id=1,
    name="Time-Trial Bicycle",
    description="Time-trial bicycles are designed to move faster than road"
    "racing bicycles, it uses triathlon handlebars or aerobars that provide"
    "a low tucked position to reduce drag and have a disc wheel that offers"
    "aerodynamic advantage over the other forms.",
    category=category3)

session.add(toolItem2)
session.commit()

toolItem3 = ToolItem(
    user_id=1,
    name="Helmet",
    description="Lightweight helmets are worn by riders that offer a minimum"
    "wind resistance and are narrower from the back for optimal aerodynamics.",
    category=category3)

session.add(toolItem3)
session.commit()

toolItem4 = ToolItem(
    user_id=1,
    name="Shoes",
    description="Cyclists wear shoes with smooth, rigid and inflexible "
    "cleated soles that are bent slightly at the ball of the foot that keeps "
    "the foot on the pedal.",
    category=category3)

session.add(toolItem4)
session.commit()


# Items for Golf
category4 = Category(name="Golf ")

session.add(category4)
session.commit()


toolItem1 = ToolItem(
    user_id=1,
    name="Golf Bag",
    description="Golf bags has several pockets that are used to carry golf"
    "clubs and various equipment required during matches.",
    category=category4)

session.add(toolItem1)
session.commit()

toolItem2 = ToolItem(
    user_id=1,
    name="Golf Ball",
    description="A golf ball weighs around 1.62 ounces and has a diameter"
    "of not less than 1.680 inches. The ball has a symmetrical arrangement of"
    "dimples on its surface to make it aerodynamic. ",
    category=category4)

session.add(toolItem2)
session.commit()

toolItem3 = ToolItem(
    user_id=1,
    name="Golf Club",
    description="A golfer can use up to 14 clubs during the game. Mainly"
    "four types of clubs are used- driver, iron, wedge and putter.",
    category=category4)

session.add(toolItem3)
session.commit()

toolItem4 = ToolItem(
    user_id=1,
    name="Tee",
    description="Usually wooden or plastic tees are used by golfers to place"
    "the ball on it for the first stroke at each hole to make the shot easier",
    category=category4)

session.add(toolItem4)
session.commit()

toolItem5 = ToolItem(
    user_id=1,
    name="Gloves",
    description="They are optional but usually worn by golfers to ensure"
    "better grip on the club.",
    category=category4)

session.add(toolItem5)
session.commit()


# Items for skydiving
category5 = Category(name="skydiving ")

session.add(category5)
session.commit()


toolItem1 = ToolItem(
    user_id=1,
    name="Parachutes",
    description="The parachutes have steering lines and toggles which are"
    "used by skydivers to control their flight and have an aerodynamic canopy"
    "like an airplanes wing.",
    category=category5)

session.add(toolItem1)
session.commit()

toolItem2 = ToolItem(
    user_id=1,
    name="Harness System",
    description="A harness system is strapped to the body of the sky divers"
    "which contains the pack with parachutes.",
    category=category5)

session.add(toolItem2)
session.commit()

toolItem3 = ToolItem(
    user_id=1,
    name="Altimeter",
    description="An altimeter is attached with the sky-divers chest strap,"
    "wrist or beside the ear which gives audible signals and shows the height"
    "above the ground.",
    category=category5)

session.add(toolItem3)
session.commit()

toolItem4 = ToolItem(
    user_id=1,
    name="AAD",
    description="AAD (Automatic Activation Device) is the most essential"
    "equipment of parachuting. It releases the parachute when it cant be"
    "done manually.",
    category=category5)

session.add(toolItem4)
session.commit()

toolItem5 = ToolItem(
    user_id=1,
    name="Helmet",
    description="Protective helmets are worn by sky-divers for protection"
    "against head injuries.",
    category=category5)

session.add(toolItem5)
session.commit()


# Items for Shooting
category6 = Category(name="Shooting")

session.add(category6)
session.commit()


toolItem1 = ToolItem(
    user_id=1,
    name="Rifle",
    description="A rifle is a long weapon, commonly a firearm or airgun with"
    "a rifled barrel that has a longer range and much greater accuracy than"
    "pistols. During international competitions, a rifle is required to have "
    "the ammunition of 5.6-8mm caliber and must not exceed the weight of 8kg "
    "for men and 6.5kg for women. The main types of rifle used are .22 calibre"
    "rifle and .177 air rifle.",
    category=category6)

session.add(toolItem1)
session.commit()

toolItem2 = ToolItem(
    user_id=1,
    name="Goggles",
    description="Protective eyewear made from shatter-resistant plastic"
    "lenses is worn by shooters to guard their eyes during the event.",
    category=category6)

session.add(toolItem2)
session.commit()

toolItem3 = ToolItem(
    user_id=1,
    name="Ear Protection",
    description="Shooters wear ear muffs or another form of protective gear"
    "to protect their hearing while in the vicinity of the firing line.",
    category=category6)

session.add(toolItem3)
session.commit()

toolItem4 = ToolItem(
    user_id=1,
    name="Cap",
    description="Sun visors or other devices are sometimes used during"
    "shooting events that keep the wind and sunlight out of shooters eyes.",
    category=category6)

session.add(toolItem4)
session.commit()


# Items for Squash
category7 = Category(name="Squash ")

session.add(category7)
session.commit()

menuItem9 = ToolItem(
    user_id=1,
    name="Ball",
    description="Squash balls are hollow rubber balls having a diameter "
    "between 39.5 mm to 40.5 mm & weigh between 23 to 25 grams. These are"
    "available in a variety of speeds, indicated by a small colored dot.",
    category=category7)

session.add(menuItem9)
session.commit()

toolItem1 = ToolItem(
    user_id=1,
    name="Racquet",
    description="Squash racquets are made from lightweight materials like"
    "graphite, titanium or Kevlar with synthetic strings. The racquets should"
    "not weigh more than 255 gm. and are normally 27 inches long & 8.5 inches "
    "wide with a maximum strung area of 77.5 sq inches.",
    category=category7)

session.add(toolItem1)
session.commit()

toolItem2 = ToolItem(
    user_id=1,
    name="Wristband",
    description="Wristband or Sweatband is used to prevent sweat from"
    "dripping down on to the racquet handle.",
    category=category7)

session.add(toolItem2)
session.commit()

toolItem3 = ToolItem(
    user_id=1,
    name="Shoes",
    description="Non-marking shoes with white or clear soles are used with"
    "a pair of well-fitting socks to prevent rubbing & blisters.",
    category=category7)

session.add(toolItem3)
session.commit()


# Items for Beach Volleyball
category8 = Category(name="Beach Volleyball ")

session.add(category8)
session.commit()


toolItem1 = ToolItem(
    user_id=1,
    name="Net And Poles",
    description="A beach volleyball net is affixed on two upright poles that"
    "are situated opposite each other at a certain distance. The measurements"
    "of the net vary according to mens, womens and junior games respectively.",
    category=category8)

session.add(toolItem1)
session.commit()

toolItem2 = ToolItem(
    user_id=1,
    name="Volleyball",
    description="Beach volleyballs are usually larger than standard"
    "volleyballs and have lower internal pressure. These usually have a "
    "circumference of about 26-27 inches and weigh around 260-280 grams.",
    category=category8)

session.add(toolItem2)
session.commit()

print "added menu items!"
