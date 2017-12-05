#-*- coding: utf-8 -*-

from numpy import *
from random import *
import matplotlib.pyplot as plt

'''
最小二乘法（又称最小平方法）:
    通过最小化误差的平方和寻找数据的最佳函数匹配。
    利用最小二乘法可以简便地求得未知的数据，并使得这些求得的数据与实际数据之间误差的平方和为最小。
    最小二乘法还可用于曲线拟合。其他一些优化问题也可通过最小化能量或最大化熵用最小二乘法来表达。
    
matplotlib： python 的2D 绘图库
'''




class LeastSquares:
    def __init__(self):
        pass

    '''
    一元线性回归
    x**y : x 的 y 次方
    sum(list) 表示 list 中算素相加的和
    // 表示整数除法
    / 表示浮点数除法
    '''
    def OneLeastSquares(self):
        x = [1, 2, 3, 5, 6, 12, 11, 13]
        y = [4, 5, 8, 13, 12, 23, 20, 22]
        # 求平均数（list所有元素的和/元素的个数）
        average_x = float(sum(x)) // len(x)
        average_y = float(sum(y)) / len(y)
        # 求残差
        x_sub = list(map((lambda x: x - average_x), x))
        y_sub = list(map((lambda x: x - average_y), y))
        # 残差平方
        x_sub_pow2 = list(map((lambda x: x ** 2), x_sub))
        y_sub_pow2 = list(map((lambda x: x ** 2), y_sub))
        # 残差成积
        x_y = list(map((lambda x, y: x * y), x_sub, y_sub))

        # 获取 最小残差平方和
        min_sub_pow2 = minimum(sum(x_sub_pow2), sum(y_sub_pow2))

        # 残差成积和/x方向的残差平方和
        a = float(sum(x_y)) / min_sub_pow2
        b = average_y - a * average_x
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.plot(x, y, '*')
        plt.plot([0, 15], [0 * a + b, 15 * a + b])
        plt.grid()
        plt.show()


    def MoreLeastSquares(self):
        x, y, xr, yr = self.Data()
        X, Y = self.MAT(x, y, 9)
        XT = X.transpose()
        B = dot(dot(linalg.inv(dot(XT, X)), XT), Y)
        myY = dot(X, B)
        self.fig(x, myY, xr, yr)

    def Data(self):
        x = arange(-1, 1, 0.02)
        y = ((x * x - 1) ** 2 + 2) * (sin(x * 3) + 0.7 * cos(x * 1.2))
        xr = []
        yr = []
        i = 0
        for xx in x:
            yy = y[i]
            d = float(randint(80, 120)) / 100
            i += 1
            xr.append(xx * d)
            yr.append(yy * d)
        return x, y, xr, yr

    def MAT(self, x, y, order):
        X = []
        for i in range(order + 1):
            X.append(x ** i)
        X = mat(X).T
        Y = array(y).reshape((len(y), 1))
        return X, Y

    def fig(self, x1, y1, x2, y2):
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.plot(x1, y1, color='g', linestyle='-', marker='')
        plt.plot(x2, y2, color='m', linestyle='', marker='.')
        plt.grid()
        plt.show()

LeastSquares().OneLeastSquares()
LeastSquares().MoreLeastSquares()