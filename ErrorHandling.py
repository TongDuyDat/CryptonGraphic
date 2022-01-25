from PyQt5.QtWidgets import QMessageBox
class ErrKey:
    def __init__(self):
        pass
    def errCaeser (sefl, parent, Key):
        if Key != "":
            try:
                List = list(map(int, Key.strip().split(" ")))
                return List
            except:
                QMessageBox.information(parent,"Error Key", "Bạn đã nhập sai định dạng của khóa K\n"
                                                                   "Mỗi chữ số cách nhau một dấu space \n"
                                                                   "Vd: 1 2 3 4 5" )
                return False
    def errRC4(self, parent, Key):
        if len(Key) < 256:
            return Key
        else:
            QMessageBox.information(parent, "Error Key", "Khóa chỉ có tối đa 256 kí tự ")
class ErrFile:
    def __init__(self):
        pass
    def errFilename(self, parent, filesrc, filedes):
        result = [True,True]
        try:
            f= open(filesrc,"rb")
            return True
        except:
            # parent.label_Err_name_filersc.setText("Lỗi")
            QMessageBox.information(parent, "Error Key", "Lỗi file vào lỗi")
            return False
        # try:
        #     f=open(filedes,"rb")
        # except:
        #     QMessageBox.information(parent, "Error Key", "Lỗi file đích")
        #     parent.label_Err_name_filedes.setText("Lỗi")