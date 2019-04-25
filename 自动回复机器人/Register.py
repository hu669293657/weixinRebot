from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import pymysql, hashlib, re



class hello_Dialog1(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setWindowIcon(QIcon('logo.png'))
        MainWindow.resize(750, 500)
        MainWindow.setFixedSize(750, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 60, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 160, 154, 12))
        self.label_2.setObjectName("label_2")
        self.usrname = QtWidgets.QLineEdit(self.centralwidget)
        self.usrname.setGeometry(QtCore.QRect(350, 160, 181, 20))
        self.usrname.setObjectName("usrname")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 210, 154, 12))
        self.label_3.setObjectName("label_3")
        self.passwd = QtWidgets.QLineEdit(self.centralwidget)
        self.passwd.setGeometry(QtCore.QRect(350, 210, 181, 20))
        self.passwd.setObjectName("passwd")
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        # 设置密码隐藏
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 260, 154, 12))
        self.label_4.setObjectName("label_4")
        self.repasswd = QtWidgets.QLineEdit(self.centralwidget)
        self.repasswd.setGeometry(QtCore.QRect(350, 260, 181, 20))
        self.repasswd.setObjectName("repasswd")
        self.repasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        # 设置密码隐藏
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(200, 320, 131, 41))
        self.back.setObjectName("back")
        self.sign_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_button.setGeometry(QtCore.QRect(430, 320, 131, 41))
        self.sign_up_button.setObjectName("sign_up_button")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.sign_up_button.clicked.connect(self.sign_up)
        # 为按钮绑定方法
        self.back.clicked.connect(MainWindow.close)
        # 关闭当前窗口

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def sign_up(self):
        regiser_user = self.usrname.text()
        regiser_passwd = self.passwd.text()
        regiser_repasswd = self.repasswd.text()
        passwd = hashlib.md5(regiser_passwd.encode(encoding='UTF-8')).hexdigest()

        if regiser_passwd and regiser_user and regiser_repasswd != '':
            # 判断输入是否为空
            if regiser_passwd == regiser_repasswd:
                # 判断两次输入的密码是否相同
                if re.match(r"^1[35678]\d{9}$", regiser_user):
                    # 判断电话号码是否合法
                    if re.match(r"^\w+$", regiser_passwd):
                        # 判断密码是否合法
                        db = pymysql.Connect(host="**", port=**, user="**", password="**",
                                             charset="utf8", db="**")
                        cursor = db.cursor()
                        try:

                            # 尝试和数据库建立连接
                            sql = "SELECT count(1) FROM login WHERE usrname = '{}' ".format(regiser_user)
                            cursor.execute(sql)
                            data = cursor.fetchone()
                            if data == (0,):
                                sql = "SELECT count(1) FROM login WHERE usrname = '' AND passwd = ''"
                                cursor.execute(sql)
                                data = cursor.fetchone()
                                if data != (0,):

                                    sql = "UPDATE login SET usrname='{}' ,passwd='{}' WHERE usrname ='' AND passwd = '' LIMIT 1".format(
                                        regiser_user, passwd)
                                    cursor.execute(sql)
                                    # 执行sql语句
                                    db.commit()
                                    # 因为用的是mysqldb操作数据库，所以执行完sql语句后需要commit提交到数据库执行
                                    QMessageBox.warning(self, "恭喜", "注册成功！", QMessageBox.Yes)
                                else:
                                    QMessageBox.warning(self, "警告", "申请账号已达上限，暂停注册", QMessageBox.Yes)
                                    # 判断是否有空余key，是的话注册账户和密码，分配一个key并退出注册界面，否的话弹出警告框
                            else:
                                QMessageBox.warning(self, "警告", "该手机号已被注册！", QMessageBox.Yes)
                                # 判断该手机号是否被注册
                        except:
                            db.rollback()
                            # 回滚
                            QMessageBox.warning(self, "警告", "数据库连接失败！", QMessageBox.Yes)
                        finally:
                            db.close()
                            # 无论是否成功都断开数据库连接

                    else:
                        QMessageBox.warning(self, "警告", "密码为由数字、26个英文字母或下划线组成！", QMessageBox.Yes)
                        # 判断密码是否合法
                else:
                    QMessageBox.warning(self, "警告", "请输入11位电话号码！", QMessageBox.Yes)
                    # 判断手机号是否合法
            else:
                QMessageBox.warning(self, "警告", "请确保两遍密码相同！", QMessageBox.Yes)
                # 检查两遍密码是否相同
        else:
            QMessageBox.warning(self, "警告", "请将信息补充完整！", QMessageBox.Yes)
            # 检查输入是否为空

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI智能回复机器人"))
        self.label.setText(_translate("MainWindow", "欢迎您注册AI智能回复机器人"))
        self.label_2.setText(_translate("MainWindow", "请输入您的电话号码"))
        self.label_3.setText(_translate("MainWindow", "请输入您的密码"))
        self.label_4.setText(_translate("MainWindow", "请再次输入您的密码"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.sign_up_button.setText(_translate("MainWindow", "注册"))
