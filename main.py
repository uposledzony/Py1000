import sys
from PyQt5.QtWidgets import *
from mainwindow import *


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()