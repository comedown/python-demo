#!/usr/bin/python3
# -*- coding: utf-8 -*-

### 函数定义 ###
import math

def my_abs(x):
    if x >= 0:
        return x;
    else:
        return -x;

# pass 空函数
# 没有pass会报错
def my_pass():
    pass

# 多个返回值
# 返回的是一个tuple（数组）
# 可以用一个参数作为数组接受，可以用相同个数参数接受
def my_move(x, y, step, angle = 1):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny, 3

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax^2 + bx + c = 0 的两个解
def my_quadratic(a, b, c):
    x1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 / a
    x2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 / a
    return x1, x2

if __name__ == '__main__':
    my_pass()
    x = my_abs(-2);
    nx = my_move(100, 100, 60, math.pi / 6)
    print("x's abs is ", x);
    print(nx)

    y = my_quadratic(1, 2, -3)
    print(y)
