# 0. 导入所需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()


class Btn(QAbstractButton):
    def paintEvent(self, evt):
        print('绘制按钮')
        # 创建一个画家
        painter = QPainter(self)
        # 创建一个笔
        pen = QPen(QColor(111, 100, 50), 6)
        painter.setPen(pen)
        # 画家画
        painter.drawText(20, 20, "1111")
        painter.drawEllipse(0, 0, 100, 100)


btn = Btn(window)
btn.setText("xxxx")
btn.resize(100, 100)

btn.pressed.connect(lambda: print('you know'))
# 2.2 设置控件
window.setWindowTitle('')
window.resize(500, 500)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
