import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import GUI
import process

def convert(ui):             #计算函数（替换）
    input = ui.input.text()
    result = float(input) * 2
    ui.output.setText(str(result))

def convert1(ui):               #计算函数1（替换）
    input = ui.input.text()
    result = float(input) * 3
    ui.output.setText(str(result))

def mode(ui):
    text = ui.mode_select.currentText()    #当前模式选项的字符串为text
    if text == "角度制":
       #进行相应的操作
       return
    if text == "弧度制":
       # 进行相应的操作
       return



def func():
    text=ui.func_select.currentText()    #当前函数选项的字符串为text
    if text == "sin":
        i.cal_Button.clicked.connect(partial(convert, ui))
        return
    if text == "cos":
        ui.cal_Button.clicked.connect(partial(convert1, ui))
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = GUI.Ui_HelloWorld()
    ui.setupUi(MainWindow)
    MainWindow.show()      #显示窗口

    ui.func_select.activated[str].connect(func)      #如果函数选项被点击，则调用func函数
    ui.mode_select.activated[str].connect(mode)      #如果模式选项被点击，则调用mode函数

    ui.cal_Button.clicked.connect(partial(convert, ui))   #如果按钮被点击，则调用convert函数

    sys.exit(app.exec_())

