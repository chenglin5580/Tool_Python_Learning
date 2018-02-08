# Function Programming



## 基础概念
- 面向过程的程序设计：函数封装，函数就是面向过程的程序设计的基本单元。
- 计算机（Computer）和计算（Compute）的概念。
1. 在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。
2. 而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远
- Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

## 高阶函数
- 函数也是对象，在Python中无处不对象
- 变量可以指向函数，f=abs()
- 函数名字也可以另定义为变量
- 函数可以做函数参数

### map 和 reduce
- map()
1. 传入为函数和Iterable,r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
2. 输出为Iterator
- reduce
1. 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
2. reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

### filter()
- Python内建的filter()函数用于过滤序列。
- 能够对数据进行筛选
- [例子](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000)

### sorter()
- Python内置的sorted()函数就可以对list进行排序：
- sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
- 这样，我们给sorted传入key函数，即可实现忽略大小写的排序
- 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：


## 返回函数
- 函数可以作为return返回[具体](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000)

## 匿名函数，lambda函数
- 格式 lambda x: x*x
- list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 待学习部分
[地址](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317848428125ae6aa24068b4c50a7e71501ab275d52000)


