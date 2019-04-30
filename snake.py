import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

class Snake(qw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_me()

    def init_me(self):
        self.setWindowTitle('Snake')
        self.setCentralWidget(Settings())
        self.show()


class Settings(qw.QWidget):

    player_name_att = 'default'
    speed_up_factor_att = 1
    int_speed_att = 1
    max_speed_att = 20
    step_speed_att = 1
    initial_snake_size_att = 2
    fruit_prob_att = 1
    fruit_life_prob_max_att = 1
    fruit_life_prob_min_att = 1
    game_board_zoom_att = 1
    game_board_size_att = [16, 16]
    border_att = False

    def __init__(self):
        super().__init__()

        self.player_name = qw.QLineEdit(self.player_name_att)
        self.player_name.setMaxLength(16)

        self.speed_up_factor = qw.QLineEdit(str(self.speed_up_factor_att))
        self.speed_up_factor.setMaxLength(3)

        self.int_speed = qw.QLineEdit(str(self.int_speed_att))
        self.int_speed.setMaxLength(3)

        self.max_speed = qw.QLineEdit(str(self.max_speed_att))
        self.max_speed.setMaxLength(3)

        self.step_speed = qw.QLineEdit(str(self.step_speed_att))
        self.step_speed.setMaxLength(3)

        self.initial_snake_size = qw.QLineEdit(str(self.initial_snake_size_att))
        self.initial_snake_size.setMaxLength(2)

        self.fruit_prob = qw.QLineEdit(str(self.fruit_prob_att))
        self.fruit_prob.setMaxLength(1)
        self.fruit_life_prob_max = qw.QLineEdit(str(self.fruit_life_prob_max_att))
        self.fruit_life_prob_min = qw.QLineEdit(str(self.fruit_life_prob_min_att))

        self.game_board_zoom = qw.QLineEdit(str(self.game_board_zoom_att))

        self.game_board_size = qw.QHBoxLayout()
        self.game_board_size_1 = qw.QLineEdit(str(self.game_board_size_att[0]))
        self.game_board_size_2 = qw.QLineEdit(str(self.game_board_size_att[1]))
        self.game_board_size.addWidget(self.game_board_size_1)
        self.game_board_size.addWidget(self.game_board_size_2)

        game_start_button = qw.QPushButton()
        game_start_button.setText('Spiel starten')
        game_start_button.clicked.connect(self.game_start_clicked)

        high_score_list = qw.QPushButton()
        high_score_list.setText('Highscore-Liste')

        border = qw.QHBoxLayout()
        border.addWidget(qw.QCheckBox("on"))
        border.addWidget(qw.QCheckBox("off"))

        form = qw.QFormLayout()

        form.addRow(qw.QLabel("player_name"), self.player_name)
        form.addRow(qw.QLabel("border"), border)
        form.addRow(qw.QLabel("speedupfactor"), self.speed_up_factor)
        form.addRow(qw.QLabel("int_speed"), self.int_speed)
        form.addRow(qw.QLabel("max_speed"), self.max_speed)
        form.addRow(qw.QLabel("step_speed"), self.step_speed)
        form.addRow(qw.QLabel("initial_snake_size"), self.initial_snake_size)
        form.addRow(qw.QLabel("fruit_prob"), self.fruit_prob)
        form.addRow(qw.QLabel("fruit_life_prob_max"), self.fruit_life_prob_max)
        form.addRow(qw.QLabel("fruit_life_prob_min"), self.fruit_life_prob_min)
        form.addRow(qw.QLabel("Game Board Size"), self.game_board_size)
        form.addRow(qw.QLabel("Game Board Zoom"), self.game_board_zoom)
        form.addRow(game_start_button, high_score_list)
        self.setLayout(form)
        self.init_me()

    def init_me(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Settings')
        self.setWindowIcon(qg.QIcon('snake.png'))
        self.show()

    def game_start_clicked(self):

        self.player_name_att = self.player_name.text()
        self.speed_up_factor_att = int(self.speed_up_factor.text())
        self.int_speed_att = int(self.int_speed.text())
        self.max_speed_att = int(self.max_speed.text())
        self.step_speed_att = int(self.step_speed.text())
        self.initial_snake_size_att = int(self.initial_snake_size.text())
        self.fruit_prob_att = int(self.fruit_prob.text())
        self.fruit_life_prob_max_att = int(self.fruit_life_prob_max.text())
        self.fruit_life_prob_min_att = int(self.fruit_life_prob_min.text())
        self.game_board_zoom_att = int(self.game_board_zoom.text())
        self.game_board_size_att[0] = int(self.game_board_size_1.text())
        self.game_board_size_att[1] = int(self.game_board_size_2.text())

        print('game_start_clicked')
        print('game zoom ist: ', self.game_board_zoom_att)
        print('game att 0 ist: ', self.game_board_size_att[0])
        print('game att 1 ist. ', self.game_board_size_att[1])
        snakegame = SnakeWindow(self)
        main_window.setCentralWidget(snakegame)
        print(self.game_board_zoom_att)


class SnakeWindow(qw.QWidget):
    settings = None

    display = None

    def __init__(self, other):
        super().__init__()
        self.settings = other
        self.display = SnakeGameWindow(self.settings.game_board_size_att[0], self.settings.game_board_size_att[1],
                                       self.settings.game_board_zoom_att)
        self.init_me()

    def init_me(self):
        vbox = qw.QHBoxLayout()
        self.setLayout(vbox)
        vbox.addWidget(self.display)

        self.setGeometry(700, 700, 500, 500)
        self.setWindowTitle('actual gameplay')
        self.setWindowIcon(qg.QIcon('snake.png'))
        self.show()


class SnakeGameWindow(qw.QLabel):
    scale = None
    size_x = None
    size_y = None

    img = None
    pixmap = None
    scaledpixmap = None

    def __init__(self, size_x, size_y, scale):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.scale = scale
        self.img = qg.QImage(size_x, size_y, qg.QImage.Format_RGBA8888)
        self.img.fill(qc.Qt.red)
        self.update()

    def update(self):
        self.pixmap = qg.QPixmap.fromImage(self.img)
        self.scaledpixmap = self.pixmap.scaled(self.size_x * self.scale, self.size_y * self.scale)
        self.setPixmap(self.scaledpixmap)

    def set_pixel(self, x, y, color=qc.Qt.white):
        if (x >= self.size_x):
            print("Ups something went wrong with set_pixel in SnakeGameWindow")
            return
        if (y >= self.size_y):
            print("Ups something went wrong with set_pixel in SnakeGameWindow")
            return
        self.img.setPixelColor(x, y, color)


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    main_window = Snake()
    sys.exit(app.exec_())
