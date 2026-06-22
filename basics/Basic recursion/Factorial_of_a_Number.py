def pattern(num):
    if num<1:
        return 1
    return num * pattern(num-1)
if __name__ =="__main__":
    num =int(input("Enter the number:-  "))
    print(pattern(num))