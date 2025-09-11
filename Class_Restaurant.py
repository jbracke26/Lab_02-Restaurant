import json
#this is the main class for the restraunt object
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
        from utils import filepath
        menu = json.loads("C:\Users\ebele\GitRep\my_work\Lab_02-Restaurant\menu.json")
        print(menu)
        classadd = input("What is an item you want to add? Input id # for the category: ")
        menu.get(classadd)
        menuitemaddid = int(input("Enter the ID number (should be greater than the current highest ID number)"))
        menuitemaddname = input("Enter the name of the item: ")
        menuitemaddprice = input("Enter a price for the item")
        menu.append({menuitemaddid,menuitemaddname,menuitemaddprice})
        json.dumps(menu)
        
    

    
    