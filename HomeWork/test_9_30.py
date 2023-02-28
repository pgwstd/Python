import math

print(pow(2, 10))  # 指数函数
a = 3.1415926535333334944
print(a)  # 只会打印到小数点的后16位
print(100 / 3)
print(100 // 3)
b = -23
print(abs(b))  # abs是获取某个数的绝对值
n = 2
m = 7
k = 3.14159
print(divmod(m, n))  # 返回一个元数组（第一个数是它的商，第二个数是它的元数组）
print(divmod(8, 4))
print(round(k, 2))  # round保留多少位小数
print(max(3, 5, 1, 8, 4, 9))  # max返回这个数组里的最大值
print(max(n, m, b))
print(min(3, 5, 1, 8, 4, 9))  # min返回这个数组里的最小值
pi = math.pi
print(pi)
print(math.e)
print(math.inf)
print(math.nan)
x = -32
print(math.fabs(x))
print(math.fmod(20, 3))  # 返回x与y的模(余数)
print(math.fsum([3.14, 2.2, 3.22]))  # math.fsum浮点数精确求和
print(math.ceil(3.5))  # 浮点数math.ceil向上取整
print(math.floor(3.5))  # 浮点数math.floor向下取整
print(math.factorial(3))  # math.factorial返回一个数的阶乘
print(math.gcd(30, 12))  # math.rcd返回x,y中的最大公约数
print(math.frexp(12))
print(math.ldexp(1, 2))
print(math.modf(12.5))  # math.modf返回小数和整数部分
print(math.trunc(12.5))  # math.trunc返回这个小数的整数部分
print(math.copysign(3, 6))
print(math.isclose(3, 4))  # math.isclose比较两个的相似性，如果一样返回true，如果假返回false
print(math.isfinite(36))  # 判断x是否是无穷大，如果不是返回true如果是返回false
print(math.isinf(36))
print(math.isnan(36))
print(pow(3, 2))
print(math.exp(3))
print(math.expm1(3))
print(math.sqrt(9))
print(math.log(3, 3))
print(math.log1p(3))
print(math.log2(3))
print(math.log10(3))
