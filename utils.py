import json
from pathlib import Path
def load_menu(filename):
    with open (filename, 'r') as file:
        menu = json.loads()
        return(menu)

