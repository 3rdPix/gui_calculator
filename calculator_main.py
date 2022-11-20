import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

form_main = uic.loadUiType("calculator2.ui")[0]  # ui 파일 불러오기


class MainWindow(QMainWindow, form_main):
    def __init__(self):
        super().__init__()
        self.initUI(),
        self.show()

    def initUI(self):
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.button_1)   # 버튼 클릭시 연결 되는 함수
        self.pushButton_2.clicked.connect(self.button_2)
        self.pushButton_3.clicked.connect(self.button_3)
        self.pushButton_4.clicked.connect(self.button_4)
        self.pushButton_5.clicked.connect(self.button_5)
        self.pushButton_6.clicked.connect(self.button_6)
        self.pushButton_7.clicked.connect(self.button_7)
        self.pushButton_8.clicked.connect(self.button_8)
        self.pushButton_9.clicked.connect(self.button_9)
        self.pushButton_0.clicked.connect(self.button_0)
        self.pushButton_00.clicked.connect(self.button_00)
        self.pushButton_dot.clicked.connect(self.button_dot)
        self.pushButton_DEL.clicked.connect(self.del_num)
        self.pushButton_C.clicked.connect(self.clr_num)
        self.pushButton_CE.clicked.connect(self.clr_num)
        self.pushButton_plus.clicked.connect(self.plus)
        self.pushButton_minus.clicked.connect(self.minus)
        self.pushButton_mult.clicked.connect(self.multiple)
        self.pushButton_divide.clicked.connect(self.divide)
        self.pushButton_equal.clicked.connect(self.equal)
        self.pushButton_percent.clicked.connect(self.percent)

    def button_1(self):
        self.number("1")

    def button_2(self):
        self.number("2")

    def button_3(self):
        self.number("3")

    def button_4(self):
        self.number("4")

    def button_5(self):
        self.number("5")

    def button_6(self):
        self.number("6")

    def button_7(self):
        self.number("7")

    def button_8(self):
        self.number("8")

    def button_9(self):
        self.number("9")

    def button_0(self):
        self.number("0")

    def button_00(self):
        self.number("00")

    def button_dot(self):
        self.number(".")

    def number(self, num):
        exist_text = self.lineEdit.text()   # lineEdit값을 가져와서 exist_text에 저장
        self.lineEdit.setText(exist_text+num)   # 기존값 + 새로 입력된 값

    def del_num(self):
        exist_text = self.lineEdit.text()
        self.lineEdit.setText(exist_text[:-1])

    def clr_num(self):
        exit_text = self.lineEdit.setText("")

    def plus(self):
        exist_text = self.lineEdit.text()
        # 연산 기호가 여러개 입력되면 그 중 맨 마지막으로 입력 받은 기호만이 수행된다.
        if((exist_text[-1]=="+")|(exist_text[-1]=="-")|(exist_text[-1]=="*")|(exist_text[-1]=="/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        self.number("+")

    def minus(self):
        exist_text = self.lineEdit.text()
        # 연산 기호가 여러개 입력되면 그 중 맨 마지막으로 입력 받은 기호만이 수행된다.
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        self.number("-")

    def multiple(self):
        exist_text = self.lineEdit.text()
        # 연산 기호가 여러개 입력되면 그 중 맨 마지막으로 입력 받은 기호만이 수행된다.
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        self.number("*")

    def divide(self):
        exist_text = self.lineEdit.text()
        # 연산 기호가 여러개 입력되면 그 중 맨 마지막으로 입력 받은 기호만이 수행된다.
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        self.number("/")

    def percent(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        ans = float(exist_text)*0.01
        self.lineEdit.setText(str(ans))


    def equal(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        self.number("=")
        try:
            ans = eval(exist_text)
            self.lineEdit.setText(str(ans))
        except Exception as e:
            print(e)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
