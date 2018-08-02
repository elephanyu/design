# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:08:14 2018

@author: mz
"""


class Template(object):
    def Excute(self):
        self.ReadyRead()
        self.ReadyWrite()

    def ReadyRead(self):
        print("Template ready read")

    def ReadyWrite(self):
        print("Template ready write")


class ATemplate(Template):
    def Excute(self):
        self.ReadyRead()
        self.ReadyWrite()

    def ReadyRead(self):
        print("A ready read")

    def ReadyWrite(self):
        print("A ready write")


class BTemplate(Template):
    def Excute(self):
        self.ReadyRead()
        self.ReadyWrite()

    def ReadyRead(self):
        print("B ready read")

    def ReadyWrite(self):
        print("B ready write")


if "__main__" == __name__:
    a = ATemplate()
    a.Excute()
    print("\r")

    b = BTemplate()
    b.Excute()



'''
A ready read
A ready write
 
B ready read
B ready write
'''