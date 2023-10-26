from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
import interface_ui, Save_window_ui
import sys
from gtts import gTTS
import os

class App(QWidget, interface_ui.Ui_window):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.app_working()
        
    def app_working(self):
        self.enter_button.clicked.connect(self.on_click)
        self.show()
    
    def check_language(self):
        if self.German_tick.isChecked() == True:
            language="de"
        elif self.Turkish_tick.isChecked() == True:
            language="tr"
        elif self.Polish_tick.isChecked() == True:
            language="pl"
        elif self.Spanish_tick.isChecked() == True:
            language="es"
        elif self.English_tick.isChecked() == True:
            language="en"
        return language
        
    def check_textbox(self):
        textboxValue = self.text_box.text()
        return textboxValue
    
    def check_if_open(self):
        fileopenState = self.open_file_tick.isChecked()
        return fileopenState
    
    def save_to_file(self,speak):
        speak.save("TextToSpeech.mp3")
        
        
    def open_file(self,speak):
        os.system("start TextToSpeech.mp3")
    
    def TTS_convert(self, language, texttospeech):
        speak = gTTS(text=texttospeech,lang=language,slow=False)
        return speak
    
    def on_click(self):
        language = self.check_language()
        textboxValue = self.check_textbox()
        fileopenState = self.check_if_open()
        speak = self.TTS_convert(language, textboxValue)
        self.save_to_file(speak)
        if fileopenState == True:
            self.open_file(speak)
        QMessageBox.question(self, 'Conversion succeded', "Your text: " + textboxValue + " has been converted", QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")
    
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = App()
    okno.show()
    #app.exec_()
    sys.exit(app.exec_())