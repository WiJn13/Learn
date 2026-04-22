# TITLE: 字符串操作与进制转换
# CATEGORY: Python基础
#2025.08.24

n='123#'
print(f'{n}')
print('Hello,\nBob!')
n='123#'
print(f'{n}')
print('Hello,\nBob!')
print('''Hello,
Bob''')

s='abcdefg'
s=s[::2]    #切片可用于字符串、列表、元组等序列类型, 不能用于整数
print(s)    #aceg

# 字符串是不可变的, 不能直接改某个位置的字符, 如: 
try:
    s='hello' 
    s[0]='H'    #错误示例, 字符串不可变，不能通过索引赋值，会导致 TypeError
    print (s)
except:    #忽略错误
    pass

s='hello'
s='H'+s[1:]    #Hello 
print(s)    #Hello

s[::1]    #意思是,[ start:stop:step ]。空值不是0也不是最后的那个数, 空值就是空值。
s[1::1]   #ello, 包括最后一个字符, 因为空值不是最后一个数
s[1:5:1]  #ello, 不包括最后一个字符


def dec_to_bin (num):
    bits=[]
    while num>0:
        bits.append (str (num%2))
        num//=2
    return ''.join (bits[::-1]) or '0'
print(dec_to_bin (10))

def base_convert (num_str,from_base,to_base):
    """
    Convert a number string from one base to another.
    Supports up to base 36 (digits 0-9 and A-Z).
    """
    if to_base > 36 or to_base < 2:
        raise ValueError("to_base must be between 2 and 36 (inclusive)")
    num=int (num_str,from_base)
    digits='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'   #给个字典, 后面从字典中取
    if num==0:
        return '0'
    
    res=[]
    while num>0:
        res.append (digits[num%to_base])
        num//=to_base
    return ''.join (res[::-1])
print(base_convert ('745',8,16))

print(chr (20013)+chr (25991))    #中文

print(int ('2A',16))   #42

# 注释或定义正无穷: 用于笔记或作为哨兵, 避免调用未定义的 inf()
inf = float ('inf')  # 无限大（正无穷）
print(float ('inf'))    #inf, 正无穷
print(float ('-inf'))   #-inf, 负无穷
# 尝试把非数字字符串转换为 float 会抛出 ValueError, 下面用 try/except 保持笔记同时避免崩溃
try:
    print(float ('wang'))    # wang, 不是数字
except ValueError:
    print ("'wang' 不是有效的数字, 无法转换为 float")


res=['a','b','c','d']
print(''.join (res))    #.join拼接
print('-'.join (res))
print(''.join (str (x) for x in res))
print(''.join (map (str,res)))    #map(str,res)把每个元素转成字符串
print(*res,sep='')    #*解包, sep控制分隔符
print(*res,sep='-')   #a-b-c-d

res=['1',2,3]
print(''.join (map (str,res)))
print(*res,sep='')
print(*map (str, res), sep='')

print(int ('2A',16))   #42
print('END')

# note:
'''
ASCII 码: 一个英文字母 (不分大小写) 通常占 1 个字节。ASCII 使用 8 位二进制表示字符, 取值范围通常为十进制 -128 到 127, 一个 ASCII 码占 1 个字节。

UTF-8 编码: 英文字符通常占 1 字节, 中文字符 (含繁体) 通常占 3 字节；中文标点通常占 3 字节, 英文标点占 1 字节。

Unicode 编码: Unicode 把多种语言统一到一套编码, 常见实现为 UTF-16 (UCS-2/UTF-16) 等, 字符占用的字节数依实现而异；在 UTF-16 中常用字符可用 2 字节表示, 但也存在需要使用 4 字节的情况。

中国常见的国家标准编码包括 GB2312 等。

UTF-8 会根据 Unicode 码位把字符编码为 1 至 6 个字节: 常用英文字母为 1 字节, 常用汉字通常为 3 字节, 较生僻的字符可能需要 4 到 6 字节。如果文本包含大量英文, 使用 UTF-8 可节省空间。

B 与 bit:
数据存储以“字节"(Byte, 简写为B) 为单位, 数据传输常以“位"(bit, 简写为b) 为单位。1 个 bit 表示一个二进制位 (0 或 1), 8 个 bit 组成 1 个字节 (1 byte = 8 bit)。

常用单位:
1 KiB (kibibyte) = 1024 byte
1 KB (kilobyte) = 1000 byte
1 MiB (mebibyte) = 1024 * 1024 byte = 1 048 576 byte
1 MB (megabyte) = 1 000 000 byte

进制说明: 十进制 (decimal), 二进制 (binary), 八进制 (octal), 十六进制 (hexadecimal)
'''

'''进制转化: 
int(num_str,from_base) #转化为十进制 
bin(num) #十进制转换为二进制 
hex(num) #十进制转十六进制 
oct(num) #十进制转八进制 
chr(num) #数字转字符。character: 字符
ord(char) #字符转数字。ordinal: 序数
b'ABC'.hex() #字节转十六进制字符串。
bytes.fromhex('616263') #十六进制字符串转字节
'''
