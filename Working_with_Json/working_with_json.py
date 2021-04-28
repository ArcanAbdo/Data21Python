# A json file looks like a python dictionary with
# key value pairs and curly brackets

import json

# pet_data = {"name": "Bob", "food": "carrots"}
# print(pet_data)
# print(type(pet_data))

# pet_data_json_str = json.dumps(pet_data)
# print(pet_data_json_str)
# print(type(pet_data_json_str))

# with open("new_json_file.json", "w") as jsonfile:
    # Dumps makes it into a string series
    # Dump creates the file.
    # json.dump(pet_data, jsonfile)

# with open("new_json_file.json") as jsonfile:
    # load will take in a json file and open it in a dictionary form
    # pet = json.load(jsonfile)
    # print(type(pet))
    # print(pet["name"])


class RatesParser:

    def __init__(self, rates_file):
        rates_info = self._open_json_file(rates_file)
        self.base = rates_info["base"]
        self.rates = rates_info["rates"]
        # self.rates can then be used to make self.gbp simpler
        self.gbp = self.rates["GBP"]

    def _open_json_file(self, file_name):
        with open(file_name) as rates:
            return json.load(rates)


rates_reader = RatesParser("exchange_rates.json")
# print(rates_reader.gbp)
