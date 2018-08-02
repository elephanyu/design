# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 18:50:47 2018

@author: mz
"""


# observer
class Boss(object):
    def __init__(self):
        self.obj = [];

    def Attach(self, employee):
        self.obj.append(employee)

    def In(self):
        print("Boss in->")
        self.Notify(0);

    def Out(self):
        print("Boss out->")
        self.Notify(1);

    def Notify(self, tag):
        if 0 == tag:
            for o in self.obj:
                o.Work()
        else:
            for o in self.obj:
                o.Relax()


# subject
class Employee(object):
    def Work(self):
        pass

    def Relax(self):
        pass


class Manager(Employee):
    def Work(self):
        print("Manger: open PPT")

    def Relax(self):
        print("Manager: check stock")


class Engineer(Employee):
    def Work(self):
        print("Engineer: coding")

    def Relax(self):
        print("Engineer: chat")


if "__main__" == __name__:
    manager = Manager()
    employee = Engineer()

    boss = Boss()
    boss.Attach(manager)
    boss.Attach(employee)

    boss.In()
    print("\r")

    boss.Out()



'''
Boss in->
Manger: open PPT
Engineer: coding
 
Boss out->
Manager: check stock
Engineer: chat
'''