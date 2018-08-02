# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:03:28 2018

@author: mz
"""


class Factory(object):
    def Manufacture(self):
        print("Base products")


class ConcreteFactoryA(Factory):
    def Manufacture(self):
        print("A products")


class ConcreteFactoryB(Factory):
    def Manufacture(self):
        print("B products")


class FatoryManager(object):
    def CreateFactory(self, name):
        if "A" == name:
            return ConcreteFactoryA()
        elif "B" == name:
            return ConcreteFactoryB()


if __name__ == "__main__":
    factoryMana = FatoryManager()

    factory = factoryMana.CreateFactory("A")
    factory.Manufacture()

    factory = factoryMana.CreateFactory("B")
    factory.Manufacture()

'''
A products
B products
'''

