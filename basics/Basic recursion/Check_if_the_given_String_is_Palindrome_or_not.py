def pattern(arr):
    arr1=[]
    arr1 = arr[::-1]
    if arr1==arr:
        print("Palindrome")
    else:
        print("Not Palindrome")
arr = list(map(str, input("Enter the arr:- ")))
pattern(arr)