from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        # 调用父类的初始化方法
        super().__init__()
        self.setWindowTitle('QObject的学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject_test()
        # self.QObject_Opeartion_On_NameandAttr()
        # self.QObject_Operation_On_ParentandChild()
        # self.QWidget_ParentandChild()
        # self.QObject_Signal()
        # self.QObject_Type_Judge()
        self.QObject_Delete_Object()
        pass

    def QObject_test(self):
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def QObject_Opeartion_On_NameandAttr(self):
        # **************测试API*****************

        # obj = QObject()
        # obj.setObjectName('notice')
        # print(obj.objectName())
        #
        # obj.setProperty('notice_level', 'error')
        # obj.setProperty('notice_level2', 'warning')
        # print(obj.property('notice_level'))
        # print(obj.dynamicPropertyNames())

        # *************测试API******************

        # *************案例演示******************
        with open('QObject.qss', 'r') as fp:
            qApp.setStyleSheet(fp.read())

        label = QLabel(self)
        label.setObjectName('notice')
        label.setProperty('notice_level', 'normal')
        label.setText('Hello World')

        label2 = QLabel(self)
        label2.setObjectName('notice')
        label2.setText('Hello World!!!!')
        label2.move(100, 100)

        label3 = QLabel(self)
        label3.setText('xxx')
        label3.move(300, 300)

        btn = QPushButton(self)
        btn.setText('111')
        btn.move(200, 200)
        # label.setStyleSheet('font-size: 20px; color: red;')
        # *************案例演示******************

    def QObject_Operation_On_ParentandChild(self):
        # ************测试API*******************start

        # obj1 = QObject()
        # obj2 = QObject()
        # obj1.setObjectName("notice1")
        #
        # print("obj1", obj1)
        # print("obj2", obj2)
        #
        # obj1.setParent(obj2)
        # print(obj1.parent())
        # print(obj2.children())
        # print(obj2.findChild(QObject, 'notice', Qt.FindDirectChildrenOnly))

        # ************测试API*******************end

        # ************内存管理机制*******************start

        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()

        obj2.setParent(obj1)

        # 监听obj2被释放
        obj2.destroyed.connect(lambda: print('obj2对象被释放了'))

        del self.obj1

        # ************内存管理机制*******************end

    def QWidget_ParentandChild(self):
        # ************案例1*******************start

        window1 = QWidget()
        window1.setStyleSheet("background:red;")
        window1.resize(500, 500)
        window1.setWindowTitle('111')
        # window1.show()

        window2 = QWidget()
        window2.setStyleSheet("background:green;")
        window2.resize(100, 500)
        window2.setWindowTitle('222')
        # window2.setParent(window1)

        window2.show()
        # ************案例1*******************end

        # ************案例2*******************start

        # win_root = QWidget()
        #
        # label1 = QLabel()
        # label1.setParent(win_root)
        # label1.setText('label1')
        #
        # label2 = QLabel()
        # label2.move(50, 50)
        # label2.setParent(win_root)
        # label2.setText('label2')
        #
        # label3 = QLabel()
        # label3.move(80, 80)
        # label3.setParent(win_root)
        # label3.setText('label2')
        #
        # btn = 05-QPushButton(win_root)
        # btn.setText('button')
        # btn.move(100, 100)
        #
        # win_root.show()
        #
        # for sub_widget in win_root.findChildren(QLabel):

        #     sub_widget.setStyleSheet('background-color:cyan;')
        # ************案例2*******************end

    def QObject_Signal(self):
        # ************API练习*******************start

        # self.obj = QObject()
        # # obj.destroyed
        # # obj.objectNameChanged
        #
        # self.obj.destroyed.connect(lambda obj: print('对象被释放了', obj))
        #
        # self.obj.objectNameChanged.connect(lambda name: print(f'name is changed to {name}'))
        # self.obj.objectNameChanged.connect(lambda name: print(f'name is changed'))
        #
        # print(self.obj.receivers(self.obj.objectNameChanged))
        # self.obj.setObjectName('xxx')
        #
        # # self.obj.objectNameChanged.disconnect()
        # # 临时取消信号连接
        # print(self.obj.signalsBlocked())
        # self.obj.blockSignals(True)
        # print(self.obj.signalsBlocked())
        # self.obj.setObjectName('ooo')
        #
        # # self.obj.objectNameChanged.connect(lambda name: print(f'name is changed to {name}'))
        # # 恢复信号连接
        # self.obj.blockSignals(False)
        # print(self.obj.signalsBlocked())
        # self.obj.setObjectName('11oo')

        # ************API练习*******************end

        # ************案例1*******************start
        # btn = 05-QPushButton(self)
        # btn.setText('click me')
        #
        # btn.clicked.connect(lambda: print("点我？"))
        # ************案例1*******************end

        # ************案例2*******************start
        windown = QWidget()

        # 连接窜口标题变化的信号与槽
        def cao(title):
            windown.blockSignals(True)
            windown.setWindowTitle('BT-' + title)
            windown.blockSignals(False)
            print('窗口标题变化成了', 'BT-' + title)

        windown.windowTitleChanged.connect(cao)
        windown.setWindowTitle('Hello')
        windown.setWindowTitle('Hello 2')
        windown.setWindowTitle('Hello 3')
        windown.show()
        # ************案例2*******************end

    def QObject_Type_Judge(self):
        # ************API*******************start
        # obj = QObject()
        # w = QWidget()
        # btn = 05-QPushButton()
        # label = QLabel()
        #
        # objs = [obj, w, btn, label]
        # for o in objs:
        #     # print(o.isWidgetType())
        #     # print(o.inherits('QWidget'))
        #     print(o.inherits('05-QPushButton'))
        # ************API*******************end

        # ************案例*******************start
        label = QLabel(self)
        label.setText('11111')
        label.move(100, 100)
        label2 = QLabel(self)
        label2.setText('2222')
        label2.move(150, 150)

        btn = QPushButton(self)
        btn.setText('点我')

        # for widget in self.findChildren(QLabel):
        #     print(widget)
        for widget in self.children():
            if widget.inherits('QLabel'):
                widget.setStyleSheet("background:cyan;")
        # ************案例*******************end

    def QObject_Delete_Object(self):
        self.obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()

        obj2.setParent(self.obj1)
        obj3.setParent(obj2)

        self.obj1.destroyed.connect(lambda: print("被释放了"))
        obj2.destroyed.connect(lambda: print("被释放了"))
        obj3.destroyed.connect(lambda: print("被释放了"))

        # 由于被引用，没有任何效果
        # del obj2

        # 稍后删除（在下一个循环）
        obj2.deleteLater()
        print(self.obj1.children())
        # obj3.deleteLater()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())
