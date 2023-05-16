import math
from functools import reduce

import pandas as pd
from pandas import array
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt


def count(n: array) -> float:

    pass


def cum(a: array) -> float:
    """
    累积收益算法：
    (x1 + 1) * (x2 + 1) .... (xn + 1) - 1
    :param a:
    :return:
    """
    r = reduce(lambda x, y: x * y, [i + 1 for i in a]) - 1
    return r


def kurt(a: array) -> float:
    """
    峰度: 描述数据分布陡峭或是平滑
    :param a:
    :return:
    """
    s = pd.Series(a)
    return s.kurt()


def skew(a: array) -> float:
    """
    偏度：用来描述数据分布的对称性
    :param a:
    :return:
    """
    s = pd.Series(a)
    return s.skew()


def linregress(a, b) -> (float, float):
    """
    回归分析
    :param a:
    :param b:
    :return:
    """
    x = np.array(a)
    y = np.array(b)
    x[np.isnan(x)] = 0
    y[np.isnan(y)] = 0
    X = sm.add_constant(x)
    fit = sm.OLS(y, X).fit()
    print(fit.summary())
    return fit.params


def g_avg_return_t(n: array) -> float:
    """
    时序几何平均分布
    :param n:
    :return:
    """
    return math.pow(reduce(lambda x, y: x * y, [i + 1 for i in n]), float(1/len(n))) - 1


def avg_t(n: array) -> float:
    """
    平均数据
    :param n:
    :return:
    """
    return np.mean(n)


def max(n: array) -> float:
    """
    序列中最大值
    :param n:
    :return:
    """
    return np.max(n)


def std(n: array) -> float:
    """
    标准差
    :param n:
    :return:
    """
    return np.std(n, ddof=1)



def maxdrawdown_t(n: array) -> float:
    """
    最大回撤率
    :return:
    """
    drawdowns = []
    for i in range(len(n)):
        if n[i] > 0:
            drawdowns.append(0)
            continue
        max_array = max(n[:i + 1])
        drawdown = (max_array - n[i]) / max_array
        drawdowns.append(drawdown)
    return max(drawdowns)



if __name__ == '__main__':
    print(kurt([0.1, 0.02, 0.003, -0.021, 0.001]))
    print(skew([0.1, 0.02, 0.003, -0.021, 0.001]))
    alpha, bet = linregress([1, 2, 3, 4, 5], [0, 2, 3, 4, 6])
    print(alpha, bet)

    x = np.arange(0, 2 * np.pi, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure(1)
    plt.plot(x, y1)
    plt.pause(2)  # 在figure(1)上绘制sin曲线，2s后自动关闭窗口

    plt.figure(2)
    plt.plot(x, y2)
    plt.pause(2)  # 在figure(2)上绘制cos曲线，2s后自动关闭窗口

    plt.pause(0)  # 重新绘制figure(1)和figure(2)，不会自动关闭
    print(2)
