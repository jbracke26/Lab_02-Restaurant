from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QHBoxLayout,
    QDialog,
    QTextEdit,
    QComboBox,
)
from PySide6.QtCore import Qt
import qt_themes
from utils import loadjson
from Class_Restaurant import restaurant


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restaurant Lab")

        self.restaurant = restaurant()

        # track selected item across all lists
        self.selected_item_id = None
        self.selected_item_data = None

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        self.label = QLabel("Welcome to Generic Restaurant Software")
        self.label.setAlignment(Qt.AlignCenter)

        self.inner_container = QWidget()
        self.inner_layout = QHBoxLayout(self.inner_container)

        self.AddItem = QPushButton("Add Item")
        self.SubItem = QPushButton("Remove Item")
        self.EditItem = QPushButton("Edit Item")

        self.AddItem.clicked.connect(self.open_add_popup)
        self.SubItem.clicked.connect(self.remove_selected_item)
        self.EditItem.clicked.connect(self.open_edit_popup)

        self.inner_layout.addWidget(self.AddItem)
        self.inner_layout.addWidget(self.SubItem)
        self.inner_layout.addWidget(self.EditItem)

        self.appetizer_widget = QListWidget()
        self.entree_widget = QListWidget()
        self.dessert_widget = QListWidget()
        self.drink_widget = QListWidget()
        self.other_widget = QListWidget()

        self.appetizer_widget.itemSelectionChanged.connect(self.appetizer_selected)
        self.entree_widget.itemSelectionChanged.connect(self.entree_selected)
        self.dessert_widget.itemSelectionChanged.connect(self.dessert_selected)
        self.drink_widget.itemSelectionChanged.connect(self.drink_selected)
        self.other_widget.itemSelectionChanged.connect(self.other_selected)

        self.load_menu()

        layout.addWidget(self.inner_container)

        # add labels and lists for each category
        appetizer_label = QLabel("Appetizers:")
        layout.addWidget(appetizer_label)
        layout.addWidget(self.appetizer_widget)

        entree_label = QLabel("Entrees:")
        layout.addWidget(entree_label)
        layout.addWidget(self.entree_widget)

        dessert_label = QLabel("Desserts:")
        layout.addWidget(dessert_label)
        layout.addWidget(self.dessert_widget)

        drink_label = QLabel("Drinks:")
        layout.addWidget(drink_label)
        layout.addWidget(self.drink_widget)

        other_label = QLabel("Other:")
        layout.addWidget(other_label)
        layout.addWidget(self.other_widget)

        layout.addWidget(self.label)

    def load_menu(self):
        # put json into lists
        menu_data = loadjson()

        # clear all lists
        self.appetizer_widget.clear()
        self.entree_widget.clear()
        self.dessert_widget.clear()
        self.drink_widget.clear()
        self.other_widget.clear()

        # add each to correct list
        for item in menu_data["menu"][0]["items"]:
            display_text = f"{item['name']} - ${item['price']}"

            if item["category"] == "Appetizers":
                self.appetizer_widget.addItem(display_text)
            elif item["category"] == "Entrees":
                self.entree_widget.addItem(display_text)
            elif item["category"] == "Desserts":
                self.dessert_widget.addItem(display_text)
            elif item["category"] == "Drinks":
                self.drink_widget.addItem(display_text)
            else:
                self.other_widget.addItem(display_text)

    def refresh_menu(self):
        self.load_menu()

    def appetizer_selected(self):
        self.item_selected("Appetizers")

    def entree_selected(self):
        self.item_selected("Entrees")

    def dessert_selected(self):
        self.item_selected("Desserts")

    def drink_selected(self):
        self.item_selected("Drinks")

    def other_selected(self):
        self.item_selected("Other")

    def item_selected(self, category):
        current_widget = None
        if category == "Appetizers":
            current_widget = self.appetizer_widget
        elif category == "Entrees":
            current_widget = self.entree_widget
        elif category == "Desserts":
            current_widget = self.dessert_widget
        elif category == "Drinks":
            current_widget = self.drink_widget
        else:
            current_widget = self.other_widget

        selected_items = current_widget.selectedItems()
        if selected_items:
            self.clear_other_selections(category)
            selected_text = selected_items[0].text()
            self.selected_item_data = self.find_item_by_text(selected_text, category)
            if self.selected_item_data:
                self.selected_item_id = self.selected_item_data["id"]
        else:
            self.selected_item_id = None
            self.selected_item_data = None

    def clear_other_selections(self, keep_category):
        if keep_category != "Appetizers":
            self.appetizer_widget.clearSelection()
        if keep_category != "Entrees":
            self.entree_widget.clearSelection()
        if keep_category != "Desserts":
            self.dessert_widget.clearSelection()
        if keep_category != "Drinks":
            self.drink_widget.clearSelection()
        if keep_category != "Other":
            self.other_widget.clearSelection()

    def find_item_by_text(self, display_text, category):
        menu_data = loadjson()
        parts = display_text.split(" - $")
        item_name = parts[0]

        for item in menu_data["menu"][0]["items"]:
            if item["name"] == item_name and item["category"] == category:
                return item
        return None

    def remove_selected_item(self):
        self.restaurant.menuremove(self.selected_item_id)
        self.refresh_menu()

        # clear selection to make sure edit works properly
        self.selected_item_id = None
        self.selected_item_data = None

    def open_add_popup(self):
        popup = AddPopup(self)
        popup.exec()
        pass

    def open_edit_popup(self):
        if self.selected_item_data is None:
            return

        popup = EditPopup(self, self.selected_item_data)
        popup.exec()


class AddPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Item")

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Add Item")
        self.label.setAlignment(Qt.AlignCenter)

        self.nameLabel = QLabel("Item Name:")
        self.nameLabel.setAlignment(Qt.AlignLeft)
        self.priceLabel = QLabel("Item Price:")
        self.priceLabel.setAlignment(Qt.AlignLeft)

        self.nameInput = QTextEdit()
        self.priceInput = QTextEdit()

        self.Category = QComboBox()
        self.Category.addItems(["Appetizers", "Entrees", "Desserts", "Drinks", "Other"])

        self.Save = QPushButton("Save")

        self.Save.clicked.connect(self.save_item)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.nameInput)
        self.layout.addWidget(self.priceLabel)
        self.layout.addWidget(self.priceInput)
        self.layout.addWidget(self.Category)
        self.layout.addWidget(self.Save)

    def save_item(self):
        # get data from input fields
        self.itemdata = {
            "name": self.nameInput.toPlainText(),
            "price": self.priceInput.toPlainText(),
            "category": self.Category.currentText(),
        }

        self.parent().restaurant.menuadd(self.itemdata)

        self.parent().refresh_menu()

        self.close()


class EditPopup(QDialog):
    def __init__(self, parent=None, item_data=None):
        super().__init__(parent)

        self.item_data = item_data
        self.setWindowTitle("Edit Item")

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Edit Item")
        self.label.setAlignment(Qt.AlignCenter)

        self.nameLabel = QLabel("Item Name:")
        self.nameLabel.setAlignment(Qt.AlignLeft)
        self.priceLabel = QLabel("Item Price:")
        self.priceLabel.setAlignment(Qt.AlignLeft)

        self.nameInput = QTextEdit()
        self.priceInput = QTextEdit()

        self.Category = QComboBox()
        self.Category.addItems(["Appetizers", "Entrees", "Desserts", "Drinks", "Other"])

        self.Save = QPushButton("Save")
        self.Save.clicked.connect(self.save_item)

        # fill with current data
        if item_data:
            self.nameInput.setPlainText(item_data["name"])
            self.priceInput.setPlainText(str(item_data["price"]))

            # set to current category
            category_index = self.Category.findText(item_data["category"])
            if category_index >= 0:
                self.Category.setCurrentIndex(category_index)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.nameInput)
        self.layout.addWidget(self.priceLabel)
        self.layout.addWidget(self.priceInput)
        self.layout.addWidget(self.Category)
        self.layout.addWidget(self.Save)

    def save_item(self):
        updated_data = {
            "name": self.nameInput.toPlainText(),
            "price": self.priceInput.toPlainText(),
            "category": self.Category.currentText(),
        }

        self.parent().restaurant.menuchange(self.item_data["id"], updated_data)

        self.parent().refresh_menu()

        self.close()


app = QApplication()
window = MainWindow()
qt_themes.set_theme("catppuccin_latte")
window.show()
app.exec()
