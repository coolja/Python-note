"""
多行注释
"""
print("hello world")
# TODO 用于标记位置
print("hello python")

# 单行注释(快捷键：ctrl+/)

"""
算术运算：
+，-，*，/，//（相除后整数部分）
%（相除后余数部分），**（a**b==a^b，优先级最高）
"""
#命名规则与c一样
r=4
pi=3.14
area=pi*r**2
print(area)

temp=1
t=type(temp)
#type():显示数据类型但无打印功能
print(t)

temp=2.21
t=type(temp)
print(t)

temp="you"
t=type(temp)
print(t)

#字符串运算与java一样print(str1+str2),只能字符串变量与字符串变量相加
#tmp=15
str="hello python"
#print(str+tmp)    报错
print(str*3)
#表示将hello python重复输出三遍

#输出
age=18
print("年龄为：%d"%age)

name="张三"
age=18
height=1.8888
print("姓名为%s，年龄为：%d,身高为%.2f"%(name,age,height))

#输入（接收默认为字符串类型）
#age=input()
#print("age="+age)

#age=input("请输入你的年龄：")#input("提示信息")
#print("age="+age)



#if
a=1
if a==1:
    print("进入if")

#if...else...
a=1
b=3
if a<b:
    print("进入if...else...(if)")
else:
    print("进入if...else...(else)")

#if...elif...else...
x=2
y=4
z=0
if x<y and x<z:
    print("进入if...elif...else...（if）")
elif y<z:
    print("进入if...elif...else...（elif）")
elif y<x:
    print("进入if...elif...else...（elif）")
else:
    print("进入if...elif...else...（else）")

#超长行处理(\)
if x==2and x==2 and x==2and x==2and x ==2and x==2and x==2and x==2 and \
    x==2and x==2and x ==2and x==2 and x==2 and x==2and x==2 and x ==2and \
    x==2 and x==2 and x==2and x==2and x ==2and x==2:
    x=1
#函数定义
def ok(a):
    """文档注释：判断a是否为1"""
    if a==1:
        print("ok")
#ctrl+鼠标移到函数位置即可看到函数注释
ok(1)

#定义类
class Dog:
    def __str__(self):
        """魔术方法"""
        return "狗狗"
    def __init__(self):
        """狗的成员变量"""
        self.type="柴犬"
        self.name="旺柴"
        self.age=3
        self.sex=None

    def hello(self):
        """狗的成员方法(无参数)"""
        print("旺柴对你笑了一下")
    def run(self,meter):
        """狗的成员方法(含参数)"""
        print("旺柴跑了%d米"%meter)
    def introduce(self):
        print("种类："+self.type+" 名字："+self.name)

Mydog=Dog()
print(Mydog)#调用魔术方法
Mydog.sex="公"
print("性别是："+Mydog.sex)
Mydog.introduce()
Mydog.hello()#无参方法调用
Mydog.run(15)#含参方法调用


#实现封装（可在类内可视，类外不可视）
class Card:
    def __init__(self):
        self.id="A001"
        self.__pwd="123"#双下划线即实现封装
    def comp(self,p):
        if p==self.__pwd:
            return 1
        else:
            return 0
c1=Card()
# p=input("请输入密码")
# flag=c1.comp(p)
# if flag==1:
#     print("密码正确")
# else:
#     print("密码错误")


#init传参
class NDog:
    def __init__(self,type,name):
        """狗的成员变量"""
        self.type=type
        self.name=name
    def print(self):
        print("种类是："+self.type+" 名字是："+self.name)
d1=NDog("柴犬","旺柴")
d1.print()


#类变量
class NNDog:
    subjuct="狗"#类变量（不允许使用对象名修改，只能用类名修改）
    def __init__(self,type,name):
        """狗的成员变量"""
        self.type=type#实例变量
        self.name=name
d2=NNDog("柴犬","旺柴")
print(NNDog.subjuct)
d2.subjuct="狗类"#修改失败
NNDog.subjuct="狗狗"
print(NNDog.subjuct)


#类方法（类方法中无法调用实例成员）
class NDog:
    @classmethod#类方法函数
    def show(cls):
        print("我是汪星人")
        #print(self.name)
#报错，找不到self对象，即使增加参数self也无法调用self的成员，因为此处的self与实例对象self不是一个self

    def __init__(self):
        """狗的成员变量"""
        self.type="柴犬"
        self.name="旺柴"
    def print(self):
        print("种类是："+self.type+" 名字是："+self.name)

#静态方法（可当函数使用）
class test:
    @staticmethod
    def show():
        print("hello")
def show():
        print("hello")
show()

#继承（规则与java一致）
class ob:
    def tshow(self):
        print("test")

class Animal:
    def fshow(self):
        print("我是父类")
    def show(self):
        print("我是动物")

class Cat(Animal,ob):

    def sshow(self):
        print("我是子类")
    def show(self):
        #调用被覆盖的父类方法
        Animal.show(self)  # 1
        super(Cat, self).show()#2
        super().show()#3
        print("我是猫")

class bosi(Cat):
    def ssshow(self):
        print("我是子子类")
    def show(self):
        print("我是波斯猫")
class cup(Cat):
    def tsshow(self):
        print("我是茶杯猫")
c=Cat()
c.fshow()
c.sshow()

c2=cup()
c2.tshow()#一个类可以有多个子类
c.tshow()#一个类可以有多个父类（接口）

c.show()#实现cat子类重写animal父类中的show方法
c1=bosi()
c1.show()#实现bosi子类重写cat父类中的show方法

#print(bosi.__mro__)#查看继承关系

#(<class '__main__.bosi'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)
#bosi继承Cat，Cat继承Animal

#鸭子类型
class teacher:
    def teach(self):
        print("教数学")
class man:
    def teach(self):
        print("教生活常识")
class gameplayer:
    def teach(self):
        print("教打游戏")
class demo:
    def do(self,ok):
        ok.teach()
d=demo()
m=man()
p=gameplayer()
t=teacher()
d.do(m)
d.do(p)
d.do(t)


