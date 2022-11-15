import sys
from PyQt5.Qt import *
import qdarkstyle
import pymssql


class Table(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 连接数据库
        with pymssql.connect(host='127.0.0.1', user='sa', password='ki20030523', database='SPJ',
                                  charset="cp936") as connect:
            cursor = connect.cursor()
            cursor.execute('select %s, %s, %s from %s;' % ('Sname', 'City', 'SNO', 'S'))
            select = cursor.fetchall()
        row = len(select)
        # 设置标题与初始大小
        self.setWindowTitle("QTableView的学习")
        self.resize(600, 300)
        # 设置数据层次结构
        self.model = QStandardItemModel(0, 0)
        # 设置四个字段
        titlelist =['Sname', 'City', 'Sno']
        self.model.setHorizontalHeaderLabels(titlelist)
        # 添加数据
        # self.model.appendRow([
        #     QStandardItem("row , column"),
        #     QStandardItem("row , column"),
        #     QStandardItem("row , column"),
        #     QStandardItem("row , column"),
        # ])
        for column in range(len(titlelist)):
            for index in range(row):
                item = QStandardItem(f'{select[index][column]}')
                self.model.setItem(index, column, item)

        # 实例化表格视图，设置模型为自定义模型
        self.tableView = QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.resize(600, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Table()
    window.show()
    sys.exit(app.exec_())
