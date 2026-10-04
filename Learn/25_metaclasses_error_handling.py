# TITLE: 使用元类，错误处理
# CATEGORY: 面向对象高级编程
# 2025.12.01
def fn(self, name='world'): # 给的默认值是world
    print('Hello, %s.' % name)
Hello = type('Hello', (object,),dict(hello=fn)) # 创建Hello class
# type(类名字符串, 父类元组, 属性字典)
'''
    1.	type(...) 根据你给的三个参数，创建了一个新的类对象；
	2.	这个类的名字叫 "Hello"，继承自 object，有一个方法 hello；
	3.	然后把这个类对象赋值给变量 Hello。
'''
h = Hello()
h.hello()   # Hello, world.
h.hello('Python')   # Hello, Python.
print('--- 分割线 ---')
print('Hello =', Hello)
print('type(Hello) =',type(Hello))  # <class 'type'>
print('type(h) =', type(h))  # <class '__main__.Hello'>
print('h.__class__ =', h.__class__) # 创造出h的类
print(type(h) is h.__class__)   # True


class ListMetaclass(type):
    '''	•	说明：这是一个“类的类”
	    •	它自己是个类（普通类），但专门用来“造别的类”
	    •	必须继承 type, 因为 type 是 Python 内置的“元类基类”
        '''
    def __new__(cls, name, bases, attrs):
        print('创建类前 sttrs =', attrs)
        attrs['add'] = lambda self, value: self.append(value)
        print('创建类后 attrs =', attrs)
        #   dict[key] = value 的语法，就是“给这个 key 赋一个 value”
        #   所以这里的 [] 不是“列表”，而是 “下标/键访问运算符”，看用在谁身上：
	    #   用在 list 上：lst[0] 是取第 0 个元素；
	    #   用在 dict 上：d['x'] 是取键 'x' 对应的值；
	    #	用在赋值左边：d['x'] = 1 就是给这个 key 指定一个 value。

        #   这是元类里最关键的方法：当解释器要创建一个类时，会先调用这个 __new__
	    #   4 个参数的意义：
	    #   cls：当前这个元类本身（这里就是 ListMetaclass）
	    #	name：即将被创建的类名（比如 'MyList'）
	    #	bases：这个类继承的父类们（一个元组，例如 (list,)）
	    #	attrs：这个类里定义的属性和方法组成的字典，比如：
        #   { '__module__': '__main__', '__qualname__': 'MyList', ... }

        return type.__new__(cls, name, bases, attrs)
        #	最后仍然调用 type.__new__ 真正把这个类对象造出来
		#   只是我们在造之前，对 attrs 做了“加工”

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add('A')
print('L =', L)
print('type(L) =', type(L))
print('type(MyList) =', type(MyList))

try:
    s = input('输入一个整数：')
    n = int(s)  # 可能ValueError
    r = 10 / n  # 可能ZeroDivisionError
except ValueError as e:
    print('数值错误：', e)
except ZeroDivisionError as e:
    print('除数不能为0：', e)
else:
    print('结果为：', r)
finally:
    print('本次计算结束')

