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


# ************自动重复*******************start
btn.setAutoRepeat(True)
btn.setAutoRepeatDelay(2000)  # 毫秒为单位
btn.setAutoRepeatInterval(1000)  # 监测间隔
print(btn.autoRepeat())
print(btn.autoRepeatDelay())
print(btn.autoRepeatInterval())
# ************自动重复*******************end

# ************排他性设置*******************start
for i in range(3):
    btn = QPushButton(window)
    btn.setText(("btn" + str(i)))
    btn.move(50 * i, 50 * i)

    print(btn.autoExclusive())
    btn.setCheckable(True)
    btn.setAutoExclusive(True)

btn = QPushButton(window)
btn.setText("btn3")
btn.setCheckable(True)
btn.move(150, 150)
# ************排他性设置*******************end


# ************按钮模拟点击*******************start
btn.click()
btn.animateClick(2000)  # 延迟松开
# ************按钮模拟点击*******************end

# ************可用信号*******************start
# btn.pressed()
# btn.released()
btn.clicked.connect(lambda value: print(value))  # 会发射一个值给外界,值为是否被选中
btn.toggled.connect(lambda value: print("按钮选中状态发生了改变", value))
# ************可用信号*******************end
# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
