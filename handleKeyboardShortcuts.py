from PyQt5.QtWidgets import QWidget,QShortcut
from PyQt5.QtGui import QKeySequence
class KeyPeressed(QWidget):
    def __init__(self):
        super(KeyPeressed, self).__init__()
#khởi tạo các phím bấm
        self.shortcutopen = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcutsaveas = QShortcut(QKeySequence("Ctrl+Shift+S"), self)
        self.shortcutclose =QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcutsave = QShortcut(QKeySequence("Ctrl+S"),self)
        self.shortcutexit = QShortcut(QKeySequence("esc"),self)