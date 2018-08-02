# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:30:45 2018

@author: mz
"""


class Component(object):
    def __init__(self, name):
        self.name = name
        self.child = []

    def add(self, name):
        pass

    def display(self):
        pass

    def remove(self, name):
        pass


class Composite(Component):
    def add(self, name):
        self.child.append(name)

    def display(self):
        print("component : %s" % (self.name))
        for n in self.child:
            n.display()
            # print("composite name : %s " %(n.name))

    def remove(self, name):
        self.child.remove(name)


class Leaf(Component):
    def add(self, name):
        self.child.append(name)

    def display(self):
        print("component : %s" % (self.name))
        for l in self.child:
            l.display()
            # print("leaf name : %s" %(l.name))

    def remove(self, name):
        self.child.remove(name)


if "__main__" == __name__:
    component = Composite("root")

    a = Composite("A node")
    b = Composite("B node")

    lf_a = Leaf("leaf A")
    lf_b = Leaf("leaf B")

    a.add(lf_a)
    b.add(lf_b)

    component.add(a)
    component.add(b)

    component.display()

'''
component : root
component : A node
component : leaf A
component : B node
component : leaf B
'''