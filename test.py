import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(object):
    def setupUi(self, Form):
        Form.setObjectName("Calculator")
        Form.resize(333, 315)
        self.textEdit_show = QtWidgets.QTextEdit(Form)
        self.textEdit_show.setGeometry(QtCore.QRect(10, 10, 311, 41))
        self.textEdit_show.setObjectName("textEdit_show")
        self.textEdit_result = QtWidgets.QTextEdit(Form)
        self.textEdit_result.setGeometry(QtCore.QRect(10, 50, 311, 41))
        self.textEdit_result.setObjectName("textEdit_result")
        self.pushButton_del = QtWidgets.QPushButton(Form)
        self.pushButton_del.setGeometry(QtCore.QRect(10, 110, 75, 31))
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_square = QtWidgets.QPushButton(Form)
        self.pushButton_square.setGeometry(QtCore.QRect(90, 110, 75, 31))
        self.pushButton_square.setObjectName("pushButton_square")
        self.pushButton_root = QtWidgets.QPushButton(Form)
        self.pushButton_root.setGeometry(QtCore.QRect(170, 110, 75, 31))
        self.pushButton_root.setObjectName("pushButton_root")
        self.pushButton_div = QtWidgets.QPushButton(Form)
        self.pushButton_div.setGeometry(QtCore.QRect(250, 110, 75, 31))
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 150, 75, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 150, 75, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_mul = QtWidgets.QPushButton(Form)
        self.pushButton_mul.setGeometry(QtCore.QRect(250, 150, 75, 31))
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(170, 150, 75, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 75, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 190, 75, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_plus = QtWidgets.QPushButton(Form)
        self.pushButton_plus.setGeometry(QtCore.QRect(250, 190, 75, 31))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 190, 75, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 230, 75, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 230, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_sub = QtWidgets.QPushButton(Form)
        self.pushButton_sub.setGeometry(QtCore.QRect(250, 230, 75, 31))
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 230, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_percent = QtWidgets.QPushButton(Form)
        self.pushButton_percent.setGeometry(QtCore.QRect(10, 270, 75, 31))
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_0 = QtWidgets.QPushButton(Form)
        self.pushButton_0.setGeometry(QtCore.QRect(90, 270, 75, 31))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_equal = QtWidgets.QPushButton(Form)
        self.pushButton_equal.setGeometry(QtCore.QRect(250, 270, 75, 31))
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_dot = QtWidgets.QPushButton(Form)
        self.pushButton_dot.setGeometry(QtCore.QRect(170, 270, 75, 31))
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.pushButton_del.setText(_translate("Form", "Del"))
        self.pushButton_square.setText(_translate("Form", "^2"))
        self.pushButton_root.setText(_translate("Form", "^1/2"))
        self.pushButton_div.setText(_translate("Form", "/"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_mul.setText(_translate("Form", "*"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_sub.setText(_translate("Form", "-"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_percent.setText(_translate("Form", "%"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_equal.setText(_translate("Form", "="))
        self.pushButton_dot.setText(_translate("Form", "."))

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer, QDateTime, QBasicTimer
from PyQt5.QtGui import QIcon, QTextDocument
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

from test import Window
class mywindow(QtWidgets.QWidget, Window):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        # номер ключа
        self.pushButton_0.clicked.connect(self.printNumber_0)
        self.pushButton_1.clicked.connect(self.printNumber_1)
        self.pushButton_2.clicked.connect(self.printNumber_2)
        self.pushButton_3.clicked.connect(self.printNumber_3)
        self.pushButton_4.clicked.connect(self.printNumber_4)
        self.pushButton_5.clicked.connect(self.printNumber_5)
        self.pushButton_6.clicked.connect(self.printNumber_6)
        self.pushButton_7.clicked.connect(self.printNumber_7)
        self.pushButton_8.clicked.connect(self.printNumber_8)
        self.pushButton_9.clicked.connect(self.printNumber_9)
        self.pushButton_plus.clicked.connect(self.printNumber_plus)
        self.pushButton_sub.clicked.connect(self.printNumber_sub)
        self.pushButton_mul.clicked.connect(self.printNumber_mul)
        self.pushButton_div.clicked.connect(self.printNumber_div)
        self.pushButton_dot.clicked.connect(self.printNumber_dot)
        self.pushButton_percent.clicked.connect(self.printNumber_percent)
        self.pushButton_square.clicked.connect(self.printNumber_square)
        self.pushButton_root.clicked.connect(self.printNumber_root)
        self.pushButton_equal.clicked.connect(self.calculate)
        self.pushButton_del.clicked.connect(self.deleteContent)
        # Прямое отображение

    def printNumber_0(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("0")

    def printNumber_1(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("1")

    def printNumber_2(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("2")

    def printNumber_3(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("3")

    def printNumber_4(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("4")

    def printNumber_5(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("5")

    def printNumber_6(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("6")

    def printNumber_7(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("7")

    def printNumber_8(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("8")

    def printNumber_9(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("9")

    def printNumber_plus(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("+")

    def printNumber_sub(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("-")

    def printNumber_mul(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("*")

    def printNumber_div(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("/")

    def printNumber_dot(self):
        self.isEqual()
        self.textEdit_show.insertPlainText(".")

    def printNumber_percent(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("%")

    def printNumber_square(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("^2")

    def printNumber_root(self):
        self.isEqual()
        self.textEdit_show.insertPlainText("^(1/2)")

    def isEqual(self):
        content = self.textEdit_show.toPlainText()
        tag = content.find('=')
        print(self.textEdit_show.toPlainText())
        print("tag:  " + str(tag))
        if tag != -1:
            self.textEdit_show.setText("")

    def deleteContent(self):
        self.textEdit_show.setText("")
        self.textEdit_result.setText("")

    def calculate(self):
        self.textEdit_show.insertPlainText("=")
        content = self.textEdit_show.toPlainText()
        print(content)

        tmp = ""
        sign = list()
        num_list = list()
        for i in range(len(content)):
            # Число

            if content[i] not in "+-*/()%^":

                #                tmp.append(content[i])
                tmp = tmp + content[i]
                # Характер
            elif tmp != '':
                num_list.append(float(tmp))
                tmp = ""
                sign.append(content[i])
            elif tmp == '':
                sign.append(content[i])
        aa = tmp.split('=')
        if aa[0] != float:
            print("Calculate wrong!")
            self.textEdit_result.setText("Wrong!")
        if aa[0] != '':
            try:
                num_list.append(float(aa[0]))
            except ValueError:
                self.textEdit_result.setText("Wrong!")
                return
        print(num_list)
        print(sign)

        # Операция
        # % Квадратный корень
        i = 0
        while i < len(sign):
            # Процент
            if sign[i] == '%':
                try:
                    num_list[i] = float(num_list[i] / 100)
                except IndexError:
                    self.textEdit_result.setText("Wrong!")
                    return
                num_list[i] = float(num_list[i] / 100)
                del (sign[i])
                # Квадрат
            elif sign[i] == '^' and num_list[i + 1] == 2:
                num_list[i] = num_list[i] * num_list[i]
                del (sign[i])
                del (num_list[i + 1])
                # Квадратный корень
            elif sign[i] == '^' and sign[i + 1] == '(':
                import math
                num_list[i] = float(math.sqrt(num_list[i]))
                del (num_list[i + 2])
                del (num_list[i + 1])
                del (sign[i + 3])
                del (sign[i + 2])
                del (sign[i + 1])
                del (sign[i])
            else:
                i = i + 1


        # + - * /
        try:
            result = num_list[0]
        except IndexError:
            self.textEdit_result.setText("Wrong!")
            return
        result = num_list[0]
        for i in range(len(sign)):

            if sign[i] == '*':
                result = result * num_list[i + 1]
            elif sign[i] == '/' and num_list[i + 1] != 0:
                result = result / num_list[i + 1]

            elif sign[i] == '+':
                result = result + num_list[i + 1]
            elif sign[i] == '-':
                result = result - num_list[i + 1]
            else:
                print("Calculate wrong!")
                self.textEdit_result.setText("Wrong!")
                return
        self.textEdit_result.setText(str(result))

if __name__ == "__main__":
    import sys


    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    win= mywindow()
    win.show()
    sys.exit(app.exec_())