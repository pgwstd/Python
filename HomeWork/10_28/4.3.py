# 最大公约数计算。从键盘输入两个正整数，计算并输出它们的最大公约数和最小公倍数。

def gcd(x, y):
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)

if __name__ == '__main__':
    x = int(input('x = '))
    y = int(input('y = '))
    print('%d 和 %d 的最大公约数是 %d' % (x, y, gcd(x, y)))
    print('%d 和 %d 的最小公倍数是 %d' % (x, y, lcm(x, y)))
