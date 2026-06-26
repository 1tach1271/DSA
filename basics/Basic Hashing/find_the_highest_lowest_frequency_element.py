from collections import defaultdict
def pattern(arr,n):
    hash = defaultdict(int)
    maxcount = 0
    minelement=0
    maxelement=0
    for i in range(n):
        hash[arr[i]]+=1
    for a,b in hash.items():
        if b> maxcount:
            maxcount = b
            maxelement = a
        if b< n:
            n = b 
            minelement = a
    print(maxelement)
    print(minelement)
arr = list(map(int, input("Enter the array").split()))
n = len(arr)
pattern(arr,n)