"""
在这里简单处理从GUI文本框中读取的数据
"""


def input_detect(input: str):
    try:
        input = float(input)
    except:
        return -1
    else:
        return input

if __name__ == '__main__':
    print(input_detect("0.223"))
