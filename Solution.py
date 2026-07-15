# 1.
# def f(n):
#     for i in range(n):
#         spaces = n-1-i
#         print(" "*spaces,end="")
#         print("*"*(2*i+1),end="")
#         print()
# n=int(input())
# f(n)

# 2.
# def f(n,m):
#     while n>0 and m>0:
#         if n>m:
#             n-=m
#         else:
#             m-=n
#     if n==0:
#         print(m)
#     else:
#         print(n)
# n=int(input())
# m=int(input())
# f(n,m)

# 3.
# def f(n,i):
#     if i<1:
#         return 
#     print(i,end= " ")
#     f(n,i-1)
# n=int(input())
# f(n,n)

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
# def f(arr,n):
#     for i in range(1,n):
#         j = i
#         while j>0 and arr[j-1]>arr[j]:
#             arr[j-1],arr[j]=arr[j],arr[j-1]
#             j-=1
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)
# print(arr)

# 6.
# def f(arr,n):
#     for i in range(1,n+1):
#         if i not in arr:
#             print(i)
#             return
# n=int(input())
# arr=list(map(int,input().split()))
# f(arr,n)

# 7.
# def f(arr,n):
#     left=0
#     right=n-1
#     mid=0
#     while mid<=right:
#         if arr[mid]==0:
#             arr[mid],arr[left]=arr[left],arr[mid]
#             mid+=1
#             left+=1
#         elif arr[mid]==1:
#             mid+=1
#         else:
#             arr[mid],arr[right]=arr[right],arr[mid]
#             right-=1
#     print(arr)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)