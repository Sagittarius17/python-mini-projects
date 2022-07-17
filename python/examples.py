import time
from unicodedata import numeric

from phonenumbers import is_alpha_number
from pyparsing import alphas



'''
x = 6
y = "t"
x = y #include this line output will be "tt"
print(str(x) + y) # output 6t


#sorting list without using 'sort'
list = [5, 8, 3, 84, 99, 22, -102, 39]
new_list = len(list)

for i in range(new_list):
    for j in range(i+1,new_list):
        if list[i]>list[j]:
            list[i], list[j] = list[j], list[i]
            
print(list)


#check if a string is palindrome or not(short way)
name = 'fjfjf'
if name == name[::-1]:
    print("its palindrome")
else:
    print('isnt palindrome')

#check if a string is palindrome or not(long way)
name = 'fjfjf'
new_name = len(name)
x = 0

for i in range(new_name):
    if name[i] != name[new_name-i-1]:
        x = 1
    break

if x == 0:
    print("its palindrome")
else:
    print('isnt palindrome')

#fibonnaci
def fibonnaci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
fib = fibonnaci()
for i in range(10):
    print(next(fib))
    time.sleep(1)


#
name = input("write down your word --> ")
if name == name [::-1]:
    print('ok')
else:
    print('not ok')

try: print(1)
except: print(2)
finally: print(3)'''

list = [1, 'dsds', 6, 'sdfdfdsf', 'fdfdcvs', 'vsvc', 6, 9, 3,18]

for i in list:
    if str(i).isnumeric() and i > 6:
        print(i)

    if str(i) is alphas:
        print(i)
        
