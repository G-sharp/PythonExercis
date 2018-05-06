# Python 学习 #
`python`

作者：S0NNET
## Day1 ##
1. **python函数**

  函数通过def关键字定义，形如
   ``` python
   def function (arg1,arg2,...):
       ...
   fuction(1,2,...) #call function
   ```
    DocStrings文档字符串

    DocStrings文档字符串是一个重要工具，用于解释文档程序。
    ``` python
    def function（）：
        ''' say something here！
        '''
        pass
        ...
    print function.__doc__ #调用doc        
    ```
    *DocStrings文档字符串 使用惯例 它的首行以大写字母开始简述功能，第二行空行，第三行为函数的具体描述*
2. **python模块**

    Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
    模块让你能够有逻辑地组织你的 Python 代码段。把相关的代码分配到一个模块里能让你的代码更好用，更易懂。模块能定义函数，类和变量，模块里也能包含可执行的代码。以下是载入方法：
    1. import方法（全部引入）

    ```python
        import modules
    ```
    注意：*一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。*
    2. from ... import方法(部分引入)

    Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
    ``` python
        from modname import name1[, name2[, ... nameN]]
    ```
    3. from ... import*语句

    导入模块内所有内容，并不建议使用。

    Python模块搜索路径
    当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

      1.  当前目录
      2.  如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
      3.  如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

    **dir()函数**

       函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
    返回的列表容纳了在一个模块里定义的所有模块，变量和函数。
    特殊字符串变量\__name\__指向模块的名字，\__file__指向该模块的导入文件名。

    **globals() 和 locals() 函数**

    据调用地方的不同，globals()和locals()函数可被用来返回全局和局部命名空间里的名字。
    如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。    如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。    两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

3. **Python中的包**

    包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。简单来说，包就是文件夹，但该文件夹下必须存在 \__init\__.py 文件, 该文件的内容可以为空。\__init\__.py用于标识当前文件夹是一个包。
4. **常用模块**

    系统相关的信息模块: import sys

    sys.argv 是一个 list,包含所有的命令行参数.    
    sys.stdout sys.stdin sys.stderr 分别表示标准输入输出,错误输出的文件对象.    
    sys.stdin.readline() 从标准输入读一行 sys.stdout.write("a") 屏幕输出a    
    sys.exit(exit_code) 退出程序    
    sys.modules 是一个dictionary，表示系统中所有可用的module    
    sys.platform 得到运行的操作系统环境    
    sys.path 是一个list,指明所有查找module，package的路径.  
    操作系统相关的调用和操作: import os

    os.environ 一个dictionary 包含环境变量的映射关系   
    os.environ["HOME"] 可以得到环境变量HOME的值     
    os.chdir(dir) 改变当前目录 os.chdir('d:\\outlook')   
    注意windows下用到转义     
    os.getcwd() 得到当前目录     
    os.getegid() 得到有效组id os.getgid() 得到组id     
    os.getuid() 得到用户id os.geteuid() 得到有效用户id     
    os.setegid os.setegid() os.seteuid() os.setuid()     
    os.getgruops() 得到用户组名称列表     
    os.getlogin() 得到用户登录名称     
    os.getenv 得到环境变量     
    os.putenv 设置环境变量     
    os.umask 设置umask     
    os.system(cmd) 利用系统调用，运行cmd命令   
    内置模块(不用import就可以直接使用)常用内置函数：

    help(obj) 在线帮助, obj可是任何类型    
    callable(obj) 查看一个obj是不是可以像函数一样调用    
    repr(obj) 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝    
    eval_r(str) 表示合法的python表达式，返回这个表达式    
    dir(obj) 查看obj的name space中可见的name    
    hasattr(obj,name) 查看一个obj的name space中是否有name    
    getattr(obj,name) 得到一个obj的name space中的一个name    
    setattr(obj,name,value) 为一个obj的name   
    space中的一个name指向vale这个object    
    delattr(obj,name) 从obj的name space中删除一个name    
    vars(obj) 返回一个object的name space。用dictionary表示    
    locals() 返回一个局部name space,用dictionary表示    
    globals() 返回一个全局name space,用dictionary表示    
    type(obj) 查看一个obj的类型    
    isinstance(obj,cls) 查看obj是不是cls的instance    
    issubclass(subcls,supcls) 查看subcls是不是supcls的子类  

    ##################    类型转换  ##################

    chr(i) 把一个ASCII数值,变成字符    
    ord(i) 把一个字符或者unicode字符,变成ASCII数值    
    oct(x) 把整数x变成八进制表示的字符串    
    hex(x) 把整数x变成十六进制表示的字符串    
    str(obj) 得到obj的字符串描述    
    list(seq) 把一个sequence转换成一个list    
    tuple(seq) 把一个sequence转换成一个tuple    
    dict(),dict(list) 转换成一个dictionary    
    int(x) 转换成一个integer    
    long(x) 转换成一个long interger    
    float(x) 转换成一个浮点数    
    complex(x) 转换成复数    
    max(...) 求最大值    
    min(...) 求最小值  
------
## Day2
-  **数据结构**

   在python中有三种内建的数据结构--列表、元组和字典。
   * 列表（list）

      list是处理一组有序项目的数据结构，即你可以在一个列表中存储一个序列的项目。

      *列表是一种可变的数据类型。*
  ```python
       listname = [item1.item2,item3]
       listname.sort()
       listname.append(item4)
       del listname[0]
  ```  
   * 元组（Tuples）

     元组与列表极其类似，只不过元组和字符串一样是不可变 即使你不能修改元组。元组通过圆括号中用逗号分割的项目定义。

     元组最通常的用法是用在打印语句中，下面是一个例子：
     > print '%sis %d' % (name,age)

  * 字典(Dictionary)

    字典有键和值二元组，键是不可变的对象，字典的值可以任意。键值对在字典中以这样的方式标记
     >d ={key1:value1,key2:value2}

  * **序列（Sequence）**

    序列是列表，元组，字符串的总称，它的特点在于两个操作--索引操作符 （indexing/subscription）、切片操作符（slicing）
    ``` python
      list[-1],list[0],list[1],list[3]
      list[0；2] #0到1的 不包含2
      list[2:]  #2以后
      list[:]   #全部   
    ```
- **引用**

  当你创建一个对象并给它赋一个变量的时候，这个变量仅仅引用那个对象，而不是表示那个对象本身
  ！也就是说，变量名只是指向计算机中存储那个对象的内存。这被称作名称到对象的绑定。
  ```python
  #!/usr/bin/python
  #-*- coding=utf-8 -*-
  print 'Simple Assignment'
  shoplist = ['apple','mango','carrot','banana']
  mylist = shoplist #简单的赋值 只是引用变量名
  del shoplist[0]
  del mylist[0]
  print 'shoplist is',shoplist
  print 'mylist is',mylist

  print 'Coping by making full slice'
  mylist = shoplist[:]
  del mylist[0]
  print 'shoplist is',shoplist
  print 'mylist is',mylist

  ```
  >Simple Assignment

  >shoplist is ['carrot', 'banana']

  >mylist is ['carrot', 'banana']

  >Coping by making full slice

  >shoplist is ['carrot', 'banana']

  >mylist is ['banana']

很明显，普通引用只是名称的绑定，3而只有完整切片才是真正意义上的复制。所以我们在简单引用后一定要考虑是否可以更改，因为操作可能影响到源对象。
## Day3 ##

- **面向对象编程**
    * 注意在python中即使是整型也会被视为对象，这与C++和Java（1.5以前），在它们那儿整数是原始的内置类型。
     在python中秉承一切皆对象的原则。
     字段（Filed）：属于某个对象或类的变量
     方法（Method)：属于类的函数
     属性（Attribute）：上者综合
     -self
     类方法与普通函数的区别所在，将类函数参数项前面用self修饰。与C++中this作用类似。
     ``` python
    class Person:
        def say_hi(self):
            print('Hello,how are you?')
    ```
    Python中 特殊意义的类函数名称
     1. __init__ 方法
          该方法会在类的对象被实例化（Instantiated）时立即运行。这一方法可以用作初始化操作。
          ``` python
           class Person:
               def __init__(self,name)
                   self.name = name
               def say_hi(self)：
                 print（'Hello,my name is',self.name)
            p = Person('Swaroop')
            p.say_hi()
      ```
    2. 特殊变量命名方法
      1、 _xx 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。若内部变量标示，如： 当使用“from M import”时，不会将以一个下划线开头的对象引入 。

      2、 __xx 双下划线的表示的是私有类型的变量。只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量），调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）

      3、 __xx__定义的是特列方法。用户控制的命名空间内的变量或是属性，如init , __import__或是file 。只有当文档有说明时使用，不要自己定义这类变量。 （就是说这些是python内部定义的变量名）

      在这里强调说一下私有变量,python默认的成员函数和成员变量都是公开的,没有像其他类似语言的public,private等关键字修饰.但是可以在变量前面加上两个下划线"_",这样的话函数或变量就变成私有的.这是python的私有变量轧压(这个翻译好拗口),英文是(private name mangling.) **情况就是当变量被标记为私有后,在变量的前端插入类名,再类名前添加一个下划线"_",即形成了_ClassName__变量名.**
