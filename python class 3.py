Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> firstname="james"
>>> second name="jane"
SyntaxError: invalid syntax
>>> secondname="jane"
>>> balance=1000
>>> secondbalance=10000
>>> print(hello{} your balance is
	  
SyntaxError: invalid syntax
>>> 
	  
>>> print("hello{} your balance is{}") format firstname+balance
	  
SyntaxError: invalid syntax
>>> print("hello{} your balance is{}") format (firstname+balance)
	  
SyntaxError: invalid syntax
>>> print("hello{} your balance is{}" format firstname+balance)
	  
SyntaxError: invalid syntax
>>> print("hello{} your balance is{}".format (firstname+balance))
	  
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("hello{} your balance is{}".format (firstname+balance))
TypeError: can only concatenate str (not "int") to str
>>> print("hello{} your balance is{}".format firstname+balance)
	  
SyntaxError: invalid syntax
>>> print("hello{} your balance is{}". format firstname+balance)
	  
SyntaxError: invalid syntax
>>> print("hello{} your balance is{}". format-firstname+balance)
	  
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("hello{} your balance is{}". format-firstname+balance)
TypeError: unsupported operand type(s) for -: 'builtin_function_or_method' and 'str'
>>> print("hello{} your balance is{}". format(firstname+balance))
	  
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print("hello{} your balance is{}". format(firstname+balance))
TypeError: can only concatenate str (not "int") to str
>>> print("hello{} your balance is{}". format("firstname"+balance))
	  
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("hello{} your balance is{}". format("firstname"+balance))
TypeError: can only concatenate str (not "int") to str
>>> print("hello{} your balance is{}". format(firstname,balance))
	  
hellojames your balance is1000
>>> print("hello {} /n your balance is{}". format(firstname,balance))
	  
hello james /n your balance is1000
>>> print("hello {} \n your balance is{}". format(firstname,balance))
	  
hello james 
 your balance is1000
>>> print("Hello {} \n your balance is {}". format(firstname,balance))
	  
Hello james 
 your balance is 1000
>>> print("hello {} \n your balance is {}". format(secondname, secondbalance))
	  
hello jane 
 your balance is 10000
>>> print("Hello {} \n your balance is {}". format(secondname, secondbalance))
	  
Hello jane 
 your balance is 10000
>>> a='car'
	  
>>> b=10
	  
>>> type(a)
	  
<class 'str'>
>>> type
	  
<class 'type'>
>>> 
	  
>>> type(b)
	  
<class 'int'>
>>> s="AkiraChix"
	  
>>> s.upper
	  
<built-in method upper of str object at 0x01D3E408>
>>> s.uppper
	  
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.uppper
AttributeError: 'str' object has no attribute 'uppper'
>>> s.upper()
	  
'AKIRACHIX'
>>> s.lower()
	  
'akirachix'
>>> s.capitalize()
	  
'Akirachix'
>>> s.endswith(x)
	  
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s.endswith(x)
NameError: name 'x' is not defined
>>> s.endswith("x")
	  
True
>>> s.startswith("a")
	  
False
>>> s.startswith("k")
	  
False
>>> s.islower()
	  
False
>>> b=s.lower
	  
>>> 
	  

>>> 
	  

>>> 
	  

>>> 
	  

>>> b=s.lower
	  
>>> 
	  



>>> b=s.lower()
	  
>>> b=is.lower()
	  
SyntaxError: invalid syntax
>>> b=islower()
	  
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    b=islower()
NameError: name 'islower' is not defined
>>> b=s.islower()
	  
>>> b.isalpha
	  
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    b.isalpha
AttributeError: 'bool' object has no attribute 'isalpha'
>>> s.islower
	  
<built-in method islower of str object at 0x01D3E408>
>>> b=s.lower
	  
>>> b=s.islower()
	  
>>> b.islower
	  
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b.islower
AttributeError: 'bool' object has no attribute 'islower'
>>> b.islower()
	  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    b.islower()
AttributeError: 'bool' object has no attribute 'islower'
>>> s.replace("x" "z")
	  
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s.replace("x" "z")
TypeError: replace() takes at least 2 arguments (1 given)
>>> s.replace("x" "z")
	  
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s.replace("x" "z")
TypeError: replace() takes at least 2 arguments (1 given)
>>> s="akirachix"
	  
>>> s.replace("x","z")
	  
'akirachiz'
>>> s.isalpha()
	  
True
>>> s.replace("c","x")
	  
'akiraxhix'
>>> a[]
	  
SyntaxError: invalid syntax
>>> s[0]
	  
'a'
>>> s
	  
'akirachix'
>>> 
	  

>>> 
	  
>>> 
	  

>>> s[-9]
	  
'a'
>>> s[-1]
	  
'x'
>>> s[1]
	  
'k'
>>> len(s)
	  
9
>>> s[0:4]
	  
'akir'
>>> s[2:6]
	  
'irac'
>>> s[5:8]
	  
'chi'
>>> s[5:10]
	  
'chix'
>>> s[3:]
	  
'rachix'
>>> s[:4]
	  
'akir'
>>> s[-9:-6]
	  
'aki'
>>> s[9:-5]
	  
''
>>> s[-9:-5]
	  
'akir'
>>> s[0:4]=s[-9:-5]
	  
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s[0:4]=s[-9:-5]
TypeError: 'str' object does not support item assignment
>>> s[0:4]==s[-9:-5]
	  
True
>>> s[5:8]==s[-1:-5]
	  
False
>>> s[5:8]==s[-1:-4]
	  
False
>>> s[5:8]==s[-4:-1]
	  
True
>>> s[5:9]==[-4:-1]
	  
SyntaxError: invalid syntax
>>> s[5:9]==[-4:-1]
	  
SyntaxError: invalid syntax
>>> s[5:9]==s[-4:-1]
	  
False
>>> s[5:9]==s[-4:0]
	  
False
>>> s[5:9]==s[-4:-0]
	  
False
>>> s[3:]==s[-6:-1]
	  
False
>>> s[3:]==s[-6:]
	  
True
>>> s[5:9]==s[-4]
	  
False
>>> 
	  

>>> 
	  
>>> s[5:9]==s[:-4]
	  
False
>>> s[5:9]==s[-4;]
	  
SyntaxError: invalid syntax
>>> 
	  
>>> s[5:9]==s[-4:]
	  
True
>>> firstname="grace'
	  
SyntaxError: EOL while scanning string literal
>>> firstname="grace"
	  
>>> second name="nyokabi"
	  
SyntaxError: invalid syntax
>>> secondname="nyokabi"
	  
>>> fullname=("{},{}".format(firstname, secondname))
	  
>>> fullname=("{},{}". format(firstname, secondname))
	  
>>> fullname="{},{}". format(firstname, secondname)
	  
>>> fullname=print"{},{}". format(firstname, secondname)
	  
SyntaxError: invalid syntax
>>> fullname="{},{}". format(firstname,secondname)
	  
>>> fullname="{} {}".format(firstname,secondname)
	  
>>> fullname="{} {}".format(firstname,secondname)
	  
>>> firstname='grace"
	  
SyntaxError: EOL while scanning string literal
>>> firstname='grace'
	  
>>> secondname="nyokabi"
	  
>>> fullname="{}, {}".format(firstname,secondname)
	  
>>> fullname="{} {}".format(firstname,secondname)
	  
>>> fullname
	  
'grace nyokabi'
>>> a=fullname
	  
>>> a=fullname[-1:-11]
	  
>>> a=fullname[-1:-11]
	  
>>> b=fullname[0:11]
	  
>>> a=fullname[-1:-12]
	  
>>> a==firstname
	  
False
>>> b==secondname
	  
False
>>> a=fullname
	  
>>> a=fullname[-1:-5]
	  
>>> b=fullname[5:11]
	  
>>> a=firstname
	  
>>> b==secondname
	  
False
>>> a==firstname
	  
True
>>> a=fullname[4:11]
	  
>>> a==secondname
	  
False
>>> bfullname[5:11]
	  
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    bfullname[5:11]
NameError: name 'bfullname' is not defined
>>> b=fullname[5:11]
	  
>>> b==secondname
	  
False
>>> b=fullname[5:]
	  
>>> b==secondname
	  
False
>>> b=fullname[:5]
	  
>>> b==secondname
	  
False
>>> b=fullname[:4]
	  
>>> b==secondname
	  
False
>>> b=fullname[4:]
	  
>>> b==secondname
	  
False
>>> b
	  
'e nyokabi'
>>> firstname="grace"
	  
>>> secondname="nyokabi"
	  
>>> fullname="{}{}".format(firstname,secondname)
	  
>>> fullname
	  
'gracenyokabi'
>>> a=fullname
	  
>>> 
	  
>>> a=fullname[-1:-5]
	  
>>> b=fullname[:-5]
	  
>>> a==firstname
	  
False
>>> a=fullname[-1:-5]
	  
>>> a==firstname
	  
False
>>> a
	  
''
>>> firstname
	  
'grace'
>>> secondname
	  
'nyokabi'
>>> fullname
	  
'gracenyokabi'
>>> help
	  
Type help() for interactive help, or help(object) for help about object.
>>> 
	  

>>> help()
	  

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> symbols

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> modules

Please wait a moment while I gather a list of all available modules...

Grace               asyncore            html                sched
__future__          atexit              http                scrolledlist
__main__            audioop             hyperparser         search
_abc                autocomplete        idle                searchbase
_ast                autocomplete_w      idle_test           searchengine
_asyncio            autoexpand          idlelib             secrets
_bisect             base64              imaplib             select
_blake2             bdb                 imghdr              selectors
_bootlocale         binascii            imp                 setuptools
_bz2                binhex              importlib           shelve
_codecs             bisect              inspect             shlex
_codecs_cn          browser             io                  shutil
_codecs_hk          builtins            iomenu              signal
_codecs_iso2022     bz2                 ipaddress           site
_codecs_jp          cProfile            itertools           smtpd
_codecs_kr          calendar            json                smtplib
_codecs_tw          calltip             keyword             sndhdr
_collections        calltip_w           lib2to3             socket
_collections_abc    cgi                 linecache           socketserver
_compat_pickle      cgitb               locale              sqlite3
_compression        chunk               logging             squeezer
_contextvars        cmath               lzma                sre_compile
_csv                cmd                 macosx              sre_constants
_ctypes             code                macpath             sre_parse
_ctypes_test        codecontext         mailbox             ssl
_datetime           codecs              mailcap             stackviewer
_decimal            codeop              mainmenu            stat
_dummy_thread       collections         marshal             statistics
_elementtree        colorizer           math                statusbar
_functools          colorsys            mimetypes           string
_hashlib            compileall          mmap                stringprep
_heapq              concurrent          modulefinder        struct
_imp                config              msilib              subprocess
_io                 config_key          msvcrt              sunau
_json               configdialog        multicall           symbol
_locale             configparser        multiprocessing     symtable
_lsprof             contextlib          netrc               sys
_lzma               contextvars         nntplib             sysconfig
_markupbase         copy                nt                  tabnanny
_md5                copyreg             ntpath              tarfile
_msi                crypt               nturl2path          telnetlib
_multibytecodec     csv                 numbers             tempfile
_multiprocessing    ctypes              opcode              test
_opcode             curses              operator            textview
_operator           dataclasses         optparse            textwrap
_osx_support        datetime            os                  this
_overlapped         dbm                 outwin              threading
_pickle             debugger            paragraph           time
_py_abc             debugger_r          parenmatch          timeit
_pydecimal          debugobj            parser              tkinter
_pyio               debugobj_r          pathbrowser         token
_queue              decimal             pathlib             tokenize
_random             delegator           pdb                 tooltip
_sha1               difflib             percolator          trace
_sha256             dis                 pickle              traceback
_sha3               distutils           pickletools         tracemalloc
_sha512             doctest             pip                 tree
_signal             dummy_threading     pipes               tty
_sitebuiltins       dynoption           pkg_resources       turtle
_socket             easy_install        pkgutil             turtledemo
_sqlite3            editor              platform            types
_sre                email               plistlib            typing
_ssl                encodings           poplib              undo
_stat               ensurepip           posixpath           unicodedata
_string             enum                pprint              unittest
_strptime           errno               profile             urllib
_struct             faulthandler        pstats              uu
_symtable           filecmp             pty                 uuid
_testbuffer         fileinput           py_compile          venv
_testcapi           filelist            pyclbr              warnings
_testconsole        fnmatch             pydoc               wave
_testimportmultiple formatter           pydoc_data          weakref
_testmultiphase     fractions           pyexpat             webbrowser
_thread             ftplib              pyparse             window
_threading_local    functools           pyshell             winreg
_tkinter            gc                  query               winsound
_tracemalloc        genericpath         queue               wsgiref
_warnings           getopt              quopri              xdrlib
_weakref            getpass             random              xml
_weakrefset         gettext             re                  xmlrpc
_winapi             glob                redirector          xxsubtype
abc                 grep                replace             zipapp
aifc                gzip                reprlib             zipfile
antigravity         hashlib             rlcompleter         zipimport
argparse            heapq               rpc                 zlib
array               help                rstrip              zoomheight
ast                 help_about          run                 zzdummy
asynchat            history             runpy               
asyncio             hmac                runscript           

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> ()>>help(s)
No Python documentation found for '()>>help(s)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> (str)
No Python documentation found for '(str)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> help (str)
No Python documentation found for 'help (str)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 'help str'
No Python documentation found for 'help str'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 
