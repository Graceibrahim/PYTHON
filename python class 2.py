Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> a
10
>>> b
20
>>> c="cat"
>>> d="dog"
>>> c
'cat'
>>> d
'dog'
>>> e=a/3
>>> e
3.3333333333333335
>>> type(e)
<class 'float'>
>>> type(c)
<class 'str'>
>>> type(a)
<class 'int'>
>>> str (a)
'10'
>>> f
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> f=str(a)
>>> type (f)
<class 'str'>
>>> g='123'
>>> h=int (g)
>>> g='123'
>>> h=int(g)
>>> i=int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    i=int(c)
ValueError: invalid literal for int() with base 10: 'cat'
>>> n=float(a)
>>> n
10.0
>>> print(Hello Akirachix)
SyntaxError: invalid syntax
>>> print("Hello Akirachix')
	  
SyntaxError: EOL while scanning string literal
>>> 
	  
>>> print("Hello Akirachix")
	  
Hello Akirachix
>>> print("Hello Akirachix.\n class of 2019")
	  
Hello Akirachix.
 class of 2019
>>> print("Hello Akirachix.\t class of 2019")
	  
Hello Akirachix.	 class of 2019
>>> print("Hello Akirachix.\b class of 2019")
	  
Hello Akirachix. class of 2019
>>> firstname="Grace"
	  
>>> last="Nyokabi"
	  
>>> greeting="hello, {}{}"format (firstname,last)
	  
SyntaxError: invalid syntax
>>> greeting="hello, {}{}".format (firstname,last)
	  
>>> greeting
	  
'hello, GraceNyokabi'
>>> greeting="hello, {}{}".format (firstname, last)
	  
>>> greeting
	  
'hello, GraceNyokabi'
>>> code=abc123
	  
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    code=abc123
NameError: name 'abc123' is not defined
>>> code="abc123"
	  
>>> amount"1000"
	  
SyntaxError: invalid syntax
>>> amount="1000"
	  
>>> reciepient="0721000000"
	  
>>> print(code) "confirmed! Hi" (firstname) \n("you have sent ksh"amount)
	  
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntaxprint(code) "confirmed! Hi "(firstname) \n("you have sent ksh"amount)
	  
SyntaxError: invalid syntax
>>> print (code "confirmed! Hi" firstname \n("you have sent ksh"amount)
	   
SyntaxError: invalid syntax
>>> print (code "confirmed! Hi firstname \n("you have sent ksh"amount)
	   
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntaxprint(code) "confirmed! Hi "(firstname) \n("you have sent ksh"amount)
	   
SyntaxError: invalid syntax
>>> print(code+"confirmed! Hi "+firstname+ \n+ "you have sent ksh"+amount)
	   
SyntaxError: unexpected character after line continuation character
>>> print(code+"confirmed! Hi "+firstname+ "\n"+ "you have sent ksh"+amount)
	   
abc123confirmed! Hi Grace
you have sent ksh1000
>>> print(code+" confirmed! Hi "+firstname+ \n+ "you have sent ksh"+amount)
	   
SyntaxError: unexpected character after line continuation character
>>> print(code+"confirmed! Hi "+firstname+ "\n"+ "you have sent ksh"+amount)
	   
abc123confirmed! Hi Grace
you have sent ksh1000
>>> SyntaxError: unexpected character after line continuation characterprint(code+"confirmed! Hi "+firstname+ "\n"+ "you have sent ksh"+amount)print(code+"confirmed! Hi "+firstname+ "\n"+ "you have sent ksh"+amount+ "to" +receipient)
	   
SyntaxError: invalid syntax
>>> SyntaxError: unexpected character after line continuation characterprint(code+" "+"confirmed! Hi "+firstname+ "\n"+ "you have sent ksh"+amount)print(code+"confirmed! Hi "+firstname+ "\n"+ "you have sent ksh"+amount+ "to" +receipient)
	   
SyntaxError: invalid syntax
>>> print(code+" "+"confirmed! Hi "+firstname+"\n" +"you have sent ksh "+amount+ "to "+receipient)
	   
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(code+" "+"confirmed! Hi "+firstname+"\n" +"you have sent ksh "+amount+ "to "+receipient)
NameError: name 'receipient' is not defined
>>> print(code+" "+"confirmed! Hi "+firstname+"\n" +"you have sent ksh "+amount+ "to "+reciepient)
	   
abc123 confirmed! Hi Grace
you have sent ksh 1000to 0721000000
>>> print(code+" "+"confirmed! Hi "+firstname+"\n" +"you have sent ksh "+amount+" "+ "to "+reciepient)
	   
abc123 confirmed! Hi Grace
you have sent ksh 1000 to 0721000000
>>> print(code+" "+"confirmed! Hi "+firstname+"\n" +"you have sent ksh "+amount+"\n"+" "+ "to "+reciepient)
	   
abc123 confirmed! Hi Grace
you have sent ksh 1000
 to 0721000000
>>> 
