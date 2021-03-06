from gui import App
from PyQt5 import QtWidgets
import sys
import config as log


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    window.connect(log.name_db)
    app.exec_()


if __name__ == '__main__':
    main()
