import json
from pathlib import Path
eben-working
# Function to load the menu.json file in an editable format
def loadjson(): 
    with open("menu.json", "r") as file:
        menu = json.loads(file)
        return menu

#Function to save the changes to the menu.json file
def savejson():
    with open("menu.json", "w") as file:
        json.dumps(file, indent = 4)
    print("Saved to JSON")    


