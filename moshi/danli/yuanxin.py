# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:41:57 2018

@author: mz
"""

from copy import copy, deepcopy


class Prototype(object):
    def Clone(self):
        pass

    def DeepClone(self):
        pass


class Year(object):
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, y):
        if isinstance(y, int):
            self._year = y
            return
        if isinstance(y, str) and y.isdigit():
            y = int(y)
            self._year = y
        else:
            raise ValueError("year is illegal")

    @year.deleter
    def year(self):
        del self._year


class Resume(Prototype):
    def __init__(self, name):
        self.name = name
        self.workingYear = 3
        self._year = Year()
        self._year.year = 3

    def SetWorkingYear(self, y):
        self.workingYear = y
        self._year.year = y

    def Clone(self):
        return copy(self)

    def DeepClone(self):
        return deepcopy(self)

    def Show(self):
        print(self.name, self.workingYear, self._year.year)


if "__main__" == __name__:
    resume = Resume("zhang san")
    resume.Show()

    a = resume.Clone()
    b = resume.DeepClone()

    print("\r\n---resume 10---")
    resume.SetWorkingYear(10)
    resume.Show()
    a.Show()
    b.Show()

    print("\r\n---clone a 8---")
    a.SetWorkingYear(8)
    resume.Show()
    a.Show()
    b.Show()

    print("\r\n---deep clone b 6---")
    b.SetWorkingYear(6)
    resume.Show()
    a.Show()
    b.Show()

'''
zhang san 3 3
 
---resume 10---
zhang san 10 10
zhang san 3 10
zhang san 3 3
 
---clone a 8---
zhang san 10 8
zhang san 8 8
zhang san 3 3
 
---deep clone b 6---
zhang san 10 8
zhang san 8 8
zhang san 6 6
'''