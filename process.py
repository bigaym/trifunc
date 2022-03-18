"""
在这里处理input模块传过来的数据
"""


def taylor_sin(x: float, order: int):
    """
    使用泰勒公式近似 sinx
    :param x: x
    :param order:阶数，越高越准但越慢
    :return: 结果
    """

    # 输入错误处理
    if x > 2147483647 or x < -2147483648:
        # 超出处理范围
        print("输入数据超出范围")    # TODO 在GUI中显示，并请求重新输入
        return -2
    elif order <= 2:
        print("精度过低")          # TODO 在GUI中显示，并请求重新输入
        return -3
    elif order > 99999:
        print("要求精度过高")       # TODO 在GUI中显示，并请求重新输入
        return -4
    e = x
    s = x
    for i in range(2, order):
        e = -1*e*x*x/((2*i-1)*(2*i-2))
        s += e
    return s


def taylor_cos(x: float, order: int):
    """
    使用泰勒公式近似 cosx
    :param x: x
    :param order:阶数，越高越准但越慢
    :return: 结果
    """

    # 输入错误处理
    if x > 2147483647 or x < -2147483648:
        # 超出处理范围
        print("输入数据超出范围")    # TODO 在GUI中显示，并请求重新输入
        return -2
    elif order <= 2:
        print("精度过低")          # TODO 在GUI中显示，并请求重新输入
        return -3
    elif order > 99999:
        print("要求精度过高")       # TODO 在GUI中显示，并请求重新输入
        return -4
    e = 1
    s = 1
    for i in range(1, order):
        e = -1*e*x*x/((2*i-1)*(2*i))
        s += e
    return s


if __name__ == '__main__':
    import math
    x = 3.14
    print(taylor_cos(x, 200))
    print(math.cos(x))
