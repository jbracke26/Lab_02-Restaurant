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
#from Class_Restaurant import restaurant, menuadd, menuremove, menuchange


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restaurant Lab")

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
        

        self.inner_layout.addWidget(self.AddItem)
        self.inner_layout.addWidget(self.SubItem)
        self.inner_layout.addWidget(self.EditItem)

        self.entree_widget = QListWidget()
        self.entree_widget.addItems(["entree 1", "entree 2", "entree 3"])

        self.appetizer_widget = QListWidget()
        self.appetizer_widget.addItems(["app 1", "app 2", "app 3"])

        self.dessert_widget = QListWidget()
        self.dessert_widget.addItems(["dessert 1", "dessert 2", "dessert 3"])

        self.drink_widget = QListWidget()
        self.drink_widget.addItems(["drink 1", "drink 2", "drink 3"])

        self.other_widget = QListWidget()
        self.other_widget.addItems(["misc 1", "misc 2", "misc 3"])

        layout.addWidget(self.inner_container)
        layout.addWidget(self.appetizer_widget)
        layout.addWidget(self.entree_widget)
        layout.addWidget(self.dessert_widget)
        layout.addWidget(self.drink_widget)
        layout.addWidget(self.other_widget)
        layout.addWidget(self.label)

    def remove_item(self, remove):


        
        pass

    def open_add_popup(self):
        popup = AddPopup(self)
        popup.exec()
        pass


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
        self.Category.addItems(["Appetizers & Sides", "Entrees", "Desserts", "Drink, Misc"])

        self.Save = QPushButton("Save")

        #self.Save.clicked.connect(self.save_item)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.nameInput)
        self.layout.addWidget(self.priceLabel)
        self.layout.addWidget(self.priceInput)
        self.layout.addWidget(self.Category)
        self.layout.addWidget(self.Save)

        #def save_item(self):
            #self.itemdata = {
                #"name": self.nameInput.toPlainText(),
                #"price": self.priceInput.toPlainText(),
                #"category": self.Category.currentText()
           # }
           # try :
         #       restaurant.menuadd(self.itemdata)
         #   except:
         #       print("Error")
          #  pass
          #  self.close()



app = QApplication()
window = MainWindow()
qt_themes.set_theme("catppuccin_latte")
window.show()
app.exec()
