def pattern(arr):
    arr[:]=arr[::-1]
    
arr = list(map(int,input("Enter the array").split()))
pattern(arr)
print(arr)