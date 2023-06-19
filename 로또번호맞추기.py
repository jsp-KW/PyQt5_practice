import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import random

form = uic.loadUiType("lottoGUI.ui")[0]

class myWindow(QMainWindow, form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowIcon(QIcon("pagicacha.png"))
        self.lineEdit.setFocus()

        self.pushButton.clicked.connect(self.start)
        self.lineEdit.returnPressed.connect(self.start)

    def start(self):
        self.com()

    def com(self):
        lotto_li = []
        while True:
            num = random.randint(1, 45)
            if num not in lotto_li:
                lotto_li.append(num)

            if len(lotto_li) == 6:
                break

        print("당첨 번호 =", lotto_li)

        if self.lineEdit.text():
            user_input = self.lineEdit.text()
            user_input = user_input.strip()
            new_user_input = user_input.split(' ')
            print(new_user_input)
            self.textEdit.clear()

            my_lotto = []
            for num in new_user_input:
                num = num.strip()
                if num.isdigit() and (int(num) >= 1 and int(num) <= 45):
                    my_lotto.append(int(num))
                else:
                    print("입력값이 숫자가 아니거나 1에서 45 사이의 값이 아닙니다.")
                    self.textEdit.setText("입력값이 숫자가 아니거나 1에서 45 사이의 값이 아닙니다.")
                    return

            if len(my_lotto) != 6:
                print("입력값이 6개가 아닙니다.")
                self.textEdit.setText("입력값이 6개가 아닙니다.")
            else:
                find_same = 0
                for my_num in my_lotto:
                    if my_num in lotto_li:
                        find_same += 1

                print("당첨번호 =", lotto_li)
                self.textEdit.append("당첨번호 = " + str(lotto_li))
                print("내 번호 =", my_lotto)
                self.textEdit.append("맞춘 개수는 = " + str(find_same))

                if find_same == 0:
                    print("맞춘 번호가 없습니다.")
                elif find_same == 6:
                    print("1등 당첨!!")
                else:
                    print(str(find_same) + "개 맞추셨습니다.!")
        else:
            self.textEdit.setText("번호를 띄어쓰기로 6개 입력해주세요.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()
    sys.exit(app.exec_())
