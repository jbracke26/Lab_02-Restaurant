import json
from pathlib import Path
from utils import loadjson, savejson
#this is the main class for the restaurant object
class restaurant: 
    def __init__(self):
        pass
    def data(self):
        globaldata = {
            "Location":"1 Lamplighter Way, Gill, MA 01354",
            "Cuisine" : "American BBQ",
            "Name" : "HBQ"
        }
        print(globaldata)
 # This is a function to add a new menu item and save it to the json file
    def menuadd(self):
        menu = loadjson
        menuitemaddid = menu.len + 1
        menuitemaddname = input("Enter the name of the item: ")
        menuitemaddprice = input("Enter a price for the item")
        menuitemaddcategory = input("Enter a category for the item")
        menu.append({menuitemaddid,menuitemaddname,menuitemaddprice,menuitemaddcategory})
        savejson(menu)
# This is a function to change an item on the menu
    def menuchange(self):
        menu = loadjson
        menuchangeid = input("What is the ID Number of the item you want to change?")
        menu.get(menuchangeid)
        menuitemchangename = input("Enter the name of the item: ")
        menuitemchangeprice = input("Enter a price for the item: ")
        menuitemchangecategory = input("Enter a category for the item: ")
        menu.append({menuchangeid,menuitemchangename,menuitemchangeprice,menuitemchangecategory})
        savejson(menu)
# This is a function to remove an item
    def menuremove(self):
        menu = loadjson
        menuremoveitemid = input("What is the ID Number of the item you want to remove?")
        menu.remove(menuremoveitemid)
        savejson(menu)




    
    