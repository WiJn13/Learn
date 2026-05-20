# TITLE: 重启
# CATEGORY: 重启
# 2026.04.23

a = [1, 2, 3]
b = a.append(5)
print(b)    # None
print(a)    # [1, 2, 3, 5]

# 如果要新的列表，可以使用切片或copy
c = a[:]
c.append(6)
print(c)
print(c.append(7))  # None
d = a.copy()
print(d)
# 如果不写索引，即 a.pop()，默认弹出最后一个（栈逻辑）

e = [2]
e.pop()
print(e)    # []
'''e.pop()
print(e)    # IndexError: pop from empty list'''
try:
    e = e.pop()
except IndexError as m:
    print(m)    # pop from empty list
    print(type(m))  # <class 'IndexError'>
    # IndexError：[术语]：索引错误。意味着给出的“排队序号”超出了当前队伍的实际长度。
# 边界检查 (Boundary Checking)：系统在执行动作前，先确认操作范围是否合法的过程。
# pop 操作前如果不检查 len(list) > 0，就容易触碰边界。

user = {'name': 'Eben', 'OS': 'macOS', 'Encourage': 3}
try:
    version = user['version']
except KeyError as m:
    print(m)    # 'version'
    print(type(m))  # <class 'KeyError'>
    print(repr(m))  # KeyError('version')   #

# 安全取值
version = user.get('version')    
print(version)  # None
version = user.get('version', '3.2.1')
print(version)  # 3.2.1

user = {'name': 'Eben'}
user['OS'] = 'macOS' 
print(user) # {'name': 'Eben', 'OS': 'macOS}
user['name'] = 'WiJn'
print(user) # {'name': 'WiJn', 'OS': 'macOS'}

print(user.keys())
print(user.values())
print(user.items())
a = list(user.items())
print(a)

# 【原理解析：为什么键的顺序改了？】
# 1. Python 3.7+ 的字典严格保持“插入顺序”。
# 2. pop('name') 将原有的键值对从字典剔除。
# 3. 赋值 user['Name'] 相当于插入新键值对，根据特性，它会被追加到字典的最末尾。
user['Name'] = user.pop('name')
print(user) # {'OS': 'macOS', 'Name': 'WiJn'}
print(a)    # [('name', 'Wijn'), ('OS', 'macOS')]

# 【解决方案：使用字典推导式重构字典以保持顺序】
# 遍历原有字典，遇到需要改名的键进行替换，其余保持原样。
user = {'name': 'WiJn', 'OS': 'macOS'} # 恢复原字典结构以便演示
user = {k: v for k,v in user.items()}
print(user) # {'name': 'WiJn', 'OS': 'macOS'}
# 三元表达式: [条件为真时的结果] if [判断条件] else [条件为假时的结果]
user = {'Name' if k == 'name' else k: v for k, v in user.items()}
print(user) # {'Name': 'WiJn', 'OS': 'macOS'}
print(a)    # [('name', 'WiJn'), ('OS', 'macOS')]
