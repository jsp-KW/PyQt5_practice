import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from googletrans import Translator, LANGUAGES

# 구글 번역 api 를 이용한
class TranslatorApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("번역기") #ui에 쓸 이름
        self.setGeometry(300, 300, 500, 400)

        # 입력받을 텍스트와 번역 결과를 위한 위젯들 생성
        self.text_input_label = QLabel("번역할 텍스트:", self) # 입력창 위에 나타낼 곳 레이블링
        self.text_input = QTextEdit(self) # 입력창 생성
        self.detect_btn = QPushButton("언어 감지", self) # 언어감지 버튼 생성
        self.translate_btn = QPushButton("번역", self) # 번역 버튼 생성
        self.output_label = QLabel("번역 결과:", self) # 번역된 문장 나타낼 공간 위 레이블링
        self.translated_text = QTextEdit(self) # 번역된 문장 나타내주는 공간
        self.translator = Translator() # 번역기 실행

        # UI 초기화 함수 호출
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        # ui에 위젯들 추가
        layout.addWidget(self.text_input_label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.detect_btn)
        layout.addWidget(self.translate_btn)
        layout.addWidget(self.output_label)
        layout.addWidget(self.translated_text)

        self.setLayout(layout)

        # 감지 버튼과 번역 버튼에 기능 연결
        self.detect_btn.clicked.connect(self.detect_language)
        self.translate_btn.clicked.connect(self.translate_text)

    def detect_language(self):
        # 입력된 텍스트 언어 감지 함수
        input_text = self.text_input.toPlainText()
        if input_text: # 텍스트 입력된 경우
            detected_lang = self.translator.detect(input_text).lang # 구글 api 내장 함수 detect 함수를 이용하여 언어 감지후 변수에 저장
            self.show_message(f"감지된 언어: {LANGUAGES[detected_lang]}") # 감지된 언어의 결과를 창과 함께 출력

    def translate_text(self):
        # 입력된 텍스트 번역 함수
        input_text = self.text_input.toPlainText()
        if input_text:
            detected_lang = self.translator.detect(input_text).lang
            translated_text = input_text
            if detected_lang != 'en': # 언어가 영어인 경우가 아니라면
                translated_text = self.translator.translate(input_text, src=detected_lang, dest='en').text # 영어로 번역한다.
            self.translated_text.setPlainText(translated_text) # 번역한 문장을 저장

    def show_message(self, message): 
        # 메시지 박스를 이용해 감지된 언어를 알려주는 함수
        msg_box = QMessageBox(self) 
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator_app = TranslatorApp() #앱등록
    translator_app.show()# 실행
    sys.exit(app.exec_()) # 종료
