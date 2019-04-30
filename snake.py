import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc


class SignalProcesser (qc.QObject):
    key_up_event = qc.pyqtSignal()


class Snake(qw.QMainWindow):

    player_name_att = 'default'
    speed_up_factor_att = 1
    int_speed_att = 1
    max_speed_att = 20
    step_speed_att = 1
    initial_snake_size_att = 2
    fruit_prob_att = 1
    fruit_life_prob_max_att = 1
    fruit_life_prob_min_att = 1
    game_board_zoom_att = 100
    game_board_size_att = [16, 9]
    border_att = False
    snake_pos = [game_board_size_att[0] / 2]
    snake_direction = 4

    def __init__(self):
        super().__init__()
        self.init_me()

    def init_me(self):

        #self.signal = SignalProcesser()
        #self.signal.key_up_event.connect(self.keyPressEvent)
        self.setWindowTitle('Snake')
        self.setGeometry(10, 10, 1000, 1000)
        self.setCentralWidget(Settings(self))
        self.show()
        self.setMouseTracking(True)

    def keyPressEvent(self, e):
        if e.key() == qc.Qt.Key_Up:
            print('oben')
            self.snake_direction = 8
        if e.key() == qc.Qt.Key_Left:
            print('links')
            self.snake_direction = 4
        if e.key() == qc.Qt.Key_Right:
            print('rechts')
            self.snake_direction = 6
        if e.key() == qc.Qt.Key_Down:
            print('unten')
            self.snake_direction = 2
        if e.key() == qc.Qt.Key_Escape:
            self.setCentralWidget(Settings(self))


class Settings(qw.QWidget):

    settings_main = None

    def __init__(self, other):
        super().__init__()
        self.settings_main = other

        self.player_name = qw.QLineEdit(self.settings_main.player_name_att)
        self.player_name.setMaxLength(16)

        self.speed_up_factor = qw.QLineEdit(str(self.settings_main.speed_up_factor_att))
        self.speed_up_factor.setMaxLength(3)

        self.int_speed = qw.QLineEdit(str(self.settings_main.int_speed_att))
        self.int_speed.setMaxLength(3)

        self.max_speed = qw.QLineEdit(str(self.settings_main.max_speed_att))
        self.max_speed.setMaxLength(3)

        self.step_speed = qw.QLineEdit(str(self.settings_main.step_speed_att))
        self.step_speed.setMaxLength(3)

        self.initial_snake_size = qw.QLineEdit(str(self.settings_main.initial_snake_size_att))
        self.initial_snake_size.setMaxLength(2)

        self.fruit_prob = qw.QLineEdit(str(self.settings_main.fruit_prob_att))
        self.fruit_prob.setMaxLength(1)
        self.fruit_life_prob_max = qw.QLineEdit(str(self.settings_main.fruit_life_prob_max_att))
        self.fruit_life_prob_min = qw.QLineEdit(str(self.settings_main.fruit_life_prob_min_att))

        self.game_board_zoom = qw.QLineEdit(str(self.settings_main.game_board_zoom_att))

        self.game_board_size = qw.QHBoxLayout()
        self.game_board_size_1 = qw.QLineEdit(str(self.settings_main.game_board_size_att[0]))
        self.game_board_size_2 = qw.QLineEdit(str(self.settings_main.game_board_size_att[1]))
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
        self.setWindowTitle('Settings')
        self.setWindowIcon(qg.QIcon('snake.png'))
        self.show()

    def game_start_clicked(self):

        main_window.player_name_att = self.player_name.text()
        main_window.speed_up_factor_att = int(self.speed_up_factor.text())
        main_window.int_speed_att = int(self.int_speed.text())
        main_window.max_speed_att = int(self.max_speed.text())
        main_window.step_speed_att = int(self.step_speed.text())
        main_window.initial_snake_size_att = int(self.initial_snake_size.text())
        main_window.fruit_prob_att = int(self.fruit_prob.text())
        main_window.fruit_life_prob_max_att = int(self.fruit_life_prob_max.text())
        main_window.fruit_life_prob_min_att = int(self.fruit_life_prob_min.text())
        main_window.game_board_zoom_att = int(self.game_board_zoom.text())
        main_window.game_board_size_att[0] = int(self.game_board_size_1.text())
        main_window.game_board_size_att[1] = int(self.game_board_size_2.text())

        print('game_start_clicked')
        print('game zoom ist: ', main_window.game_board_zoom_att)
        print('game att 0 ist: ', main_window.game_board_size_att[0])
        print('game att 1 ist. ', main_window.game_board_size_att[1])
        snakegame = SnakeWindow(self)
        main_window.setCentralWidget(snakegame)
        print(main_window.game_board_zoom_att)


class SnakeWindow(qw.QWidget):
    settings = None
    display = None

    def __init__(self, other):
        super().__init__()
        self.settings = other
        self.display = SnakeGameWindow(main_window.game_board_size_att[0], main_window.game_board_size_att[1],
                                       main_window.game_board_zoom_att)
        self.init_me()

    def init_me(self):
        vbox = qw.QHBoxLayout()
        self.setLayout(vbox)
        vbox.addWidget(self.display)

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
        self.img.fill(qc.Qt.black)
        self.draw_rectangle(5, 5, qc.Qt.blue)

    def update(self):
        self.pixmap = qg.QPixmap.fromImage(self.img)
        self.scaledpixmap = self.pixmap.scaled(self.size_x * self.scale, self.size_y * self.scale)
        self.setPixmap(self.scaledpixmap)

    def draw_rectangle(self, x, y, color=qc.Qt.white):
        if x >= self.size_x:
            print("Ups something went wrong with set_pixel in SnakeGameWindow")
            return
        if y >= self.size_y:
            print("Ups something went wrong with set_pixel in SnakeGameWindow")
            return
        self.img.setPixelColor(x, y, color)
        self.update()




if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    main_window = Snake()
    sys.exit(app.exec_())
