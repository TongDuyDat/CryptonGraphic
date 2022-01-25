import sys
from PyQt5 import QtWidgets
import GraphicUI
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    UImain = GraphicUI.MainUserInterface()
    UImain.show()
    app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
