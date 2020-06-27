from datetime import datetime
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
print('Functions\n')
def callName(name):
  print("Name called: " + name)

callName("Fritz")

def add(a, b):
  return a + b

sum = add(1, 5)
print('Sum added from function: ', sum)
