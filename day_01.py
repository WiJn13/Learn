#2025.08.23

name=input('请输入你的姓名：')    #name即为变量。字符串只是提示作用，不会赋值给name。输入的内容才为name的内容
print(f'请相信自己！可爱的{name}')    #当用户输入之后，输入的内容就是"name"
print('hello,',name)



a=input('输入你的出生年份：')
if a.isdigit():
    a=int(a)
    print(f'恭喜你今年{2025-a}岁啦！')


a='123'
input('a')
print(a.isdigit())

print(1+2+3)

print('hello\rworld')
    #\：转义符。\r：回车（return）；\\：一个反斜杠（\）
    # \n：换行（new line)；\b：回退（backspace）；\t：制表符（tab）

print('''abc
defg
hijk''')    #'''...'''换行
print(r'''hello,    #不受r(raw)控制
good''')

print(r'''hello,\nworld #\n受r控制
good''')    

print('**good'.lstrip('*')) #leftstrip()：丢掉左边的

a='*#good##*'
if a[1]=='#':
    a=a[0:3]+a[5:]
print(a)    # *#gd##*

10/3    #没有赋值或打印，输出结果不会包含这个结果
print(10/3)
print(10/3)    #3.3333333333333335
print(10/3)    #3.3333333333333335


