import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from googletrans import Translator, LANGUAGES

class TranslatorApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("번역기")
        self.setGeometry(300, 300, 500, 400)

        # 입력받을 텍스트와 번역 결과를 위한 위젯들 생성
        self.text_input_label = QLabel("번역할 텍스트:", self)
        self.text_input = QTextEdit(self)
        self.detect_btn = QPushButton("언어 감지", self)
        self.translate_btn = QPushButton("번역", self)
        self.output_label = QLabel("번역 결과:", self)
        self.translated_text = QTextEdit(self)
        self.translator = Translator()

        # UI 초기화 함수 호출
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

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
        if input_text:
            detected_lang = self.translator.detect(input_text).lang
            self.show_message(f"감지된 언어: {LANGUAGES[detected_lang]}")

    def translate_text(self):
        # 입력된 텍스트 번역 함수
        input_text = self.text_input.toPlainText()
        if input_text:
            detected_lang = self.translator.detect(input_text).lang
            translated_text = input_text
            if detected_lang != 'en':
                translated_text = self.translator.translate(input_text, src=detected_lang, dest='en').text
            self.translated_text.setPlainText(translated_text)

    def show_message(self, message):
        # 메시지 박스를 이용해 감지된 언어를 알려주는 함수
        msg_box = QMessageBox(self)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())
