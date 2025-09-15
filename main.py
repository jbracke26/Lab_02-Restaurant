from gui import MainWindow
from PySide6.QtWidgets import QApplication
import qt_themes

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    qt_themes.set_theme("catppuccin_latte")
    window.show()
    app.exec()