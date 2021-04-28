import requests
import json

# post_code_req = requests.get("https://api.postcodes.io/postcodes/DY54HU")

# print(post_code_req)
# Prints off request 200 which means there was a correct response
# print(post_code_req.status_code)
# prints the same as previously

# print(post_code_req.headers)
# Returns header information in the form of a dictionary

# print(post_code_req.content)
# Prints off the actual information around the postcode

# print(type(post_code_req.content))
# class 'bytes'

# print(post_code_req.json())
# prints content in dictionary format


json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
# dumps serialises the object into a string
headers = {"content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)

print(post_multi_req.status_code)
# 200 which again means that its working and responding correctly
print(post_multi_req.json())
# Prints off a list of dictionaries. Each dictionary represents each postcode


