# TITLE: match/case 与 for 循环
# CATEGORY: Python基础
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

total = 0
for x in [1,2,3]:
    total = total + x
print(total)

print(range(5))
my_list= list (range(5))   # 不包括5
print(my_list)

total = 0
for x in my_list :  # list写成range(5)也可以
    total = total + x
print(total)

total = 0
for x in (range(101)):
    total = total + x
print(total)

total = 0
num = input ('请输入累加到几：')
if num.isdigit():
    num = int(num)
while num > 0:
    total = total + num
    num = num-1
print(total)

total = 0
n = 99
while n > 0 :
    total = total + n
    n = n-3 # 每3步累加一次
    print(total) # print应该写最前面才是累加结果；如果写在这个缩进这里，会打印每一次累加的值。在循环内部打印会显示每次累加的中间结果；如果想要只显示最终累加结果，应将 print 放在循环结束后。

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(f'Hello,{x}')    # 逐个问候

print(f'Hello,{L[0]}') # 单个问候   


L = ['Bart', 'Lisa', 'Adam']
for x in L:  
    print('Hello,%s!'%x)   #逐个问候

L = ['B','A','D']
match L:
    case L:     # 这两行累赘
        print('Hello,'+'-'.join(L))    # 列表元素拼接

n=1
total = 0
while n < 100 :
    if n > 9:
        break
    total = total + n
    n = n+1
print(total)     # 从1加到9

n = 11
total = 0
while n > 0 :   
    total = total+n   
    n = n-1
print(total)     # 从1加到11

s=sum (range(1,11))
print(s)   # 从1加到10

n = 0
while n < 10 :
    n = n + 1
    if n % 2 == 0 : 
        continue    # 1，不continue，输出；到2，continue，不输出。
    print(n)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1   # 先打印再进入循环。输出为1-10
print('END')

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    n = n + 1
    print(n)    # 少个1，多个11。11先打出来再进入循环判断
print('END')
'''实际编程中尽量少用 continue 和 break '''

# 写一个死循环程序：
RUN_DEMO = False    # False 表示跳过
                    # RUN_DEMO 只控制紧跟在后面的if同级
if RUN_DEMO:
    n = 0
    while n < 1 :
        n = n - 1
        print(n)
# ctrl + c , 退出程序

# 以下代码与上个if同级，不受RUN_DEMO开关控制
m = {
    'WangYibin':75,
    'HuJinsheng':73,
    'HuangLin':85
    }   #字典
print(m['WangYibin'])  #查找
# {key:value}, key可以为 tuple，str，int，float，bool, 不可变
m = {85:27,
     98:65,
     28:65
     }
print(m[98])   # 65
print(28 in m)
print(m.get(13))   # 通过dict提供的 get()方法调用，如果key不存在，返回None，或者自己指定的。
print(m.get(77,63))  # 63

