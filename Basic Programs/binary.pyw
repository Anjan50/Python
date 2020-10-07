from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #f4f9f4;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTitle = QtWidgets.QLabel(self.centralwidget)
        self.mainTitle.setGeometry(QtCore.QRect(120, 0, 471, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(36)
        self.mainTitle.setFont(font)
        self.mainTitle.setObjectName("mainTitle")
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        self.description_label.setGeometry(QtCore.QRect(190, 50, 331, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.description_label2 = QtWidgets.QLabel(self.centralwidget)
        self.description_label2.setGeometry(QtCore.QRect(190, 90, 261, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.description_label2.setFont(font)
        self.description_label2.setWordWrap(True)
        self.description_label2.setObjectName("description_label2")
        self.ascii_to_char = QtWidgets.QPushButton(self.centralwidget)
        self.ascii_to_char.setGeometry(QtCore.QRect(550, 160, 131, 61))
        self.ascii_to_char.setStyleSheet("QPushButton#ascii_to_char {\n"
"    font: 10pt \"OCR A Extended\";\n"
"    background-color: #dde9b9;\n"
"}")
        self.ascii_to_char.setObjectName("ascii_to_char")
        self.int_to_binary = QtWidgets.QPushButton(self.centralwidget)
        self.int_to_binary.setGeometry(QtCore.QRect(440, 330, 241, 61))
        self.int_to_binary.setStyleSheet("QPushButton#int_to_binary {\n"
"    font: 10pt \"OCR A Extended\";\n"
"    background-color: #dde9b9;\n"
"}")
        self.int_to_binary.setObjectName("int_to_binary")
        self.binary_to_int = QtWidgets.QPushButton(self.centralwidget)
        self.binary_to_int.setGeometry(QtCore.QRect(10, 330, 241, 61))
        self.binary_to_int.setStyleSheet("QPushButton#binary_to_int {\n"
"    font: 10pt \"OCR A Extended\";\n"
"    background-color: #dde9b9;\n"
"}")
        self.binary_to_int.setObjectName("binary_to_int")
        self.char_to_ascii = QtWidgets.QPushButton(self.centralwidget)
        self.char_to_ascii.setGeometry(QtCore.QRect(10, 160, 131, 61))
        self.char_to_ascii.setStyleSheet("QPushButton#char_to_ascii {\n"
"    font: 10pt \"OCR A Extended\";\n"
"    background-color: #dde9b9;\n"
"}")
        self.char_to_ascii.setObjectName("char_to_ascii")
        self.input_int = QtWidgets.QLineEdit(self.centralwidget)
        self.input_int.setGeometry(QtCore.QRect(390, 410, 291, 31))
        self.input_int.setText("")
        self.input_int.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_int.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_int.setClearButtonEnabled(True)
        self.input_int.setObjectName("input_int")
        self.input_binary = QtWidgets.QLineEdit(self.centralwidget)
        self.input_binary.setGeometry(QtCore.QRect(10, 410, 291, 31))
        self.input_binary.setClearButtonEnabled(True)
        self.input_binary.setObjectName("input_binary")
        self.input_ascii = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ascii.setGeometry(QtCore.QRect(530, 240, 151, 31))
        self.input_ascii.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_ascii.setClearButtonEnabled(True)
        self.input_ascii.setObjectName("input_ascii")
        self.input_char = QtWidgets.QLineEdit(self.centralwidget)
        self.input_char.setGeometry(QtCore.QRect(10, 240, 151, 31))
        self.input_char.setClearButtonEnabled(True)
        self.input_char.setObjectName("input_char")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTitle.setText(_translate("MainWindow", "Binary Converter"))
        self.description_label.setText(_translate("MainWindow", "- Convert an integer to binary - Convert binary to an integer"))
        self.description_label2.setText(_translate("MainWindow", "- Convert Char to ASCII - Convert ASCII to char"))
        self.ascii_to_char.setText(_translate("MainWindow", "ASCII -> Char"))
        self.int_to_binary.setText(_translate("MainWindow", "Integer -> Binary"))
        self.binary_to_int.setText(_translate("MainWindow", "Binary -> Integer"))
        self.char_to_ascii.setText(_translate("MainWindow", "Char -> ASCII"))
        self.input_int.setPlaceholderText(_translate("MainWindow", "Integer (Non-Negative)  "))
        self.input_binary.setPlaceholderText(_translate("MainWindow", "  Binary "))
        self.input_ascii.setPlaceholderText(_translate("MainWindow", "ASCII value  "))
        self.input_char.setPlaceholderText(_translate("MainWindow", "  Character(s)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
