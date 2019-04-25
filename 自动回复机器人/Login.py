import psutil
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
import Main,re,pymysql,hashlib,sys,Login_UI,Register


class MainCode(QMainWindow, Login_UI.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Login_UI.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # 初始化界面
        self.pushButton.clicked.connect(self.registry)
        # self.login_button.clicked.connect(MainWindow.close)
        self.login_button.clicked.connect(self.login)
        # 给按钮绑定功能

    def registry(self):
        md.hide()  # 如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序

        form1 = QtWidgets.QDialog()
        uii = Register.hello_Dialog1()
        uii.setupUi(form1)
        form1.show()
        form1.exec_()
        md.show()

        # 实现窗口的切换,关闭子窗口之后会显示主窗口

    def login(self):
        login_user = self.lineEdit.text()

        login_password = self.lineEdit_2.text()

        if login_password and login_user != '':
            # 判断输入是否为空
            if re.match(r"^1[35678]\d{9}$", login_user):
                # 判断电话号码是否合法
                if re.match(r"^\w+$", login_password):
                    # 判断密码是否合法
                    passwd = hashlib.md5(login_password.encode(encoding='UTF-8')).hexdigest()
                    db = pymysql.Connect(host="224f749b10.iok.la", port=63306, user="root", password="123",
                                         charset="utf8", db="test")
                    cursor = db.cursor()
                    # 尝试和数据库建立连接
                    try:
                        sql = "SELECT count(1) FROM login WHERE usrname = '{}' and passwd = '{}'".format(login_user,
                                                                                                         passwd)
                        cursor.execute(sql)
                        data = cursor.fetchone()
                        # 判断是否查询到存在此账号密码

                        if data != (0,):
                            sql = "SELECT rebotkey FROM login_copy1 WHERE usrname = '17377430997' AND passwd = 'b4b147bc522828731f1a016bfa72c073'"
                            cursor.execute(sql)
                            for i in cursor.fetchone():
                                with open('key.txt', 'w') as f:
                                    f.write(i)
                                    # 将该用户的key保存下来
                            md.hide()
                            form2 = QtWidgets.QDialog()
                            ui_2 = Main.Ui_Dialog2()
                            ui_2.setupUi(form2)
                            form2.show()
                            form2.exec_()
                            md.show()
                            # 实现窗口的切换,关闭子窗口之后会显示主窗口
                        else:
                            QMessageBox.warning(self, "警告", "账户或密码错误！", QMessageBox.Yes)



                    except:
                        db.rollback()
                        # 回滚
                        QMessageBox.warning(self, "警告", "数据库连接失败！", QMessageBox.Yes)
                    finally:
                        db.close()
                        # 无论是否成功都断开数据库连接

                else:
                    QMessageBox.warning(self, "警告", "密码为由数字、26个英文字母或下划线组成！", QMessageBox.Yes)

            else:
                QMessageBox.warning(self, "警告", "请输入11位电话号码！", QMessageBox.Yes)

        else:
            QMessageBox.warning(self, "警告", "请将信息补充完整！", QMessageBox.Yes)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            psutil.Popen('taskkill /IM Login.exe /F', shell=True)

        else:
            event.ignore()
    # 重写关闭窗体的方法,通过杀死进程的方式避免程序关闭但是自动回复还在运行
    # 同时采用psutil.Popen的方法可以避免出现黑色窗体影响用户体验






if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())
# 显示窗体