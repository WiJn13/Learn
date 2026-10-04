# TITLE: 重启
# CATEGORY: 重启
# 2026.04.18

s = 'abcdefg'
part1 = s[1:4]
print({part1})

part2 = s[::2]
print(s)

import logging

logging. basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def system_self_check():
    status = 'Active'
    user_input = input('请输入你的学习目标：').strip()

    if not user_input:
        logging.warning('输入为空，系统将使用默认参数')
        user_input = '全面复习'

    print(f'[系统自检]状态：{status} | 目标：{user_input}')
if __name__ == '__main__':
    system_self_check()

my_list = ['macOS', 'VSCode', 'Python', 'Terminal', 'Git']
result = my_list[0:3]

print(f'原始：{my_list}')
print(f'提取后：{result}')

jump_result = my_list[0::2]
print(f'跳跃提取结果:{jump_result}')

my_list.append(3)
my_list_1 = my_list.insert(2,5)
my_list_2 = my_list.remove(3)   # remove和inset，append，都不返回，直接原内存地址修改，不能赋值给别人，返回None
                                # 也就是，my_list盒子没有改变，拿my_list_1是个空的
del my_list[1]
my_list[3] = 8
print(my_list)
print(my_list_1)    # None

tasks = ['写代码', '修Bug']
tasks.append('提交测试')
tasks[0] = '设计架构'
a = tasks.pop(2)
print(tasks)
print(a)    # ‘提交测试‘被pop并返回保存，内存里有，所以赋值给a的是‘提交测试‘

tasks.pop(0)
tasks.pop(0)

print(tasks)

names = ['WiJn', 'Eben']
for name in names:
    name = name.upper()
print(names)    # ['WiJn', 'Eben']，遍历的元素赋值给了name
print(name) # EBEN，WiJn变成WIJN，赋值给name，再把Eben变成EBEN，赋值给name，name最后变成EBEN（字符串）
names = ['WiJn', 'Eben', 'Mac']
for i in range(len(names)):
    names[i] = names[i].upper()
print(names)
