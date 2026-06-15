def pattern(num):
    for i in range(num):
        spaces = (" "*(num - i -1))
        stars = ("*"*(2*i +1))
        print(spaces + stars)
    for i in range(num):
        spaces = (" "*i)
        stars = ("*"*(2*num - 2*i -1))
        print(spaces + stars)

num = 5
pattern(num)