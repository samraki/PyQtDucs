import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QToolTip,QMessageBox
from PyQt5.QtGui import QFont


class Example(QWidget): #inherit from the QtWidget class

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self) :
        QToolTip.setFont(QFont('SanaSerif', 10))  #this code set the font family and font size
        self.setToolTip("<b>Sarah is a <u>Free</u> and <u>Open Sorce</u> Text assistant</b>")
        qbtn = QPushButton('Submit',self)
        #qbtn.clicked.connect(self.close) uptional
        qbtn.move(20,20)
        qbtn.setToolTip("Start")
        self.setGeometry(300,300,500,500)   #1st and 2nd numbers are position and 3th and 4th are resizing
        self.setWindowTitle('Sarah Assist')   #Window title
        self.show()
        
    def closeEvent(self,event):
        replay = QMessageBox.question(self,'Message','Are you sure to quit',
                                      QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if replay == QMessageBox.Yes:
            event.assept()
        else :
            event.ignore()

        
if __name__ == "__main__" :

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

