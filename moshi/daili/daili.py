# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:17:20 2018

@author: mz
"""


class Person(object):
    def ShowLove(self):
        pass


class Girl(Person):
    def ShowLove(self):
        pass


class Man(Person):
    def ShowLove(self):
        print("Send a beautiful flower")


class Proxy(Person):
    def ShowLove(self, p):
        p.ShowLove()


if "__main__" == __name__:
    p = Proxy()
    p.ShowLove(Man())

'''
Send a beautiful flower
'''