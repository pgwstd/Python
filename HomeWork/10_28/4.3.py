# 最大公约数计算。从键盘接收两个正整数，编写程序求出这两个整数的最大公约数和最小公倍数。

def gcd(x, y):  # 求最大公约数
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):  # 求最小公倍数
    return x * y // gcd(x, y)

if __name__ == '__main__':
    x = int(input('x = '))
    y = int(input('y = '))
    print('%d 和 %d 的最大公约数是 %d' % (x, y, gcd(x, y)))
    print('%d 和 %d 的最小公倍数是 %d' % (x, y, lcm(x, y)))
