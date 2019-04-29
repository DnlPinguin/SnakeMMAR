import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg


class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.init_me()

    def init_me(self):

        player_name = qw.QLineEdit()
        speed_up_factor = qw.QLineEdit()
        int_speed = qw.QLineEdit()
        max_speed = qw.QLineEdit()
        step_speed = qw.QLineEdit()
        initial_snake_size = qw.QLineEdit()
        fruit_prob = qw.QLineEdit()
        fruit_life_prob_max = qw.QLineEdit()
        fruit_life_prob_min = qw.QLineEdit()
        game_board_zoom = qw.QLineEdit()

        game_board_size = qw.QHBoxLayout()
        game_board_size.addWidget(qw.QLineEdit())
        game_board_size.addWidget(qw.QLineEdit())

        game_start_button = qw.QPushButton()
        game_start_button.setText('Spiel starten')

        high_score_list = qw.QPushButton()
        high_score_list.setText('Highscore-Liste')

        border = qw.QHBoxLayout()
        border.addWidget(qw.QCheckBox("on"))
        border.addWidget(qw.QCheckBox("off"))

        form = qw.QFormLayout()

        form.addRow(qw.QLabel("player_name"), player_name)
        form.addRow(qw.QLabel("border"), border)
        form.addRow(qw.QLabel("speedupfactor"), speed_up_factor)
        form.addRow(qw.QLabel("int_speed"), int_speed)
        form.addRow(qw.QLabel("max_speed"), max_speed)
        form.addRow(qw.QLabel("step_speed"), step_speed)
        form.addRow(qw.QLabel("initial_snake_size"), initial_snake_size)
        form.addRow(qw.QLabel("fruit_prob"), fruit_prob)
        form.addRow(qw.QLabel("fruit_life_prob_max"), fruit_life_prob_max)
        form.addRow(qw.QLabel("fruit_life_prob_min"), fruit_life_prob_min)
        form.addRow(qw.QLabel("Game Board Size"), game_board_size)
        form.addRow(qw.QLabel("Game Board Zoom"), game_board_zoom)
        form.addRow(game_start_button, high_score_list)


        self.setLayout(form)
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Snake Game')
        self.setWindowIcon(qg.QIcon('snake.png'))
        self.show()

class SnakeWindow(qw.QWidget):
    pass

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
