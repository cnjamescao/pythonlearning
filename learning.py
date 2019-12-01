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