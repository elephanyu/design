# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:48:29 2018

@author: mz
"""


class Strategy(object):
    def action(self):
        pass


class ConcreteStrategyA(Strategy):
    def action(self):
        print("A action")


class ConcreteStrategyB(Strategy):
    def action(self):
        print("B action")


class Context(object):
    def __init__(self, rhs):
        self.strategy = rhs

    def action(self):
        self.strategy.action()
        # print(self.strategy.action())  --输出: None


if "__main__" == __name__:
    context = Context(ConcreteStrategyA())
    context.action()


'''
A action
'''