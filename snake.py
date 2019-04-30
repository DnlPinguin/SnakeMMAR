import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc
import random


class Snake(qw.QMainWindow):

    player_name_att = 'default'

    int_speed_att = 200
    max_speed_att = 50
    step_speed_att = 0.9

    initial_snake_size_att = 1

    fruit_not_on_board = True
    fruit_pos = [1, 1]
    game_board_zoom_att = 50
    game_board_size_att = [16, 9]

    history = []

    snake_hungry = True
    snake_pos = [round(game_board_size_att[0]/2), round(game_board_size_att[1]/2)]
    snake_direction = 4
    snake_whole = [(snake_pos[0], snake_pos[1])]

    def __init__(self):
        super().__init__()
        self.init_me()

    def init_me(self):
        self.setWindowIcon(qg.QIcon('snake.png'))
        self.setWindowTitle('Snake')
        self.setCentralWidget(Settings(self))
        self.show()
        self.setMouseTracking(True)

    def keyPressEvent(self, e):
        if e.key() == qc.Qt.Key_Up:
            if self.snake_direction == 4 or self.snake_direction == 6:
                self.snake_direction = 8

        if e.key() == qc.Qt.Key_Left:
            if self.snake_direction == 8 or self.snake_direction == 2:
                self.snake_direction = 4

        if e.key() == qc.Qt.Key_Right:
            if self.snake_direction == 8 or self.snake_direction == 2:
                self.snake_direction = 6

        if e.key() == qc.Qt.Key_Down:
            if self.snake_direction == 4 or self.snake_direction == 6:
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

        self.int_speed = qw.QLineEdit(str(self.settings_main.int_speed_att))
        self.int_speed.setMaxLength(4)

        self.max_speed = qw.QLineEdit(str(self.settings_main.max_speed_att))
        self.max_speed.setMaxLength(4)

        self.step_speed = qw.QLineEdit(str(self.settings_main.step_speed_att))
        self.step_speed.setMaxLength(3)

        self.initial_snake_size = qw.QLineEdit(str(self.settings_main.initial_snake_size_att))
        self.initial_snake_size.setMaxLength(1)

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

        form = qw.QFormLayout()

        form.addRow(qw.QLabel("player_name"), self.player_name)
        form.addRow(qw.QLabel("int_speed"), self.int_speed)
        form.addRow(qw.QLabel("max_speed"), self.max_speed)
        form.addRow(qw.QLabel("step_speed"), self.step_speed)
        form.addRow(qw.QLabel("initial_snake_size"), self.initial_snake_size)
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
        main_window.int_speed_att = int(self.int_speed.text())
        main_window.max_speed_att = int(self.max_speed.text())
        main_window.step_speed_att = float(self.step_speed.text())
        main_window.initial_snake_size_att = int(self.initial_snake_size.text())
        main_window.game_board_zoom_att = int(self.game_board_zoom.text())
        main_window.game_board_size_att[0] = int(self.game_board_size_1.text())
        main_window.game_board_size_att[1] = int(self.game_board_size_2.text())

        print('game_start_clicked')
        print('game zoom ist: ', main_window.game_board_zoom_att)
        print('game att 0 ist: ', main_window.game_board_size_att[0])
        print('game att 1 ist. ', main_window.game_board_size_att[1])
        snake_game = SnakeWindow(self)
        main_window.setCentralWidget(snake_game)
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
        self.draw_rectangle(main_window.snake_pos[0], main_window.snake_pos[1], qc.Qt.green)
        self.move()
        self.timer = qc.QTimer()
        self.timer.setInterval(main_window.int_speed_att)
        self.timer.timeout.connect(self.game)
        self.timer.start(main_window.int_speed_att)
        self.create_snake()

    def update(self):
        self.pixmap = qg.QPixmap.fromImage(self.img)
        self.scaledpixmap = self.pixmap.scaled(self.size_x * self.scale, self.size_y * self.scale)
        self.setPixmap(self.scaledpixmap)

    @staticmethod
    def create_snake():
        while main_window.initial_snake_size_att > 1:
            main_window.snake_whole.append((main_window.game_board_size_att[0]/2+1,
                                            main_window.game_board_size_att[1]/2))
            main_window.initial_snake_size_att = main_window.initial_snake_size_att - 1

    def board_reset(self):
        self.img.fill(qc.Qt.black)

    def game(self):
        main_window.statusBar().showMessage(main_window.player_name_att +
                                            " Length : " +
                                            str(main_window.initial_snake_size_att))
        self.board_reset()
        if main_window.fruit_not_on_board:
            self.spawn_fruit()
        else:
            self.draw_fruit()
        self.move()
        self.draw_snake()

    def draw_snake(self):
        for body in main_window.snake_whole:
            self.draw_rectangle(body[0], body[1])

    @staticmethod
    def spawn_fruit():
        main_window.fruit_pos[0] = random.randint(1, main_window.game_board_size_att[0]-1)
        main_window.fruit_pos[1] = random.randint(1, main_window.game_board_size_att[1]-1)
        main_window.fruit_not_on_board = False

    @staticmethod
    def snake_collide_border(self):
        if main_window.snake_pos[0] < 0:
            main_window.snake_pos[0] = main_window.game_board_size_att[0]-1

        elif main_window.snake_pos[0] > main_window.game_board_size_att[0]-1:
            main_window.snake_pos[0] = 0

        elif main_window.snake_pos[1] < 0:
            main_window.snake_pos[1] = main_window.game_board_size_att[1]-1

        elif main_window.snake_pos[1] > main_window.game_board_size_att[1]-1:
            main_window.snake_pos[1] = 0

    def snake_collide_fruit(self):
        if main_window.snake_pos[0] == main_window.fruit_pos[0] and main_window.snake_pos[1] == main_window.fruit_pos[1]:
            main_window.snake_hungry = False
            main_window.fruit_not_on_board = True
            main_window.int_speed_att = main_window.int_speed_att*main_window.step_speed_att
            if main_window.int_speed_att < main_window.max_speed_att:
                main_window.int_speed_att = main_window.max_speed_att
            self.timer.setInterval(main_window.int_speed_att)
            main_window.initial_snake_size_att = main_window.initial_snake_size_att +1

    def snake_harakiri(self):
        print(' Snake length', len(main_window.snake_whole))
        for i in range(0, len(main_window.snake_whole)-1):
            print('for elenment', i)
            print('snake Head', main_window.snake_pos)
            print('snake whole', main_window.snake_whole[i])
            print('--------------------------------')
            if (main_window.snake_pos[0], main_window.snake_pos[1]) == main_window.snake_whole[i]:
                self.game_lost()
                print('game_lost')

    def game_lost(self):
        self.timer.stop()
        main_window.history.append((main_window.player_name_att, main_window.initial_snake_size_att))
        main_window.snake_pos = [round(main_window.game_board_size_att[0]/2), round(main_window.game_board_size_att[1]/2)]
        main_window.snake_whole = [(main_window.snake_pos[0], main_window.snake_pos[1])]
        main_window.int_speed_att = 200
        main_window.initial_snake_size_att = 1
        main_window.statusBar().showMessage('Game OVER: Press Escape to get back in the Menu')

    def draw_fruit(self):
        self.draw_rectangle(main_window.fruit_pos[0], main_window.fruit_pos[1], qc.Qt.red)

    def move(self):

        if main_window.snake_direction == 2:
            main_window.snake_pos[1] = main_window.snake_pos[1] + 1

        if main_window.snake_direction == 4:
            main_window.snake_pos[0] = main_window.snake_pos[0] - 1

        if main_window.snake_direction == 6:
            main_window.snake_pos[0] = main_window.snake_pos[0] + 1

        if main_window.snake_direction == 8:
            main_window.snake_pos[1] = main_window.snake_pos[1] - 1

        self.snake_harakiri()
        self.snake_collide_fruit()
        self.snake_collide_border(self)

        main_window.snake_whole.append((main_window.snake_pos[0], main_window.snake_pos[1]))

        if main_window.snake_hungry:
            main_window.snake_whole.pop(0)
        else:
            main_window.snake_hungry = True

    def draw_rectangle(self, x, y, color=qc.Qt.green):
        if x >= self.size_x:
            print("Ups something went wrong with x set_pixel in SnakeGameWindow")
            return
        if y >= self.size_y:
            print("Ups something went wrong with y set_pixel in SnakeGameWindow")
            return
        self.img.setPixelColor(x, y, color)
        self.update()


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    main_window = Snake()
    sys.exit(app.exec_())
