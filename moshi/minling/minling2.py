# coding:utf-8
"""
命令模式
在请求者和请求实现者之间，把请求抽象成命令，并添加一个命令接受和分发者，实现请求者和实现者的解耦
如客户（请求者）去烧烤店吃饭，并不需要认识烧烤boy（实现者），只需要有菜单（命令），服务员（命令接收和分发者），然后根据
菜单给服务员下单就好了。然后菜单有会有记录，我们可以要求撤销和重做，烧烤店可以拒绝我们的某个菜单。
优点：1、可以有一个命令列表；2、命令可以很容易写入日志；3、命令可以被撤销或重做；4、命令实现者可以拒绝命令；5、实现了请求者
和实现者的解耦；6、要加入新的命令很容易，增加个命令类，实现者能做对应的命令
"""
from abc import ABCMeta, abstractmethod

class Cooker(object):
    """
    厨师
    """
    def __init__(self):
        self._num_yang = 1
        self._num_niu = 1

    def cook_yang(self):
        if self._num_yang <= 3:
            print("烧烤羊肉串")
            self._num_yang += 1
        else:
            print("没羊肉串了")

    def cook_niu(self):
        if self._num_niu <= 3:
            print("烧烤牛肉串")
            self._num_niu += 1
        else:
            print("没牛肉串了")


class Command(object):
    """
    抽象菜单
    """
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.cooker = Cooker()
        self.name = name

    @abstractmethod
    def cook(self):
        pass


class CommandYang(Command):
    def __init__(self, name):
        super(CommandYang, self).__init__(name)

    def cook(self):
        self.cooker.cook_yang()


class CommandNiu(Command):
    def __init__(self, name):
        super(CommandNiu, self).__init__(name)

    def cook(self):
        self.cooker.cook_niu()


class Waiter(object):
    def __init__(self):
        self._command_list = []
        self._menu = None
        self._kehu = None

    def set_kehu(self, kehu):
        self._kehu = kehu

    def set_order(self, command, num=1):
        print("加菜：" + command.name)
        for i in range(num):
            self._command_list.append(command)

    def remove_order(self, command, num=1):
        print("减菜：" + command.name)
        try:
            for i in range(num):
                self._command_list.remove(command)
        except Exception as e:
            print("没点那么多菜")

    def notify(self):
        print("下单啦：")
        self._menu = Order(self._kehu, self._command_list)
        self._menu.show()
        for command in self._command_list:
            command.cook()
        self._command_list = []
        print("")


class Order(object):
    def __init__(self, name, command_list):
        self._command_list = command_list
        self._name = name

    def set_order(self, command_list):
        self._command_list = command_list

    def set_name(self, name):
        self._name = name

    def show(self):
        print(self._name + "，您的菜单是：")
        for command in self._command_list:
            print(command.name)
        print("")


if __name__ == '__main__':
    # 烧烤店初始化
    command_yang = CommandYang("羊肉串")
    command_niu = CommandNiu("牛肉串")
    waiter = Waiter()

    # 营业
    waiter.set_kehu("张三")
    waiter.set_order(command_yang, 4)
    waiter.set_order(command_niu, 5)
    waiter.notify()