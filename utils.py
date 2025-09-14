import json
from pathlib import Path
# Function to load the menu.json file in an editable format
def loadjson(): 
    with open("menu.json", "r") as file:
        global menu
        menu = json.load(file)
        return menu

#Function to save the changes to the menu.json file
def savejson():
    global menu
    with open("menu.json", "w") as file:
        json.dump(menu, file, indent=1)
    print("Saved to JSON")
