from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget,QShortcut
from PyQt5.QtGui import QKeySequence
import ErrorHandling
import EncryptionSystems

class keyUI(QtWidgets.QMainWindow, QWidget):
    src = None
    des = None
    type = None
    def __init__(self, parent=None):
        super(keyUI, self).__init__(parent)
        uic.loadUi("keyUI.ui", self)
        self.buttonBoxOk.rejected.connect(self.close)
        self.schortcutclose = QShortcut(QKeySequence("Ctrl+W"),self)
        self.schortcutclose.activated.connect(self.close)
        # self.src = None
        # self.des = None
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key_Return:
            self.mahoa()
    def mahoa(self):
        if self.type ==0 or self.type ==1:
            key = ErrorHandling.ErrKey().errCaeser(self, self.textBoxK.text())
            isfile = ErrorHandling.ErrFile().errFilename(self.parent(), self.src, self.des)
            if isfile and key != False:
                self.close()
                self.parent().bars()
                EncryptionSystems.Caeser().mahoafile(self.src, self.des, key)
                self.parent().Bar.setValue(100)
        elif self.type == 2:
            key = ErrorHandling.ErrKey().errRC4(self, self.textBoxK.text())
            isfile = ErrorHandling.ErrFile().errFilename(self.parent(), self.src, self.des)
            if isfile and key != False:
                self.close()
                self.parent().bars()
                EncryptionSystems.RC4().mahoafile(self.src, self.des, key)
                self.parent().Bar.setValue(100)
    def giaima(self):
        if self.type ==0 or self.type ==1:
            key = ErrorHandling.ErrKey().errCaeser(self, self.textBoxK.text())
            isfile = ErrorHandling.ErrFile().errFilename(self.parent(), self.src, self.des)
            if isfile and key!= False:
                self.close()
                self.parent().bars()
                EncryptionSystems.Caeser().giaimafile(self.src, self.des, key)
                self.parent().Bar.setValue(100)
            self.close()
        elif self.type == 2:
            key = ErrorHandling.ErrKey().errRC4(self, self.textBoxK.text())
            isfile = ErrorHandling.ErrFile().errFilename(self.parent(), self.src, self.des)
            if isfile and key != False:
                self.close()
                self.parent().bars()
                EncryptionSystems.RC4().giaimafile(self.src, self.des, key)
                self.parent().Bar.setValue(100)

'''app=QtWidgets.QApplication(sys.argv)
Form1=FormKhoaK()
Form1.show()
app.exec()
'''
