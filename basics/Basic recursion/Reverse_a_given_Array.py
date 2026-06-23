def pattern(arr):
    arr[:]=arr[::-1]
if __name__=="__main__":
    arr = list(map(int,input("Enter the array").split()))
    pattern(arr)
    print(" ".join(map(str,arr)))