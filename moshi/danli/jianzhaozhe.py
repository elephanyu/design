# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:19:38 2018

@author: mz
"""


class Director(object):
    def Build(self, builder):
        builder.BuildFloor()
        builder.BuildWindow()


class Builder(object):
    def __init__(self, product):
        self._product = product

    def BuildWindow(self):
        pass

    def BuildFloor(self):
        pass


class Product(object):
    def BuildWindow(self, window):
        self._window = window

    def BuildFloor(self, floor):
        self._floor = floor

    def Show(self):
        print(self._window, self._floor)


class ABuilder(Builder):
    def BuildWindow(self):
        self._product.BuildWindow("A builds Blue window\r\n")

    def BuildFloor(self):
        self._product.BuildFloor("A builds white floor\r\n")


class BBuilder(Builder):
    def BuildWindow(self):
        self._product.BuildWindow("B builds transparent window\r\n")

    def BuildFloor(self):
        self._product.BuildFloor("B builds gray floor\r\n")


if "__main__" == __name__:
    director = Director()
    product = Product()

    print('---a builder---')
    a = ABuilder(product)
    a.BuildFloor()
    a.BuildWindow()

    product.Show()

    print('---b builder---')
    b = BBuilder(product)
    b.BuildFloor()
    b.BuildWindow()

    product.Show()

'''
---a builder---
A builds Blue window
 A builds white floor
 
---b builder---
B builds transparent window
 B builds gray floor
'''