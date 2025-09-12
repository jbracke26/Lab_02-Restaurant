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
from Class_Restaurant import restaurant


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restaurant Lab")

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        label = QLabel("Welcome to Generic Restaurant Software")
        label.setAlignment(Qt.AlignCenter)

        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)

        self.AddItem = QPushButton("Add Item")
        self.SubItem = QPushButton("Remove Item")
        self.EditItem = QPushButton("Edit Item")

        self.AddItem.clicked.connect(self.open_add_popup)
        # SubItem.clicked.connect(remove_item)

        inner_layout.addWidget(self.AddItem)
        inner_layout.addWidget(self.SubItem)
        inner_layout.addWidget(self.EditItem)

        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])

        layout.addWidget(inner_container)
        layout.addWidget(list_widget)
        layout.addWidget(label)

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
