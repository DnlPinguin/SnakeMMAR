from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
import sys


class SnakeGame(QMainWindow):
    def __init__(self):
        super(SnakeGame, self).__init__()


        #self.setCentralWidget(self.sboard)
        self.setWindowTitle('PyQt5 Snake game')
        self.resize(600, 400)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

        self.show()


def main():
    app = QApplication([])
    launch_game = SnakeGame()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()