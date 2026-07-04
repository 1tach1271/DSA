# def pattern(n):
#     for i in range(n-1,-1,-1):
#         for j in range(i+1):
#             print(chr(65+j), end="")
#         print()


# n = int(input())
# pattern(n)

# def p(num):
#     a = 0
#     b= int(num**(0.5)) 
#     for i in range(1,b+1):
#         if num%i==0:
#             a+=1
#             if num//i != i:
#                 a+=1
#     if a==2:
#         print("Prime")
#     else:
#         print("Not prime")

# num = int(input())
# p(num)

# def p(arr):
#     arr=arr[::-1]
#     print(arr)
# arr = list(map(int,input().split()))
# p(arr)

# from collections import defaultdict
# def p(arr,n):
#     hash = defaultdict(int)
#     for i in range(n):
#         hash[arr[i]]+=1
#     for a, b in hash.items():
#         print(a,b)
# arr=list(map(int,input().split()))
# n = len(arr)
# p(arr,n)

# def iss(arr,i,n):
#     if i==n:
#         return 
#     j =i
#     while j>0 and arr[j-1]>arr[j]:
#         arr[j-1],arr[j]=arr[j],arr[j-1]
#         j-=1
#     iss(arr,i+1,n)
# arr = list(map(int,input().split()))
# n = len(arr)
# iss(arr,1,n)
# print(arr)

# def m(arr,n):
#     for i in range(1,n+1):
#         if i not in arr:
#             return i

# arr=list(map(int,input().split()))
# n = len(arr)+1
# print(m(arr,n))
# def m(arr,n):
#     a = (n*(n+1))//2
#     b = sum(arr)
#     print(a-b)
# arr=list(map(int,input().split()))
# n = len(arr)+1
# m(arr,n)

# def k(arr,n):
#     m =float('-inf')
#     s=0
#     for i in range(n):
#         s+=arr[i]
#         m = max(m,s)

#         if s<0:
#             s=0
#     print(m)
# arr = list(map(int,input().split()))
# n = len(arr)
# k(arr,n)

# def k(arr,n):
#     m=float('-inf')
#     for i in range(n):
#         s=0
#         for j in range(i,n):
#             s+=arr[j]
#             m=max(s,m)
#     print(m)

# arr = list(map(int,input().split()))
# n = len(arr)
# k(arr,n)