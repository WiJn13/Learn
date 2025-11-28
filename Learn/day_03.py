# TITLE: 字符编码、bytes 与进制
# CATEGORY: 字符编码与进制
#2025.08.25

print(ord('中'))
print(ord('A'))
print(chr(20013))
print(chr(65))
print(b'ABC'.hex())
print(bytes.fromhex('616263'))
print(bytes.fromhex('112233'))

names=['Walter','简','胡']
print(f'这{len(names)}个人是好朋友')    #大括号要包含len()，len()才有效
print('good\bse')

def base_convert(num_str,from_base,to_base):    #注意冒号
    num=int(num_str,from_base)    #先用自带的规则转成十进制.int(num,from_base)
    digits='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'   #给个字典，后面从字典中取
    if num==0:    #注意冒号
        return'0'
    res=[]
    while num>0:    #注意冒号
        res.append(digits[num%to_base])    #num除以目标进制 的余数，再append一下
        num//=to_base    #num地板除目标进制，并赋值。用while语句就可以一直循环直到num=0
    return''.join(res[::-1])
    return''.join(reversed(res))
print(base_convert('10',10,2))    #print的是这个变量，算法算的是这个变量的内容

print(bin(7))   # bin() 只接受一个整数参数，将其转换为二进制字符串；不像 int() 可以指定进制，bin() 不接受 base 参数。
print(int(90))  # 将数字 90 转换为整数类型并输出，int() 用于类型转换

'''不要忘记冒号！！！'''

