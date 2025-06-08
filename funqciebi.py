from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
import sys
from math import sqrt, factorial, pow, e

from kalkulatori_ui import Ui_Dialog

class Calculator(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.expression = ""

        # ციფრები და ძირითადი ოპერატორები
        self.ui.pushButton_5.clicked.connect(lambda: self.add_to_expression("1"))
        self.ui.pushButton_6.clicked.connect(lambda: self.add_to_expression("2"))
        self.ui.pushButton_10.clicked.connect(lambda: self.add_to_expression("3"))
        self.ui.pushButton.clicked.connect(lambda: self.add_to_expression("4"))
        self.ui.pushButton_11.clicked.connect(lambda: self.add_to_expression("5"))
        self.ui.pushButton_2.clicked.connect(lambda: self.add_to_expression("6"))
        self.ui.pushButton_4.clicked.connect(lambda: self.add_to_expression("7"))
        self.ui.pushButton_12.clicked.connect(lambda: self.add_to_expression("8"))
        self.ui.pushButton_8.clicked.connect(lambda: self.add_to_expression("9"))
        self.ui.pushButton_3.clicked.connect(lambda: self.add_to_expression("0"))

        self.ui.pushButton_7.clicked.connect(lambda: self.add_to_expression("+"))
        self.ui.pushButton_13.clicked.connect(lambda: self.add_to_expression("-"))
        self.ui.pushButton_23.clicked.connect(lambda: self.add_to_expression("/"))
        self.ui.pushButton_9.clicked.connect(lambda: self.add_to_expression("*"))
        self.ui.pushButton_21.clicked.connect(lambda: self.add_to_expression("**"))
        self.ui.pushButton_22.clicked.connect(lambda: self.add_to_expression("("))
        self.ui.pushButton_14.clicked.connect(lambda: self.add_to_expression(")"))
        self.ui.pushButton_19.clicked.connect(lambda: self.add_to_expression(str(e)))

        # ფუნქციები
        self.ui.pushButton_25.clicked.connect(lambda: self.add_to_expression("sqrt("))
        self.ui.pushButton_24.clicked.connect(lambda: self.add_to_expression("1/("))
        self.ui.pushButton_26.clicked.connect(lambda: self.add_to_expression("10**"))
        self.ui.pushButton_17.clicked.connect(lambda: self.add_to_expression("abs("))
        self.ui.pushButton_16.clicked.connect(lambda: self.add_to_expression("**2"))
        self.ui.pushButton_15.clicked.connect(self.add_factorial)

        # გათვლის ღილაკი "="
        self.ui.pushButton_18.clicked.connect(self.calculate)

    def add_to_expression(self, value):
        self.expression += value
        self.ui.textBrowser.setText(self.expression)

    def add_factorial(self):
        try:
            result = str(factorial(int(eval(self.expression))))
            self.ui.textBrowser.setText(result)
            self.expression = result
        except Exception as e:
            self.ui.textBrowser.setText("შეცდომა")
            self.expression = ""

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.ui.textBrowser.setText(result)
            self.expression = result
        except Exception as e:
            self.ui.textBrowser.setText("შეცდომა")
            self.expression = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
