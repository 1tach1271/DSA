# 1.
# def pattern(num):
#     for i in range(num):
#         if i%2==0:
#             v = 1
#         else:
#             v = 0
#         for j in range(i+1):
#             print(v, end = "")
#             v= 1-v
#         print()
# num= int(input())
# pattern(num)

# 2.
# def pattern(num):
#     l=len(str(num))
#     a=0
#     n=num
#     while n>0:
#         last_digit = n%10
#         a= last_digit**l + a
#         n=n//10
#     if a ==num:
#         print("Armstrong number")
#     else:
#         print("Not an Armstrong number")
# num = int(input())
# pattern(num)

# 3.
# def f(n):
#     if n==1:
#         return 1
#     return n + f(n-1)
# n=int(input())
# print(f(n))

# 4.
# from collections import defaultdict
# def f(arr,n):
#     h=defaultdict(int)
#     for i in range(n):
#         h[arr[i]]+=1
#     for a,b in h.items():
#         print(a,b)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# 5.
# def b(arr,n):
#     if n==1:
#         return 
#     for j in range(n-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#     b(arr,n-1)
# arr=list(map(int,input().split()))
# n=len(arr)
# b(arr,n)
# print(arr)

# 6.
# def f(arr,n):
#     c=0
#     m=0
#     for i in range(n):
#         if arr[i]==1:
#             c+=1
#         else:
#             c= 0
#         m=max(c,m)
#     print(m)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# 7.
# def p(arr,n,k):
#     a=sorted(arr)
#     left =0
#     right = n-1
#     while left<right:
#         if a[left]+a[right] >k:
#             right-=1
#         elif a[left]+a[right]<k:
#             left+=1
#         elif a[left]+a[right]==k:
#             return "Yes"
#     return "NO"
# def m(arr,n,k):
#     a={}
#     for i , num in enumerate(arr):
#         x=k-num
#         if x in a:
#             return [a[x],i]
#         a[num]=i 
#     return [-1,-1]
# arr=list(map(int,input("Enter the array: ").split()))
# n = len(arr)
# k=int(input("Enter the number sum: "))
# print(m(arr,n,k))
# print(p(arr,n,k))