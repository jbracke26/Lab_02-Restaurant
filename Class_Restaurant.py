import json
from pathlib import Path
from utils import loadjson, savejson
#this is the main clthisass for the restaurant object
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
        global menu
        menu = loadjson()

    #takes user input and adds it to a directory
        menuitemaddid = len(menu) + 1
        menuitemaddname = input("Enter the name of the item: ")
        menuitemaddprice = input("Enter a price for the item: ")
        menuitemaddcategory = input("Enter a category for the item: ")
        newitemdict = {
            "id" : menuitemaddid,
            "Name" : menuitemaddname,
            "Price" : menuitemaddprice,
            "Category" : menuitemaddcategory
        }
    
    #updates the menu[] list with the new data and writes to json
        menu.append(newitemdict)
        savejson()

# This is a function to change an item on the menu
    def menuchange(self):
        global menu
        menu = loadjson()
    # takes an id input and finds the correlating value in the list
        menuchangeid = int(input("What is the ID Number of the item you want to change? "))
        index = next((i for i, item in enumerate(menu) if item["id"] == menuchangeid), None)
        if index is None:
            print("Item ID not found.")
            return
    #recieving the user input
        newitemdict = {
            "id" : menuchangeid,
            "Name": input("Enter the name of the item: "),
            "Price" : input("Enter a price for the item: "),
            "Category" : input("Enter a category for the item: ")
        }
    #adds to the list and saves it to json
        menu[index] = (newitemdict)
        savejson()
# This is a function to remove an item
    def menuremove(self):
        global menu
        menu = loadjson()
        menuremoveitemid = int(input("What is the ID Number of the item you want to remove? "))
    # takes an id input and finds the correlating value in the list
        index = next((i for i, item in enumerate(menu) if item["id"] == menuremoveitemid), None)
        if index is None:
            print("Item ID not found.")
            return
        removed_item = menu.pop(index)
        print(f"Removed item {removed_item}")
        savejson()  