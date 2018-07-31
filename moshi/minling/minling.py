# coding:utf-8
from abc import ABCMeta,abstractmethod

class Switch:
    def __init__(self, flipUpCmd, flipDownCmd):
        self.__flipUpCommand = flipUpCmd
        self.__flipDownCommand = flipDownCmd

    def flipUp(self):
        self.__flipUpCommand.execute()

    def flipDown(self):
        self.__flipDownCommand.execute()

class Light:
    def turnOn(self):
        print "The light is on"

    def turnOff(self):
        print "The light is off"

class Command:
    __metaclass__ = ABCMeta
    def __init__(self):
        pass
    @abstractmethod
    def execute(self):
        pass

class FlipUpCommand(Command):
    '''The Command class for turning on the light'''

    def __init__(self, light):
        Command.__init__(self)
        self.__light = light

    def execute(self):
        self.__light.turnOn()

class FileDownCommand(Command):
    def __init__(self, light):
        Command.__init__(self)
        self.__light = light

    def execute(self):
        self.__light.turnOff()

class LightSwitch:
    def __init__(self):
        self.__lamp = Light()
        self.__switchUp = FlipUpCommand(self.__lamp)
        self.__switchDown = FileDownCommand(self.__lamp)
        self.__switch = Switch(self.__switchUp, self.__switchDown)

    def switch(self, cmd):
        cmd = cmd.strip().upper()
        try:
            if cmd == "ON":
                self.__switch.flipUp()
            elif cmd == "OFF":
                self.__switch.flipDown()
            else:
                print "Argument \"ON\" or \"OFF\" is required"
        except Exception,msg:
            print "Exception occured:%s" % msg

if __name__ == "__main__":
    lightSwitch = LightSwitch()

    print "Switch ON test"
    lightSwitch.switch("ON")

    print "Switch OFF test"
    lightSwitch.switch("OFF")

    print "Invalid Command test"
    lightSwitch.switch("****")