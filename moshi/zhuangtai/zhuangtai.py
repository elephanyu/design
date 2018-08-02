# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:45:13 2018

@author: mz
"""


class Status(object):
    def Handle(self, rhs):
        pass


class AStatus(Status):
    def Handle(self, rhs):
        print("A status happens")
        if rhs is not None:
            b = BStatus()
            rhs.Handle(b)


class BStatus(Status):
    def Handle(self, rhs):
        print("B status happens")
        if rhs is not None:
            status = None
            rhs.Handle(status)


class StatusManager(object):
    def Handle(self, rhs):
        if rhs is not None:
            rhs.Handle(self)
        else:
            print("End")


if "__main__" == __name__:
    a = AStatus()
    statusManager = StatusManager()
    statusManager.Handle(a)

'''
A status happens
B status happens
End 
'''