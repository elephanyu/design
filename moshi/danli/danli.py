# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:40:24 2018

@author: mz
"""
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


class SingleTonTest(object):
    def create(self):
        for i in range(10):
            t = threading.Thread(target=SingleTonTest.PrintAddress, args=[i, ])
            t.start()

    def PrintAddress(self):
        print(Singleton())


if "__main__" == __name__:
    sig0 = Singleton()
    sig1 = Singleton()

    print(sig0)
    print(sig1)

    test = SingleTonTest();
    test.create()

'''
<__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630><__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630>
<__main__.Singleton object at 0x0000019E475BD630>
'''