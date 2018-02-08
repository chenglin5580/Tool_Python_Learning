# Python Common Operation

[TOC]

## 结构
- .#是注释
- 当语句以冒号:结尾时，缩进的语句视为代码块
- 赋值语句：t = b, a + b, t是一个tuple,可以用x，y=

## 索引功能

## 切片Slice
- L[n1:n2] 其中[n1,n2)
- L[-1]最后一个
- L[:10:2] 隔两个取一个
- tuple也是list，也可以切片

## 迭代Iteration
- for ... in ...: 就是一种很常见的迭代形式
- 针对dict，可以采用for value in d.values()
- 由于字符串也是可迭代对象，因此，也可以作用于for循环
- 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
```
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
```

## 列表生成式 List Comprehension
- Python内置的非常简单却强大的可以用来**创建list**的生成式
- [x * x for x in range(1, 11)]
- 还可以加**判断** [x * x for x in range(1, 11) if x % 2 == 0]
- 可以使用**两层循环**，可以生成全排列， [m + n for m in 'ABC' for n in 'XYZ']['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
- [具体使用参考](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431779637539089fd627094a43a8a7c77e6102e3a811000)

## 列表生成器 generator
- 好处就是，一个一个的生成，省空间
- 构造方式
- g = (x * x for x in range(10))
- 也可以用yield定义，不太熟悉

## 迭代器 Iterator
- [具体](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000)

##两个属性
- Iterable: list tuple,dict,set,str
- Iterator:genetator
