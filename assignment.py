Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> listx = [1,2,3,4,5,6,7,8,9]
>>> listx.append(3)
>>> listx
[1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
>>> listx.remove(4)
>>> listx
[1, 2, 3, 5, 6, 7, 8, 9, 3]
>>> listx.insert(2,-1)
>>> listx
[1, 2, -1, 3, 5, 6, 7, 8, 9, 3]
>>> listx.reverse()
>>> listx
[3, 9, 8, 7, 6, 5, 3, -1, 2, 1]
>>> listx.extend([10,15]);
>>> listx
[3, 9, 8, 7, 6, 5, 3, -1, 2, 1, 10, 15]
>>> listx.pop()
15
>>> listx.index(6)
4
>>> listx.sort()
>>> listx
[-1, 1, 2, 3, 3, 5, 6, 7, 8, 9, 10]
>>> listx.count([-1, 1, 2, 3, 3, 5, 6, 7, 8, 9, 10])
0
>>> listy = [x*10 for n in (listx)]

>>> listy = [x*10 for x in (listx)]
>>> listy
[-10, 10, 20, 30, 30, 50, 60, 70, 80, 90, 100]
>>> 
>>> 
>>> k= (listx[0:6])
>>> k
[-1, 1, 2, 3, 3, 5]
>>> u= (listx[6:0])
>>> u
[]
>>> u = (listx[6:])
>>> u
[6, 7, 8, 9, 10]
>>> n=[[1,2,3], [4,5,6], [7,8,9]]
>>> 
>>> m= [1,2,3,4,5,6,7,8,9]
>>> m.append(n)
>>> m
[1, 2, 3, 4, 5, 6, 7, 8, 9, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
>>> 
