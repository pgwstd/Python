#统计不同字符的个数。用户从键盘输入一行字符，编写一个程序，统计其中英文字母、空格、数字和其它字符的个数。
s = input('请输入一行字符：')
letters = 0 #英文字母
space = 0   #空格
digit = 0   #数字
others = 0  #其它字符
for c in s:
    if c.isalpha(): #判断是否是字母
        letters += 1
    elif c.isspace():   #判断是否是空格
        space += 1
    elif c.isdigit():   #判断是否是数字
        digit += 1
    else:
        others += 1
print('英文字母个数：{}，空格个数：{}，数字个数：{}，其它字符个数：{}'.format(letters, space, digit, others))