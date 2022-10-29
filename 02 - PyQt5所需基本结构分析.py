# 0. 导入所需要的包和模块
from PyQt5.Qt import * # 包含了我们常用的一些类，汇总到了一块
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# # explanation 1.1
# # qApp全局变量，可以在文件中互通参数
# print(app.arguments())
# print(qApp.arguments())

# # explanation 1.2
# 我们的代码，有两种执行方式 1. 右击执行 2. 命令行 python 代码名称
# 从命令行获取相关参数,当别人通过命令行启动这个程序的时候
# 可以通过判定接收命令行参数的不同来执行不同的业务逻辑
# args = sys.argv
# print(args)

# 2. 控件的操作
# 创建控件，设置控件，事件、信号的处理
# 2.1 创建控件
# 当我们创建一个控件之后，若这个控件没有父控件，则把它当作顶层控件（窗口），系统会给窗口添加一些装饰（标题栏）
# 窗口控件具备一些特性（设置标题，图标）
window = QWidget()
# window = QPushButton()
# window = QLabel()

# 2.2 设置控件
window.setWindowTitle('Hello!!!')
# window.setText('hello world')


# 控件也可以作为一个容器（承载其他控件）
label = QLabel()
label.setText('XXX')
label.setWindowTitle("xxxxxxx")
label.show()


# 2.3 展示控件
# 刚创建好一个控件之后（这个控件没有什么父控件），默认情况下不会被展示，调用show
window.show()


# 3. 应用程序的执行，进入到消息循环
# 让整个程序开始执行，并且进入到消息循环（无限循环）
# 监测整个程序所收到的交互信息，将错误退出代码传给sys.exit()并退出
sys.exit(app.exec_())

# #  explanation 3.1
# # 告知时因为什么原因退出(退出代码)
# sys.exit()
