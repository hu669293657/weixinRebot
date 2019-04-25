import threading
import itchat,requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon




class MyThread(threading.Thread,):
    def __init__(self, log_ctrl):
        super().__init__()
        self.log_ctrl = log_ctrl
        self.singal = threading.Event()
        self.singal.set()
        # 初始化多线程

    def run(self):
        self.log_ctrl.setText("程序正在运行...")
        self.singal.wait() #相当于判断,若even为真则继续,若为假则等待或超时

        def get_response(msg):
            with open('key.txt', 'r') as f:
                key = f.read()
            apiUrl = 'http://www.tuling123.com/openapi/api'
            data = {
                'key': '{}'.format(key),  # Tuling Key
                'info': msg,  # 这是我们发出去的消息
                'userid': 'wechat-robot',  # 这里你想改什么都可以
            }
            # 我们通过如下命令发送一个post请求
            r = requests.post(apiUrl, data=data).json()
            return r.get('text')

        @itchat.msg_register(itchat.content.TEXT)
        def print_content(msg):
            return get_response(msg['Text'])
        # 开启好友聊天功能
        @itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
        def print_content(msg):
            return get_response(msg['Text'])
        # 开启群聊功能

        itchat.auto_login(hotReload=False)
        # 登录程序,在这里会弹出二维码,同时强制要求每次登录使用二维码登录
        itchat.run()
        # 运行程序

    def pause(self):
        itchat.logout()
        self.log_ctrl.setText("程序暂停...")
        self.singal.clear()




class Ui_Dialog2(object):
    def __init__(self):
        self.thread =None

    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(750, 500)
        Dialog2.setFixedSize(750,500)
        Dialog2.setWindowIcon(QIcon('logo.png'))
        self.pushButton = QtWidgets.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(100, 320, 151, 51))
        self.pushButton.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog2)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 320, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog2)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 320, 151, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(280, 210, 161, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 431, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        # 以上是UI界面设计

        self.pushButton.clicked.connect(Dialog2.close)
        # self.pushButton.clicked.connect(Dialog2.close)
        # 关闭当前窗口并返回登录界面
        self.pushButton_2.clicked.connect(self.stop)
        # 停止运行自动回复程序
        self.pushButton_3.clicked.connect(self.run)
        # 开始运行自动回复程序



        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)


    def run(self):
        self.thread = MyThread(self.label)
        self.thread.start()
        # 启动多线程
        self.pushButton_3.setEnabled(False)
        # 设置运行按钮不可用
        self.pushButton_2.setEnabled(True)
        # 设置停止按钮可用



    def stop(self):
        self.thread.pause()
        # 调用自定义的pause方法
        self.pushButton_2.setEnabled(False)
        # 设置停止按钮不可用
        self.pushButton_3.setEnabled(True)
        # 设置运行按钮可用






    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "AI智能回复机器人"))
        self.pushButton.setText(_translate("Dialog2", "注销"))
        self.pushButton_2.setText(_translate("Dialog2", "停止"))
        self.pushButton_3.setText(_translate("Dialog2", "运行"))
        self.label.setText(_translate("Dialog2", ""))
        self.label_2.setText(_translate("Dialog2", "欢迎使用AI智能回复机器人"))





