def pattern(num):
    for i in range(num):
        for j in range(1):
            print(" "*(num - i -1), "*"*(2*i + 1), " "*(num - i -1), end = " ")
        print()
num = 5
pattern(num)