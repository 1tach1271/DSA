# def f(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*",end="")
#         print()

# n=int(input())
# f(n)
# import math
# def f(n):
#     if n==0:
#         return 1
#     n=abs(n)
#     count=int(math.log10(n)+1)
#     return count
# n = int(input())
# print(f(n))

# def f(n):
#     if n ==0:
#         return 1
#     return n*f(n-1)

# n=int(input())
# print(f(n))

# from collections import defaultdict
# def f(arr,n):
#     a=defaultdict(int)
#     for i in range(n):
#         a[arr[i]]+=1
#     for a,b in a.items():
#         print(a,b)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# def f(arr,n):
#     for i in range(n-1,-1,-1):
#         for j in range(i):
#             if arr[j+1]<arr[j]:
#                 arr[j+1],arr[j]=arr[j],arr[j+1]
#     print(arr)

# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# def f(arr1,n):
#     a=0
#     for j in range(1,n):
#         if arr1[j]!=arr1[a]:
#             a+=1
#             arr1[a]=arr1[j]
#     print(arr1)
# arr1=list(map(int,input().split()))
# n=len(arr1)
# f(arr1,n)

# def f(arr,n):
#     low=0
#     mid=0
#     high=n-1
#     while mid<=high:
#         if arr[mid]==0:
#             arr[low],arr[mid]=arr[mid],arr[low]
#             low+=1
#             mid+=1
#         elif arr[mid]==1:
#             mid+=1
#         else:
#             arr[mid],arr[high]=arr[high],arr[mid]
#             high-=1
#     print(arr)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

