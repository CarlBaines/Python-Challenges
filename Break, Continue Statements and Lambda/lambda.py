import time

z = lambda a:a + 4
print(z(4))
time.sleep(1)

y = lambda a,b: a*b
print(y(2,3)) #multiplication
time.sleep(1)

x = lambda a,b: a/b
print(x(6,3)) #division
time.sleep(1)

w = lambda a:a-4
print(w(8)) #subtraction
time.sleep(1)

a = lambda a,b,c: a*b*c
print(a(1,2,3))
