from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/main_menu.ui', self)
        self.load_game_button.setStyleSheet("background-image : url(images/arch_color.jpg);")
        self.start_game_button.setStyleSheet("background-image : url(images/arch_color.jpg);")
        self.records_table_button.setStyleSheet("background-image : url(images/arch_color.jpg);")
        QMainWindow.setStyleSheet(self, "background-image : url(images/arch.jpg);")
        self.load_game_button.clicked.connect(self.load_game)
        self.start_game_button.clicked.connect(self.start_game)
        self.records_table_button.clicked.connect(self.record_table)

    def load_game(self):
        pass

    def start_game(self):
        pass

    def record_table(self):
        pass
