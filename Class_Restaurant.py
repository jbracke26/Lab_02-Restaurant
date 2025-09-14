import json
from pathlib import Path
from utils import loadjson, savejson


#this is the main class for the restaurant object
class restaurant:
    def __init__(self):
        pass

    def data(self):
        globaldata = {
            "Location": "1 Lamplighter Way, Gill, MA 01354",
            "Cuisine": "American BBQ",
            "Name": "HBQ",
        }
        print(globaldata)

 # This is a function to add a new menu item and save it to the json file
    def menuadd(self, item_data):
        menu = loadjson()
        # menuitemaddid = menu.len + 1
        # menuitemaddname = input("Enter the name of the item: ")
        # menuitemaddprice = input("Enter a price for the item")
        # menuitemaddcategory = input("Enter a category for the item")

        # get next id number
        existing_ids = []
        for item in menu["menu"][0]["items"]:
            existing_ids.append(item["id"])
        new_id = max(existing_ids) + 1

        # create new item
        new_item = {
            "id": new_id,
            "name": item_data["name"],
            "price": float(item_data["price"]),
            "category": item_data["category"],
        }

        menu["menu"][0]["items"].append(new_item)
        savejson(menu)

# This is a function to change an item on the menu
    def menuchange(self, item_id, item_data):
        menu = loadjson()
        # menuchangeid = input("What is the ID Number of the item you want to change?")
        # menu.get(menuchangeid)
        # menuitemchangename = input("Enter the name of the item: ")
        # menuitemchangeprice = input("Enter a price for the item: ")
        # menuitemchangecategory = input("Enter a category for the item: ")

        for item in menu["menu"][0]["items"]:
            if item["id"] == item_id:
                item["name"] = item_data["name"]
                item["price"] = float(item_data["price"])
                item["category"] = item_data["category"]
                break

        savejson(menu)

# This is a function to remove an item
    def menuremove(self, item_id):
        menu = loadjson()
        # menuremoveitemid = input("What is the ID Number of the item you want to remove?")

        items = menu["menu"][0]["items"]
        updated_items = []

        # keep everything except the item to remove
        for item in items:
            if item["id"] != item_id:
                updated_items.append(item)

        menu["menu"][0]["items"] = updated_items

        savejson(menu)
