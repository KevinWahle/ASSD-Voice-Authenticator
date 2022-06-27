from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtGui import QIcon

from src.ui.windows.Speaker_recognition_Windows import Ui_MainWindow

class VoiceAuthToolApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.playIcon = [QIcon("res/play.png"), QIcon("res/pause.png")]
        
        