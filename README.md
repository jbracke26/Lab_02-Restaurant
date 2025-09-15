# Restaurant Menu App

An application for managing a restaurant's menu. 

## Features

Items displayed by category:
   - Appetizers
   - Main Courses
   - Desserts
   - Drinks
Add new items with the following details:
   - Name
   - Description
   - Price
   - Category
Edit existing menu items
   - Auto populate existing details
   - Modify details
Remove menu items
   - Select item from any list, most recent item is used
   - Click remove button to remove item
   - Deletes from json and gui
Data automatically saved to JSON file afte every action

## Installation

Have Python installed on your system.


Install required packages with command:
   pip install -r requirements.txt


Run the Application through main.py

## Usage


**Adding Items**: Click "Add Item" button, put information in popup, and click save to save to json and show on gui.
**Editing Items**: Select the desired item from any list, click "Edit item" button, modify the information in the popup, and click save to save to json and show on gui. (Only the most recently selected item is used, not the selected item in each list)
**Removing Items**: Select the desired item from any list, click "Remove item" button, and click save to save to json and remove from gui. (Only the most recently selected item is used, not the selected item in each list)

All actions automatically save to menu.json and refresh the gui.