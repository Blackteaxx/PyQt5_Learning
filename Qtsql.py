import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableView


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.db = None
        self.db_connect()
        self.displayData()

    def db_connect(self):
        # 1.设置数据库驱动（MSSQL为QODBC）
        self.db = QSqlDatabase.addDatabase('QODBC')
        self.db.setHostName('LAPTOP-77HHQ6NR')
        self.db.setDatabaseName('DRIVER=SQL Server;SERVER=LAPTOP-77HHQ6NR;DATABASE=dbo.SPJ')

        if self.db.open():  # 3
            QMessageBox.about(self, 'Database Connection', 'Success')

    def closeEvent(self, QCloseEvent):  # 4
        self.db.close()

    def displayData(self):
        sqlstr = 'select * from SPJ'

        qry = QSqlQuery(self.db)
        qry.prepare(sqlstr)
        qry.exec_()

        while qry.next():
            a = qry.value(0)
            b = qry.value(1)
            c = qry.value(2)
            print(a, b, c)
        # self.model = QSqlQueryModel(self)
        # self.model.setQuery(qry)
        #
        # self.view = QTableView(self)
        # self.view.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
