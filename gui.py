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


class AddPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Item")

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Add Item")
        self.label.setAlignment(Qt.AlignCenter)

        self.Name = QTextEdit("Name")
        self.Price = QTextEdit("Price")

        self.Category = QComboBox()
        self.Category.addItems(["Appetizers & Sides", "Entrees", "Desserts", "Drinks"])

        self.Save = QPushButton("Save")

        self.Save.clicked.connect(self.close)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.Name)
        self.layout.addWidget(self.Price)
        self.layout.addWidget(self.Category)
        self.layout.addWidget(self.Save)


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
        SubItem = QPushButton("Remove Item")

        self.AddItem.clicked.connect(self.open_add_popup)
        # SubItem.clicked.connect(remove_item)

        inner_layout.addWidget(self.AddItem)
        inner_layout.addWidget(SubItem)

        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])

        layout.addWidget(inner_container)
        layout.addWidget(list_widget)
        layout.addWidget(label)

    def remove_item(self, remove):
        # TODO: Implement item removal functionality
        pass

    def open_add_popup(self):
        popup = AddPopup(self)
        popup.exec()
        pass


app = QApplication()
window = MainWindow()
window.show()
app.exec()
