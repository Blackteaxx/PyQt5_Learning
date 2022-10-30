from login_Panel import LoginPanel
from register_Panel import RegisterPanel
from PyQt5.Qt import *
import qdarkstyle


def show_registerPanel():
    print('1')
    registerpanel.setVisible(True)
    loginpanel.setVisible(False)


def return_loginPanel():
    registerpanel.setVisible(False)
    loginpanel.setVisible(True)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    window = QWidget()
    loginpanel = LoginPanel(window)
    registerpanel = RegisterPanel(window)
    registerpanel.setVisible(False)

    loginpanel.show_registerPanel_signal.connect(show_registerPanel)
    registerpanel.exit_signal.connect(lambda: return_loginPanel())

    window.show()
    sys.exit(app.exec_())
