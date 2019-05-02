import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QToolTip
from PyQt5.QtGui import QFont


class Example(QWidget): #inherit from the QtWidget class

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self) :
        QToolTip.setFont(QFont('SanaSerif', 10))  #this code set the font family and font size
        self.setToolTip("<b>Sarah is a <u>Free</u> and <u>Open Sorce</u> Text assistant</b>")
        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(self.close)
        qbtn.move(20,20)
        self.setGeometry(300,300,500,500)   #1st and 2nd numbers are position and 3th and 4th are resizing
        self.setWindowTitle('Sarah Assist')   #Window title
        self.show()

if __name__ == "__main__" :

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

