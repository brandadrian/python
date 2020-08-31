import time
from datetime import datetime

class Basics():
    def firstMethod(self):
#Python Basics
        print('Python Basics Script\n')
        print('...for Adrian Brand...')

###Variables###
        print('Simple Math\n')
        a = 42
        b = 2
        c = 2 * 42
        print('Result: ', a, '+', b, '=', c)

###Variables###
        print('Conditions\n')
        if c > 10:
            print(c, 'is larger than 10')
        elif c == 10:
            print(c, 'is qual to 10')
        else:
            print(c, 'is smaller than 10')

###DateTime###
        dateTimeObj = datetime.now()
        print('Message from: ', dateTimeObj)

###Loops###
        print('For Loop\n')
        position = 0
        for i in range(0, 10):
            print('Loop:', position)
            position = position + 1

###Functions###
    def callMethods(self):
        self.callName('fritz')
        sum = self.add(1, 5)
        print('Sum added from function: ', sum)
            
    def callName(self, name):
        print("Name called: " + name)

    def add(self, a, b):
        return a + b

    def showUserInput(self):
        seconds = input('Countdown [s]: ')
        seconds = int(seconds)
        while seconds > -1:
            print('Countdown: ', seconds, 's')
            time.sleep(1)
            seconds=seconds-1


test = Basics()
test.showUserInput()
