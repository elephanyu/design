# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:17:02 2018

@author: mz
"""


class ICommand(object):
    def __init__(self, rhs):
        self.rcv = rhs

    def Excute(self):
        pass


class LeftCommand(ICommand):
    def Excute(self):
        self.rcv.AtackLeft()


class RightCommand(ICommand):
    def Excute(self):
        self.rcv.AtackRight()


# receiver
class Boxer(object):
    def AtackLeft(self):
        print("left Atack")

    def AtackRight(self):
        print("Right Atack")


        # Invoker


class Coach(object):
    def TunLeft(self, command):
        command.Excute()

    def TurnRight(self, command):
        command.Excute()


if "__main__" == __name__:
    rcv = Boxer()

    coach = Coach()
    coach.TunLeft(LeftCommand(rcv))

    coach.TunLeft(RightCommand(rcv))

'''
left Atack
Right Atack
'''