import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget,QMessageBox


class Example(QWidget): #inherit from the QtWidget class

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self) :
        self.resize(250, 250)
        self.center()
        self.setWindowTitle('Sarah Assist')   #Window title
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def closeEvent(self,event):
        replay = QMessageBox.question(self,'Message','Are you sure to quit',
                                      QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if replay == QMessageBox.Yes:
            event.accept()
        else :
            event.ignore()

        
if __name__ == "__main__" :

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

 
