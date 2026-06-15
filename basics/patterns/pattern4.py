def pattern(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(i , end=" ")
        print()

num = 5
pattern(num)