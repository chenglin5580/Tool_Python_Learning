# Class and Instance

[TOC]

## 类和实例



## 访问限制
- 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
- 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法
- 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：


## 继承
继承一个类：
如果已经定义了Person类，需要定义新的Student和Teacher类时，可以直接从Person类继承：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
定义Student类时，只需要把额外的属性加上，例如score：

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

