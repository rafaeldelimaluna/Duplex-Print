from pathlib import Path
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow,QLineEdit,QPushButton,QApplication,QWidget
from PyQt6.QtCore import Qt
from re import compile

pat = compile(r"continuar")


gui_path = Path("/home/rafae/Programacao/PYTHON/APPs/duplex-print/gui/gui.ui")
gui_path = gui_path.__str__().removeprefix("b'")

class Dialog(QMainWindow):
    is_continue = False
    def __init__(self):
        super().__init__()
        uic.loadUi(gui_path,self)
        self.resize(400,200)

        self.line_edit = self.findChild(QLineEdit,"lineEditField")
        self.abort_button = self.findChild(QPushButton,"AbortButton")

        self.abort_button.clicked.connect(lambda x:self.__set_false())
        self.line_edit.textChanged.connect(self.verify)

        
        self.show()
    def verify(self,text):
        if pat.match(text.lower()):
            Dialog.is_continue = True
            self.close()

    def __set_false(self):
        Dialog.is_continue = False
        self.close()


app = QApplication([])
class Question():
    def __init__(self) -> None:
        self.ui = Dialog()
    def start(self):
        app.focusWindow()
        app.exec()
        return self.ui.is_continue