from PySide6.QtWidgets import QApplication
from Ui import Project
import os

if __name__ == '__main__':
    app = QApplication([])

    base_dir = os.path.dirname(os.path.abspath(__file__))
    style_path = os.path.join(base_dir, "style.qss")

    with open(style_path, "r") as arquivo:
        app.setStyleSheet(arquivo.read())
    
    projeto = Project()
    projeto.show()
    app.exec()
