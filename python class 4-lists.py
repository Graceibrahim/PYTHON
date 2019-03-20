Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers=[1, 2, 3, 4, 5, 6]
>>> letter=["a", "b", "c", "d"]
>>> 2 in numbers
True
>>> c in letters
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c in letters
NameError: name 'c' is not defined
>>> "c" in letters
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    "c" in letters
NameError: name 'letters' is not defined
>>> "c" in letter
True
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> 
>>> numbers*3
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
>>> numbers+letter
[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd']
>>> fruits=["apple", "melon", "grapes", "mango", "banana"]
>>> fruits.append("orange")
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange']
>>> fruits.extend(["guava", "strawberries"])
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange', 'guava', 'strawberries']
>>> fruits.extend(["avocado" "peach"])
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange', 'guava', 'strawberries', 'avocadopeach']
>>> fruits.pop()
'avocadopeach'
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange', 'guava', 'strawberries']
>>> fruits.remove("banana")
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'orange', 'guava', 'strawberries']
>>> 
>>> fruits.reverse
<built-in method reverse of list object at 0x0343E058>
>>> fruits.reverse()
>>> fruits
['strawberries', 'guava', 'orange', 'mango', 'grapes', 'melon', 'apple']
>>> fruits.sort()
>>> fruits
['apple', 'grapes', 'guava', 'mango', 'melon', 'orange', 'strawberries']
>>> fruits.append("grapes")
>>> fruits.append("mango")
>>> fruits.append("guava")
>>> fruits
['apple', 'grapes', 'guava', 'mango', 'melon', 'orange', 'strawberries', 'grapes', 'mango', 'guava']
>>> fruits.count("grapes")
2
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> sum (numbers)
21
>>> max(numbers)
6
>>> min(number)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    min(number)
NameError: name 'number' is not defined
>>> min (numbers)
1
>>> max(fruits)
'strawberries'
>>> min (fruits)
'apple'
>>> sum(fruits)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    sum(fruits)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> fruits[0]
'apple'
>>> fruits[4]
'melon'
>>> fruits
['apple', 'grapes', 'guava', 'mango', 'melon', 'orange', 'strawberries', 'grapes', 'mango', 'guava']
>>> numbers[1]
2
>>> numbers[3]
4
>>> numbers[5]
6
>>> numbers[-5]
2
>>> fruits[-4]
'strawberries'
>>> numbers[-1]
6
>>> numbers[:-2]
[1, 2, 3, 4]
>>> numbers[-4:-1]
[3, 4, 5]
>>> fruits[3:]
['mango', 'melon', 'orange', 'strawberries', 'grapes', 'mango', 'guava']
>>> fruits[-5:-2]
['orange', 'strawberries', 'grapes']
>>> for fruit in fruits: print (fruit)

apple
grapes
guava
mango
melon
orange
strawberries
grapes
mango
guava
>>> for car in fruits: print (car)

apple
grapes
guava
mango
melon
orange
strawberries
grapes
mango
guava
>>> for number in number: print(number)

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    for number in number: print(number)
NameError: name 'number' is not defined
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> for number in numbers: print(number)

1
2
3
4
5
6
>>> for number in number:print(number*10)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    for number in number:print(number*10)
TypeError: 'int' object is not iterable
>>> for number in numbers:print(number*10)

10
20
30
40
50
60
>>> for number in numbers:print(number*10)

10
20
30
40
50
60
>>> for number in numbers:
	print(number*10)

	
10
20
30
40
50
60
>>> for each number in numbers:
	
SyntaxError: invalid syntax
>>> for number in numbers:
	print (number**2)

	
1
4
9
16
25
36
>>> for number in numbers:
	print (number*number)

	
1
4
9
16
25
36
>>> x=range (5,15)
>>> x
range(5, 15)
>>> for n in x:
	print (n)

	
5
6
7
8
9
10
11
12
13
14
>>> x=range (9,19)
>>> x=
SyntaxError: invalid syntax
>>> x
range(9, 19)
>>> for n in:
	
SyntaxError: invalid syntax
>>> for n in x:
	print(n*5)

	
45
50
55
60
65
70
75
80
85
90
>>> squares=[number*number for number in numbers]
>>> 
>>> squares
[1, 4, 9, 16, 25, 36]
>>> doubles=[number*2 for number in numbers]
>>> doubles
[2, 4, 6, 8, 10, 12]
>>> for number in numbers:
	x=number*2
	e.append(x)

	
Traceback (most recent call last):
  File "<pyshell#99>", line 3, in <module>
    e.append(x)
NameError: name 'e' is not defined
>>> e=[]
>>> for number in numbers:
	x=number*2
	e.append(x)

	
>>> x
12
>>> e
[2, 4, 6, 8, 10, 12]
>>> for number in numbers:
	x=number*2
	e.append(x)
	e

	
[2, 4, 6, 8, 10, 12, 2]
[2, 4, 6, 8, 10, 12, 2, 4]
[2, 4, 6, 8, 10, 12, 2, 4, 6]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12]
>>> e
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12]
>>> e==doubles
False
>>> for number in numbers:
	x=number*2
	e.append(x)
	e

	
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12]
>>> e==doubles
False
>>> e
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12]
>>> doubles
[2, 4, 6, 8, 10, 12]
>>> doubles=[number*2 for number in numbers]
>>> e==doubles
False
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> doubles
[2, 4, 6, 8, 10, 12]
>>> e
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12]
>>> for numbers in numbers:
	x=number*2
	e.append(x)
	e

	
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 12]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 12, 12]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 12, 12, 12]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 12, 12, 12, 12]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 12, 12, 12, 12, 12]
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 12, 12, 12, 12, 12, 12]
>>> e==doubles
False
>>> e
[2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 2, 4, 6, 8, 10, 12, 12, 12, 12, 12, 12, 12]
>>> e=[]
>>> 
>>> for numbers in numbers:
	x=number*2
	e.append(x)

	
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    for numbers in numbers:
TypeError: 'int' object is not iterable
>>> for number in numbers:
	x=number*2
	e.append(x)

	
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    for number in numbers:
TypeError: 'int' object is not iterable
>>> for numberin numbers:
	x=number*2
	e.append(x)
	e
	
SyntaxError: invalid syntax
>>> for number in numbers:
	x=number*2
	e.append(x)

	
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    for number in numbers:
TypeError: 'int' object is not iterable
>>> numbers [1, 2, 3, 4, 5, 6,7]
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    numbers [1, 2, 3, 4, 5, 6,7]
TypeError: 'int' object is not subscriptable
>>> numbers=[1, 2, 3, 4, 5, 6,7]
>>> doubles=[number*2 for number in numbers]
>>> for number in numbers:
	x=number*2
	e.append(x)

	
>>> e
[2, 4, 6, 8, 10, 12, 14]
>>> doubles
[2, 4, 6, 8, 10, 12, 14]
>>> e==doubles
True
>>> m=[100, 200, 300, 400,500]
>>> for number in m:
	print(number/7)

	
14.285714285714286
28.571428571428573
42.857142857142854
57.142857142857146
71.42857142857143
>>> for number in m:
	print(number%7)

	
2
4
6
1
3
>>> for number in m:
	p=(number%7)

	
>>> 
>>> p
3
>>> p=[number/7for number in m]
>>> p
[14.285714285714286, 28.571428571428573, 42.857142857142854, 57.142857142857146, 71.42857142857143]
>>> p(%)
SyntaxError: invalid syntax
>>> for number in m:
	p=(number%7)

	
>>> 
>>> p
3
>>> divide=[m%7 for number in m]
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    divide=[m%7 for number in m]
  File "<pyshell#160>", line 1, in <listcomp>
    divide=[m%7 for number in m]
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> p=[m%7 for number in m]
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    p=[m%7 for number in m]
  File "<pyshell#161>", line 1, in <listcomp>
    p=[m%7 for number in m]
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> p=[number %7 for number in m]
>>> 
>>> p
[2, 4, 6, 1, 3]
>>> for number in m:
	a=number%7
	k.append(a)

	
Traceback (most recent call last):
  File "<pyshell#168>", line 3, in <module>
    k.append(a)
NameError: name 'k' is not defined
>>> 
>>> k
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    k
NameError: name 'k' is not defined
>>> for number in m:
	a=number%7
	k.append(a)

	
Traceback (most recent call last):
  File "<pyshell#172>", line 3, in <module>
    k.append(a)
NameError: name 'k' is not defined
>>> range
<class 'range'>
>>> 
>>> 
>>> range(78, 88)
range(78, 88)
>>> w=range(78, 88)
>>> w
range(78, 88)
>>> for  x in w:
	print (X%6)

	
Traceback (most recent call last):
  File "<pyshell#181>", line 2, in <module>
    print (X%6)
NameError: name 'X' is not defined
>>> w
range(78, 88)
>>> x=[0, 1,3, 4, 5, 6, 7, 8, 9,]
