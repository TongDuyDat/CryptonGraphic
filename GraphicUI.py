import time
from PyQt5 import QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
import UIinputKey
from handleKeyboardShortcuts import KeyPeressed

'''----------------------------------------------------
----------------------------------------------'''


class MainUserInterface(QtWidgets.QMainWindow, KeyPeressed):
    def __init__(self, keys=0):
        super(MainUserInterface, self).__init__()
        uic.loadUi("mainUI.ui", self)
        self.UIinputkey= UIinputKey.keyUI(self)
# tạo các tính năng cho các nút bấm
        self.rdnewFile.clicked.connect(self.set_checked_new)
        self.rdoldFile.clicked.connect(self.set_checked_old)
        self.btOk.clicked.connect(self.mahoafile)
        self.btReset.clicked.connect(self.reset)
        self.OpenFileSrc.clicked.connect(self.openfile)
        self.OpenFileSave.clicked.connect(self.openfolder)
        self.btGM.clicked.connect(self.giaimafile)
        self.EncryptionType.currentIndexChanged.connect(self.choose_encryption_type)
        self.Bar.setValue(0)
# tính năng gõ các phím tắt trên bàn phím
        self.shortcutopen.activated.connect(self.openfile)
        self.shortcutsave.activated.connect(self.mahoafile)
        self.shortcutsaveas.activated.connect(self.openfolder)
        self.shortcutexit.activated.connect(self.close)
    # các phương thức
    # bắt sự kiện click button File mới và mở phần chọn file để lưu
    def set_checked_new(self):
        self.rdnewFile.setChecked(True)
        if self.rdnewFile.isChecked():
            self.textSaveFile.setEnabled(True)
            self.OpenFileSave.setEnabled(True)
            self.textSaveFile.setText("")

    # bắt sự kiện click button ghì Đè và ẩn phần chọn file để lưu
    def set_checked_old(self):
        self.rdoldFile.setChecked(True)
        if self.rdoldFile.isChecked():
            self.textSaveFile.setEnabled(False)
            self.OpenFileSave.setEnabled(False)
            self.textSaveFile.setText(self.teSrcFile.text())
    def reset(self):
        self.teSrcFile.setText("")
        self.textSaveFile.setText("")
        self.rdoldFile.setChecked(True)

    def openfile(self):
        response = QFileDialog.getOpenFileNames(
            parent=self
        )
        filename = ",".join(response[0])
        self.teSrcFile.setText(str(filename))
        self.textSaveFile.setText(self.teSrcFile.text())

    def openfolder(self):
        if self.rdnewFile.isChecked():
            text_filename = self.teSrcFile.text()
            try:
                text_filename_extensions = text_filename[len(text_filename) - text_filename[::-1].find(".")::]
                text_filename_defaut = "/home/jana/untitled." + text_filename_extensions
            except:
                text_filename_defaut = "/home/jana/untitled.txt"

            response = QFileDialog.getSaveFileName(self,
                                                   "Select Save File",
                                                   text_filename_defaut,
                                                   "All (*) ;; Text File(*.txt *.docx *.doc *.pdf) ;; Videos (*.mp4) ;;"
                                                   " Audio (*.mp3) ;; Images (*.png *.xpm *.jpg)")
            self.textSaveFile.setText(response[0])
    def choose_encryption_type(self) -> 0:
        index = self.EncryptionType.currentIndex()
        return index

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key_Return:
            self.mahoafile()
    def bars(self):
        for i in range(100):
            self.Bar.setValue(i)
            time.sleep(0.1)
    def mahoafile(self):
        self.UIinputkey.textBoxK.setText("")
        srcfile = self.teSrcFile.text()
        self.UIinputkey.src = srcfile
        desfile = self.textSaveFile.text()
        self.UIinputkey.des = desfile
        typeEncryption = self.choose_encryption_type()
        self.UIinputkey.type = typeEncryption
        self.UIinputkey.show()
        self.UIinputkey.buttonBoxOk.accepted.connect(self.UIinputkey.mahoa)

    def giaimafile(self):
        self.UIinputkey.textBoxK.setText("")
        srcfile = self.teSrcFile.text()
        self.UIinputkey.src = srcfile
        desfile = self.textSaveFile.text()
        self.UIinputkey.des = desfile
        typeEncryption = self.choose_encryption_type()
        self.UIinputkey.type = typeEncryption
        self.UIinputkey.show()
        self.UIinputkey.buttonBoxOk.accepted.connect(self.UIinputkey.giaima)