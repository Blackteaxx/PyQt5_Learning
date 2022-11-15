# 0. 导入所需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle('按钮的功能测试')
window.resize(500, 500)

btn = QPushButton(window)
# ************文本操作*******************start
# text = 1
# btn.setText(str(text))
#
#
# def slot():
#     text = int(btn.text())
#     text += 1
#     btn.setText(str(text))
#
#
# btn.clicked.connect(slot)
# ************文本操作*******************end

# ************图标操作*******************start
icon = QIcon()
btn.setIcon(icon)

size = QSize()
btn.setIconSize(size)
# ************图标操作*******************end


# ************快捷键设定*******************start
btn.pressed.connect(lambda: print("pressed"))
# btn.setText('&abc')
btn.setShortcut('Ctrl+A')
# ************快捷键设定*******************end
# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
