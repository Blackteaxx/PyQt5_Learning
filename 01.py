from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

# 窗口控件
window = QWidget()
window.setWindowTitle('Hello')
window.resize(500, 500)
window.move(400, 200)

# 标签控件
label = QLabel(window)
label.setText("hello world")
label.move(200, 200)

window.show()
sys.exit(app.exec_())
