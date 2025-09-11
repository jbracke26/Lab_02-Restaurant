import json
from pathlib import Path
from utils import load_menu
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
    #This is a function to add a new menu item and save it to the json file
    def menuadd(self):
        menu = json.loads("menu.json")
        classadd = input("What is an item you want to add? Input id # for the category: ")
        menu.get(classadd)
        menuitemaddid = menu.len + 1
        menuitemaddname = input("Enter the name of the item: ")
        menuitemaddprice = input("Enter a price for the item")
        menu.append({menuitemaddid,menuitemaddname,menuitemaddprice})
        json.dumps(menu)
    def menuchange(self):
        menu = json.loads("menu.json")
        menuchangeid = input("What is the ID Number of the item you want to change?")
        menu.get(menuchangeid)
        menuitemaddname = input("Enter the name of the item: ")
        menuitemaddprice = input("Enter a price for the item")
        menu.append({menuchangeid,menuitemaddname,menuitemaddprice})
        json.dumps(menu)
    def menuremove(self):
        menu = json.loads("menu.json")
        menuremoveitemid = input("What is the ID Number of the item you want to remove?")
        menu.remove(menuremoveitemid)
        json.dumps(menu)




    
    