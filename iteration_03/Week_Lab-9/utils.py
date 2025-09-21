import json
import random
def loadjson(): 
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "userdata.json")
    with open(file_path, "r") as file:
        return json.load(file)
    
def savejson(file, data):
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "userdata.json")
    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)
    print("Saved to JSON")    
def randomname():
    randomint = random.randint(0,77)
    names = [
    "Adley May",
    "Finley Zamora",
    "Sierra Alfaro",
    "Xzavier Smith",
    "Olivia Hall",
    "Thomas Travis",
    "Mazikee Sparks",
    "Drake Harrell",
    "Kara Robbins",
    "Finnegan Guerrero",
    "Margot Webster",
    "Shawn McLaughlin",
    "Stephanie Wyatt",
    "Sam Hopkins",
    "Gabriela Le",
    "Damien Coffey",
    "Paola Poole",
    "Quincy Tanner",
    "Harmoni Mullen",
    "Shepard Duncan",
    "Elise Arias",
    "Alec Brady",
    "Ryan Guerra",
    "Leland Foster",
    "Brielle Brandt",
    "Damir Reed",
    "Valentina Villanueva",
    "Huxley Greene",
    "Selena Bernal",
    "Eithan Morton",
    "Mallory Dean",
    "Ronan Estes",
    "Brittany Preston",
    "Vincenzo Weaver",
    "Teagan Hancock",
    "Rex Carr",
    "Rowan McGuire",
    "Casey Pearson",
    "Kiara Wallace",
    "Chase Thornton",
    "Haisley Rollins",
    "Wes Holmes",
    "Bailey Marquez",
    "Malakai Riley",
    "Kayla Spears",
    "Ameer Chapman",
    "Zuri Huang",
    "Ayaan Huang",
    "Francesca Hodge",
    "Reign Nichols",
    "Aliyah Blevins",
    "Avi Whitehead",
    "Sylvie Herring",
    "Henrik Gordon",
    "Taylor Zavala",
    "Dillon Koch",
    "Milana Kane",
    "Brock Young",
    "Zoey Orozco",
    "Keanu Mitchell",
    "Willow Schultz",
    "Cody McLean",
    "Sky Austin",
    "Omar Palmer",
    "Juniper Saunders",
    "Kasen Horne",
    "Marlowe Pennington",
    "Bobby Barrera",
    "Beatrice Stephens",
    "Messiah Miles",
    "Alessandra Murray",
    "Ashton Fernandez",
    "Amara Parra",
    "Davion Duran",
    "Willa Moody",
    "Ryland Wells",
    "Cecilia Barron",
    "Dustin Brooks"] 
    randomname = names[randomint]
    return randomname
def randomhobby(): 
    randomint = random.randint(0,9)
    hobbies = [
        "Piano",
        "Soccer",
        "Bird watching",
        "Volleyball",
        "Music Production",
        "Watching Anime",
        "Studying",
        "Reading",
        "Golf",
        "Tap Dancing"
    ]
    randomhobby = hobbies[randomint]
    return randomhobby
def randomage():
    randomage = random.randint(10,100)
    return randomage
