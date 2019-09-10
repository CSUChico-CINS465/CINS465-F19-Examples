#!/usr/bin/python

print("Hello World")

x=3
x="c"
x=[1,2,3]
x=[1,"2",3]
def x(x):
    print(x)
#
# x(x)

y="y"
x=3
z = str(x) + y
print(z)

x = [1,2,3]
x += [4]
x.append(5)

y = (1,2,3)
x+=[y]
try:
    y += (4)
except:
    print("Tuple's are immutable")
# print(x[5][2])
z = {"key":"value","list":x, "tuple":y}
print(z)
# print(x[2])
# print(y[2])

class MyClass:
    """A simple example class"""
    def __init__(self):
        self.data = []
        self.i = 12345

    def f(self, blah, alice=4, bob=5):
        # self.bob= 4
        return 'hello world ' + str(blah) + " " + str(alice) + " " + str(bob)

x = MyClass()
print(x.f(bob=1, blah="hi"))
