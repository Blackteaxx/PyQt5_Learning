from PyQt5.Qt import *
from resource.ui.register import Ui_register_window


class Window(QWidget, Ui_register_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.retranslateUi(register_window)
        # self.register_menu_btn.clicked.connect(register_window.show_hide_menu)
        # self.register_about_btn.clicked.connect(register_window.show_about)
        # self.register_restart_btn.clicked.connect(register_window.restart)
        # self.register_exit_btn.clicked.connect(register_window.register_exit)
        # self.register_register_btn.clicked.connect(register_window.check_register)
        # QtCore.QMetaObject.connectSlotsByName(register_window)
    def show_hide_menu(self):


if __name__ == '__main__':
    # 0. 导入所需要的包和模块
    import sys

    # 1. 创建一个应用程序对象
    app = QApplication(sys.argv)

    # 2. 控件的操作
    # 2.1 创建控件
    window = Window()

    # 2.2 设置控件
    window.setWindowTitle('')
    window.resize(500, 500)

    # 2.3 展示控件
    window.show()

    # 3. 应用程序的执行，进入到消息循环
    sys.exit(app.exec_())
