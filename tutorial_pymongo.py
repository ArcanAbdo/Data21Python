import pymongo
from pprint import pprint
import math


# client = pymongo.MongoClient()
# # print(client)
# db = client['starwars']


# luke = db.characters.find({name: "Luke Skywalker"})
# luke = db.characters.find({"name": "Luke Skywalker"})
# print(luke)
# pprint(type(luke))
# pprint(type(luke))
# print(luke, sort_dicts=False)

# print(luke)
# # cursor objects are iterable
# for char in luke:
#     print(char["name"])

# blue = db.characters.find({"eye_color": "blue"})
# for char in blue:
#     print(blue["name"])


# droids = db.characters.find({"species.name": "Droid"})
#
# for char in droids:
#     print(char["name"])

# darth_vader = db.characters.find({"name": "Darth Vader"})
# for char in darth_vader:
#     print(char["height"])
#     print(char["name"])
# # or
# print(db.characters.find_one({"name": "Darth Vader"}, {"name": 1, "height": 1, "_id": 0}))

# yellow_eyes = db.characters.find({"eye_color": "yellow"}, {"name": 1, "_id": 0})
# for char in yellow_eyes:
#     print(char)

# male_characters = db.characters.find({
#     "gender": "male"},
#     {"name": 1, "_id": 0}
# ).limit(3)
# # .limit(3) returns first three values. Could also use [0:3]
# for char in male_characters:
#     print(char)

# human_alderaan = db.characters.find(
#     {"species.name": "Human", "homeworld.name": "Alderaan"},
#     {"name": 1, "_id": 0}
# )
# for char in human_alderaan:
#     print(char)

# avg_height_fe = db.chardemo.aggregate([
#     {"$match": {"gender": "female", "height": {"$ne": float("nan")}}},
#     {"$group": {"_id": "$gender", "avg_height": {"$avg": "$height"}}}
# ])
# print(avg_height_fe.next())

# max_height = db.chardemo.aggregate([
#     {"$group": {
#         "_id": None, "max_height": {"$max": "$height"}
#     }}
# ]).next()["max_height"]
# # print(max_height)
#
# for tallest in db.chardemo.find({"height": max_height}):
#     print(tallest['name'])
