a = 'ABC'
b = a
a = 'XYZ'
print(b)
print(a)

# -*- coding: utf-8 -*-

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "\nBart"'
s4 = r'''Hello, 
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')



def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return 1
    else:
        x = move(n-1, a, c, b)
        y = move(1, a, b, c)
        z = move(n-1, b, a, c)
        return x + y + z 


count = move(5,'A','B','C')
print(str(count))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value: ',e.value)
        break
