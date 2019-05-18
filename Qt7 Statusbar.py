import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Example(QMainWindow): #inherit from the QtWidget class
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self) :
        self.setGeometry(300,300,500,400)   #1st and 2nd numbers are position and 3th and 4th are resizing
        self.setWindowTitle('Sarah Assist')   #Window title
        self.statusBar().showMessage("Ready")
        self.show()

if __name__ == "__main__" :

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
