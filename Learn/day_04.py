# TITLE: shebang 与编码声明
# CATEGORY: 脚本基础与环境
#2024.08.26

# NOTE:
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 说明：
# 1) 第一行（shebang）："#!/usr/bin/env python3" 用于类 Unix 系统，告诉系统用哪个解释器来运行此脚本。
#    - 使用 /usr/bin/env 的好处：会在当前环境的 PATH 中查找 python3，便于在不同系统或虚拟环境中运行同一脚本。
#    - 注意：shebang 只有在将脚本设为可执行并直接运行（chmod +x script.py; ./script.py）时才被内核读取；
#      在 Windows 下通常被忽略，但保留无害。
#
# 2) 第二行（编码声明）："# -*- coding: utf-8 -*-" 告诉 Python 和编辑器此文件使用 UTF-8 编码。
#    - 在 Python3 中默认是 UTF-8，但显式声明可以避免某些编辑器或旧环境误读，且在含中文的源文件中是良好实践。
#    - 根据 PEP 263，编码声明必须出现在文件的第一行或第二行（若有 shebang，则放第二行）。
#
# 小结：保留这两行可以提升跨平台与编辑器的兼容性；若你只在 Windows 编辑器中运行，也可以保留以增加可读性。

# 额外说明：
# - shebang 语法：第一行以 "#!" 开头，后面跟解释器路径，例如 "#!/usr/bin/python3" 或 "#!/usr/bin/env python3"。
#   内核在直接执行脚本时会读取这行以决定使用哪个程序来运行脚本。
# - 为什么用 "/usr/bin/env python3"：env 会在当前 PATH 中查找 python3，便于在虚拟环境或不同系统上使用同一脚本；env:environment，环境
# - 直接指定解释器路径（如 "#!/usr/bin/python3"）
#   优点是可移植，缺点是依赖 PATH（在被篡改或含非预期目录时可能选择错误的解释器）。
# - 编码声明（PEP 263）：例如 "# -*- coding: utf-8 -*-" 或 "# coding=utf-8"，必须在文件的第一或第二行出现（若有 shebang 则放第二行），
#   用于告诉解析器如何把源文件字节解码为字符，避免中文等非 ASCII 字符导致错误。
# - Windows 与 py launcher：Windows 通常通过文件关联或显式调用 python.exe；官方的 py launcher（py.exe）会解析 shebang 来选择 Python 版本，
#   因此在 Windows 上保留 shebang 也可能有用。
# - 示范检查命令（类 Unix）：
#   /usr/bin/env python3 -c "import sys; print(sys.executable)"
#   该命令会显示 env 在 PATH 中找到并执行的 python3 的完整路径。
# - 建议：保持文件以 UTF-8 保存，并建议在开发时保留这两行注释，既便于跨平台也便于团队协作。


res=['1',2,3]
# map(str, res) 将列表中的每个元素都转换为字符串，便于拼接
print(''.join(map(str,res)))
print(*res,sep='')  #先解包，再用sep控制分隔符。sep:separator，分隔符
print(*map(str, res), sep='')  #先用map把每个元素转成字符串，再解包，再用sep控制分隔符

print(int('2A',16))   # 2A 是十六进制，2*16 + 10 = 42
print(int('22',8))  # 2*8 + 2 = 18

#占位符：
#%d:整数；%f:浮点数；%s:字符串；%x:十六进制整数
print('%2d-%02d' % (3, 1))  #%2d:至少占2位，右对齐；%02d:至少占2位，不够补0，右对齐
print('%.2f' % 3.1415926)   #.2f:小数点后保留2位
print('your age:%s'%7)
print('%2d'%7)
print(f'{7:2d}')
print('{:.4f}'.format(2/3))
print(f'{2/3:.4f}')
print('{:.4f}'.format(2/3))
print(f'{2/3:.3f}')
print('Hello,{0},I think you is {1:.3f} years old'.format('小明',54.8765))  #{0}、{1}：位置参数,format后传入的参数一次替换字符串内的占位符{0}、{1}
print('Hello,{name},I think you is {age:.3f} years old'.format(name='小明',age=54.8765))
print('%X'%255)
print('%s'%255)
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

last_year_score=input('请输入小明去年的分数：')
this_year_score=input('请输入小明今年的分数：')
print(f'小明去年成绩为{last_year_score}分，今年成绩为{this_year_score}分。')
try:
	last = float(last_year_score)
	this = float(this_year_score)
	if last == 0:
		print('去年成绩为0，无法计算提升百分比。')
	else:
		print(f'小明成绩提升了：{((this - last)/last) * 100:.1f}%')
except ValueError:
	print('输入的成绩不是有效数字，请重新输入。')



