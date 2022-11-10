def hanoi(n, A, B, C):
    if n == 1:
        print(A, '-->', C, '', n)
    else:
        hanoi(n - 1, A, C, B)
        print(A, '-->', C, '', n)
        hanoi(n - 1, B, A, C)


hanoi(3, 'A', 'B', 'C')
