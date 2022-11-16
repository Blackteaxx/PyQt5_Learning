from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        # 调用父类的初始化方法
        super().__init__()
        self.setWindowTitle('')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cb = QComboBox(self)
        # cb.addItem('忧郁')
        # cb.addItem('抖音')
        # cb.addItems(['忧郁', '抖音'])
        # cb.insertItem(0, '二次元')
        #
        # cb.setItemText(0, 'binary')
        #
        # cb.removeItem(0)
        cb.addItems(['123', '456'])
        btn = QPushButton(self)
        btn.setText("测试按钮")

        btn.clicked.connect(lambda: print(cb.count()))
        btn.clicked.connect(lambda: print(cb.currentIndex()))
        btn.clicked.connect(lambda: print(cb.currentText()))
        btn.clicked.connect(lambda: print(cb.currentData()))

        cb.move(100, 100)
        cb.resize(100, 30)

        # # 使用标准数据模型显示
        # model = QStandardItemModel()
        # item1 = QStandardItem("1")
        # item2 = QStandardItem("2")
        # item22 = QStandardItem("3")
        #
        # item2.appendRow(item22)
        # model.appendRow(item1)
        # model.appendRow(item2)
        #
        # cb.setModel(model)
        #
        # cb.setView(QTreeView(cb))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
