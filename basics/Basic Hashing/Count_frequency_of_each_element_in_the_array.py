from collections import defaultdict
def pattern(arr,n):
    hash = defaultdict(int)
    for i in range(n):
        hash[arr[i]]+=1
    for a,b in hash.items():
        print(a,b)
arr = list(map(int, input("Enter the array").split()))
n = len(arr)
pattern(arr,n)