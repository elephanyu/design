# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:56:43 2018

@author: mz
"""


class Facade(object):
    def TradeWar(self):
        a = ASubject()
        b = BSubject()
        c = CSubject()

        a.Start()
        b.Start()
        c.Start()


class ASubject(object):
    def Start(self):
        print("A start trade war")


class BSubject(object):
    def Start(self):
        print("B start trade war")


class CSubject(object):
    def Start(self):
        print("C start trade war")


if "__main__" == __name__:
    facade = Facade()
    facade.TradeWar()


'''
A start trade war
B start trade war
C start trade war
'''