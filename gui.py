from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel, 
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTextEdit,
    QSlider,
    QListWidget, 
    QHBoxLayout, 
    )
from PySide6.QtCore import Qt


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

        AddItem = QPushButton("Add Item")
        SubItem = QPushButton("Remove Item")

        #SubItem.clicked.connect(remove_item)
   
        inner_layout.addWidget(AddItem)
        inner_layout.addWidget(SubItem)

        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])





        layout.addWidget(inner_container)
        layout.addWidget(list_widget)
        layout.addWidget(label)

        def remove_item(remove):
            item = list_widget.currentItem()
            #removeitem()
            #refresh()

            







app = QApplication()
window = MainWindow()
window.show()
app.exec()
