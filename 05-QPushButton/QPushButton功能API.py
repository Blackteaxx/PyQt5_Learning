# 0. 导入所需要的包和模块
from PyQt5.Qt import *
import sys
import qdarkstyle

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)
# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle('按钮的功能')
window.resize(500, 500)

btn = QPushButton(window)
btn.resize(100, 100)
btn.setText('XXX')
icon = QIcon()  # 文件路径
btn.setIcon(icon)

# ************菜单的设置*******************start
menu = QMenu()

# 子菜单，最近打开
submenu = QMenu()
submenu.setTitle("最近打开")
# 行为动作：新建，打开，分割线，退出
new_action = QAction()
new_action.setText('新建')
new_action.setIcon(icon)
new_action.triggered.connect(lambda: print('triggered'))

open_action = QAction()
open_action.setText('打开')
open_action.setIcon(icon)
open_action.triggered.connect(lambda: print('triggered'))

exit_action = QAction()
exit_action.setText('退出')
exit_action.setIcon(icon)
exit_action.triggered.connect(lambda: print('triggered'))

file_action = QAction("OK")

submenu.addAction(file_action)

menu.addAction(new_action)
menu.addAction(open_action)
menu.addMenu(submenu)
menu.addSeparator()
menu.addAction(exit_action)

btn.setMenu(menu)
# ************菜单的设置*******************end
# 2.3 展示控件
window.show()
btn.showMenu()
# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
