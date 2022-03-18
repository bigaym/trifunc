"""
在这里简单处理从GUI文本框中读取的数据
"""


def read_from_gui():
    """

    :return:
        func:str      表示调用的函数
        value:float   用户输入的值
        flag:bool     输入的是角度（0）还是弧度（1）
    """
    func = ""
    value = 0.0
    flag = int(0)

    return func, value, flag
