import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from googletrans import Translator

# MyApp 클래스 정의
class MyApp(QWidget):

    # 생성자 메서드
    def __init__(self):
        super().__init__()
        # 라벨과 입력 필드, 텍스트 에디터, 버튼 생성
        self.kor = QLabel('번역할 한국어 문장 입력: ', self)
        self.eng = QLabel('영어로 번역된 문장: ', self)
        self.le = QLineEdit(self)
        self.te = QTextEdit(self)
        self.trans_btn = QPushButton('영어로 번역하기', self)

        # 구글 번역기 객체 생성
        self.translator = Translator()
        
        # UI 초기화 메서드 호출
        self.UI()

    # UI 초기화 메서드
    def UI(self):
        # 수직 박스 레이아웃 생성
        box = QVBoxLayout()
        # 위젯들을 수직 박스 레이아웃에 추가
        box.addWidget(self.kor)

        #입력 칸의 높이를 100으로 설정하기
        self.le.setFixedHeight(60)

        # 입력시 위치를 왼쪽 상단으로 이동
   
        box.addWidget(self.le)
        box.addWidget(self.eng)
        box.addWidget(self.te)
        box.addWidget(self.trans_btn)
        self.setLayout(box)

        # 번역 버튼 클릭 시 translate_kor 메서드 호출
        self.trans_btn.clicked.connect(self.translate_kor)
        # 입력 필드 편집 완료 시 translate_kor 메서드 호출
        self.le.editingFinished.connect(self.translate_kor)

        # 윈도우 타이틀과 크기 설정 및 표시
        self.setWindowTitle("구글 번역기 API")
        self.setGeometry(500, 500, 700, 600)
        self.show()

    # 한국어를 영어로 번역하는 메서드
    def translate_kor(self):
        # 입력 필드에서 한국어 텍스트 가져오기
        kor_text = self.le.text()
        # 구글 번역기 API를 사용하여 한국어를 영어로 번역
        text_en = self.translator.translate(kor_text).text
        # 번역된 텍스트를 텍스트 에디터에 설정
        self.te.setText(text_en)


if __name__ == '__main__':
    # PyQt5 애플리케이션 생성
    app = QApplication(sys.argv)
    # MyApp 클래스 인스턴스 생성
    e = MyApp()
    # 애플리케이션 실행
    sys.exit(app.exec_())
