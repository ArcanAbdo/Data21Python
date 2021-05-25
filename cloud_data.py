import pymongo

# connecting to the aws server through mongodb compass
client = pymongo.MongoClient('mongodb://18.193.109.61:27017/demo')
db = client['demo']

a = db.hello.find()
print(a)
for b in a:
    print(b)
