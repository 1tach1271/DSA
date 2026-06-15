def pattern(num):
    for i in range(num):
        spaces = (" "*i)
        stars = ("*"*(2*num - 2*i -1))
        print(spaces + stars)

num = 5
pattern(num)