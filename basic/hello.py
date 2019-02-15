#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print('中文'.encode('gb2312'))
    print('Hello, %s' % 'world')
    x = input('x:')
    print(x)

    # list，下表从0开始，-1代表最后一个，-2代表倒数第二个...
    classmates = ['Michael', 'Bob', 'Tracy']
    print(classmates)
    print(classmates[0])
    print(len(classmates))
    # list是一个可变的有序表，所以，可以往list中追加元素到末尾：
    classmates.append('nancy')
    print(classmates[-1])
    # 在指定位置插入元素
    classmates.insert(1, 'Jack')
    print(classmates[1])

    # 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
    # 用()定义
    classmates = ('Michael', 'Bob', 'Tracy')
    # 只有一个元素
    t = (1) # 这样表示1
    print(t)
    # 加上逗号区分
    t = (1,) # 这样表示只有一个元素的元组
    print(t)
    # 利用list，可变
    t = ('a', 'b', ['A', 'B'])
    t[2][0] = 'a'
    t[2][1] = 'b'
    print(t)

    # dict 全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d)
    print(d['Michael'])
    print('Nancy' in d)

    # set 集合
    s = set([1, 2, 3])
    print(s)
    s = set([1, 1, 2, 2, 3, 3 ,4])
    print(s)
