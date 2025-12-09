# TITLE: 使用元类
# CATEGORY: 面向对象高级编程
class Hello(object):
    def hello(self, name='world'):  # 设置函数参数默认值，等号前后不空格
        print('Hello, %s.' % name)

h = Hello()
h.hello()   # Hello, world.

print(type(Hello))  # <class 'type'>
print(type(h))  # <class '__main__.Hello'>，
#   h = Hello()  是类 Hello 的实例
#   实例对象的类型就是它归属的类

