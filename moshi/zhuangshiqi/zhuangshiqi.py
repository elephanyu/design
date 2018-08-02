# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:37:17 2018

@author: mz
"""


class Warrior:
    def __init__(self):
        self.attrack = 100
        self.defend = 200

    def ShowAttributes(self):
        print("*self*")
        print("attrack : %d" % (self.attrack))
        print("attrack : %d \r\n" % (self.defend))


class OnCloth(Warrior):
    def __init__(self, rhs):
        self.attrack = 100 + rhs.attrack
        self.defend = 300 + rhs.defend

    def ShowAttributes(self):
        print("*on cloth*")
        print("attrack : %d" % (self.attrack))
        print("attrack : %d \r\n" % (self.defend))


class OnWeapon(Warrior):
    def __init__(self, rhs):
        self.attrack = 1500 + rhs.attrack
        self.defend = 100 + rhs.defend

    def ShowAttributes(self):
        print("*on weapon*")
        print("attrack : %d " % (self.attrack))
        print("attrack : %d \r\n" % (self.defend))


if "__main__" == __name__:
    print("crete a warrior....")
    person = Warrior()
    person.ShowAttributes()

    print("put on cloth....")
    putonCloth = OnCloth(person)
    person.ShowAttributes()
    putonCloth.ShowAttributes()

    print("put on weapon....")
    holdWeapon = OnWeapon(putonCloth)
    person.ShowAttributes()
    putonCloth.ShowAttributes()
    holdWeapon.ShowAttributes()

'''
装饰模式，经过装饰后总的属性发生变化，但是本身属性不发生变化
crete a warrior....
*self*
attrack : 100
attrack : 200 
 
put on cloth....
*self*
attrack : 100
attrack : 200 
 
*on cloth*
attrack : 200
attrack : 500 
 
put on weapon....
*self*
attrack : 100
attrack : 200 
 
*on cloth*
attrack : 200
attrack : 500 
 
*on weapon*
attrack : 1700 
attrack : 600 
'''

