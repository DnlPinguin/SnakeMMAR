import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg


class Snake(qw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_me()

    def init_me(self):
        self.setWindowTitle('Snake')
        self.setCentralWidget(Settings())
        self.show()


class Settings(qw.QWidget):

    player_name = 'default'
    speed_up_factor = 1
    int_speed = 1
    max_speed = 20
    step_speed = 1
    initial_snake_size = 2
    fruit_prob = 1
    fruit_life_prob_max = 1
    fruit_life_prob_min = 1
    game_board_zoom = 1
    game_board_size = [16, 16]
    border = False

    def __init__(self):
        super().__init__()
        self.init_me()

    def init_me(self):

        player_name = qw.QLineEdit()
        player_name.setMaxLength(16)
        self.player_name = player_name.text()

        speed_up_factor = qw.QLineEdit()
        speed_up_factor.setMaxLength(3)
        self.speed_up_factor = speed_up_factor.text()

        int_speed = qw.QLineEdit()
        int_speed.setMaxLength(3)
        self.int_speed = int_speed.text()

        max_speed = qw.QLineEdit()
        max_speed.setMaxLength(3)
        self.max_speed = max_speed.text()

        step_speed = qw.QLineEdit()
        step_speed.setMaxLength(3)
        self.step_speed = step_speed.text()

        initial_snake_size = qw.QLineEdit()
        initial_snake_size.setMaxLength(2)
        self.initial_snake_size = initial_snake_size.text()

        fruit_prob = qw.QLineEdit()
        fruit_prob.setMaxLength(1)
        self.fruit_prob = fruit_prob.text()

        fruit_life_prob_max = qw.QLineEdit()
        self.fruit_life_prob_max = fruit_life_prob_max.text()

        fruit_life_prob_min = qw.QLineEdit()
        self.fruit_life_prob_min = fruit_life_prob_min.text()

        game_board_zoom = qw.QLineEdit()
        self.game_board_zoom = game_board_zoom.text()

        game_board_size = qw.QHBoxLayout()
        game_board_size_1 = qw.QLineEdit()
        game_board_size_2 = qw.QLineEdit()
        game_board_size.addWidget(game_board_size_1)
        game_board_size.addWidget(game_board_size_2)
        self.game_board_size[0] = game_board_size_1.text()
        self.game_board_size[1] = game_board_size_2.text()

        game_start_button = qw.QPushButton()
        game_start_button.setText('Spiel starten')
        game_start_button.clicked.connect(self.game_start_clicked)

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
        self.setWindowTitle('Settings')
        self.setWindowIcon(qg.QIcon('snake.png'))
        self.show()

    def game_start_clicked(self):
        print('game_start_clicked')
        snakegame = SnakeWindow(self)
        main_window.setCentralWidget(snakegame)


class SnakeWindow(qw.QWidget):
    settings = None

    def __init__(self, other):
        super().__init__()
        self.init_me()
        self.settings = other

    def init_me(self):
        self.setGeometry(700, 700, 500, 500)
        self.setWindowTitle('actual gameplay')
        self.setWindowIcon(qg.QIcon('snake.png'))
        self.show()


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    main_window = Snake()
    sys.exit(app.exec_())
