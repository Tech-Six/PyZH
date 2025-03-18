# -*- coding: utf-8 -*-
"""
数值运算 - Python数值运算函数的中文封装

abs()     & 绝对值()
divmod()  & 商余()
round()   & 四舍五入()
pow()     & 幂运算()
max()     & 最大值()
min()     & 最小值()
sum()     & 求和()
bin()     & 二进制()
oct()     & 八进制()
hex()     & 十六进制()
complex() & 复数()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""


def 绝对值(数字):
    """
    参数:
        数字 (number): 要取绝对值的数字。
    示例:
        绝对值(-5)  # 返回 5
    返回值:
        number: 数字的绝对值。
    """
    return abs(数字)


def 商余(被除数, 除数):
    """
    返回:
        包含商和余数的元组 (商, 余数)。
    """
    return divmod(被除数, 除数)


def 四舍五入(数字, 小数位数=None):
    """
    将数字四舍五入到指定的小数位数。
    
    参数:
        数字: 要四舍五入的数字。
        小数位数: 要保留的小数位数，默认为None（四舍五入到最接近的整数）。
    
    示例:
        四舍五入(3.14159)  # 返回 3
        四舍五入(3.14159, 2)  # 返回 3.14
        四舍五入(3.5)  # 返回 4
    
    返回:
        四舍五入后的数字。
    """
    return round(数字, 小数位数)


def 幂运算(底数, 指数, 模数=None):
    """
    返回底数的指数次幂，如果提供了模数，则返回幂对模数取余的结果。
    
    参数:
        底数: 底数。
        指数: 指数。
        模数: 可选的模数，用于取余。
    
    示例:
        幂运算(2, 3)  # 返回 8，即 2³
        幂运算(2, 3, 5)  # 返回 3，即 2³ % 5
    
    返回:
        幂运算的结果。
    """
    return pow(底数, 指数, 模数)


def 最大值(*参数, 默认值=None, 键=None):
    """
    返回参数中的最大值，或者可迭代对象中的最大项。
    
    参数:
        *参数: 要比较的值，或者单个可迭代对象。
        默认值: 如果可迭代对象为空，返回的默认值。
        键: 用于从每个元素中提取比较值的单参数函数。
    
    示例:
        最大值(1, 2, 3, 4, 5)  # 返回 5
        最大值([1, 2, 3, 4, 5])  # 返回 5
        最大值('a', 'b', 'c')  # 返回 'c'
        最大值(['apple', 'banana', 'cherry'], 键=len)  # 返回 'banana'，因为它的长度最大
    
    返回:
        最大值。
    """
    if len(参数) == 1 and isinstance(参数[0], (list, tuple, set)):
        return max(参数[0], key=键) if 默认值 is None else max(参数[0], default=默认值, key=键)
    return max(参数, key=键) if 默认值 is None else max(参数, default=默认值, key=键)


def 最小值(*参数, 默认值=None, 键=None):
    """
    返回参数中的最小值，或者可迭代对象中的最小项。
    
    参数:
        *参数: 要比较的值，或者单个可迭代对象。
        默认值: 如果可迭代对象为空，返回的默认值。
        键: 用于从每个元素中提取比较值的单参数函数。
    
    示例:
        最小值(1, 2, 3, 4, 5)  # 返回 1
        最小值([1, 2, 3, 4, 5])  # 返回 1
        最小值('a', 'b', 'c')  # 返回 'a'
        最小值(['apple', 'banana', 'cherry'], 键=len)  # 返回 'apple'，因为它的长度最小
    
    返回:
        最小值。
    """
    if len(参数) == 1 and isinstance(参数[0], (list, tuple, set)):
        return min(参数[0], key=键) if 默认值 is None else min(参数[0], default=默认值, key=键)
    return min(参数, key=键) if 默认值 is None else min(参数, default=默认值, key=键)


def 求和(可迭代对象, 起始值=0):
    """
    对可迭代对象中的元素求和。
    
    参数:
        可迭代对象: 包含要求和的元素的可迭代对象。
        起始值: 求和的起始值，默认为0。
    
    示例:
        求和([1, 2, 3, 4, 5])  # 返回 15
        求和([1, 2, 3], 10)  # 返回 16，即 10 + 1 + 2 + 3
    
    返回:
        求和的结果。
    """
    return sum(可迭代对象, 起始值)


def 二进制(整数):
    """
    将整数转换为二进制字符串，前缀为'0b'。
    
    参数:
        整数: 要转换的整数。
    
    示例:
        二进制(10)  # 返回 '0b1010'
        二进制(42)  # 返回 '0b101010'
    
    返回:
        表示二进制的字符串。
    """
    return bin(整数)


def 八进制(整数):
    """
    将整数转换为八进制字符串，前缀为'0o'。
    
    参数:
        整数: 要转换的整数。
    
    示例:
        八进制(10)  # 返回 '0o12'
        八进制(42)  # 返回 '0o52'
    
    返回:
        表示八进制的字符串。
    """
    return oct(整数)


def 十六进制(整数):
    """
    将整数转换为十六进制字符串，前缀为'0x'。
    
    参数:
        整数: 要转换的整数。
    
    示例:
        十六进制(10)  # 返回 '0xa'
        十六进制(42)  # 返回 '0x2a'
    
    返回:
        表示十六进制的字符串。
    """
    return hex(整数)


def 复数(实部, 虚部=0):
    """
    创建一个复数。
    
    参数:
        实部: 实部值或包含复数的字符串。
        虚部: 虚部值，如果实部是字符串则忽略。
    
    示例:
        复数(3, 4)  # 返回 (3+4j)
        复数('3+4j')  # 返回 (3+4j)
    
    返回:
        复数。
    """
    if isinstance(实部, str):
        return complex(实部)
    return complex(实部, 虚部)