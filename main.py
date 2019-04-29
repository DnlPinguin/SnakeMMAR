import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Window(QtWidgets):

    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    w.setWindowTitle("PyQt2")
    w.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    Window()