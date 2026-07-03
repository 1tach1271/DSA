# def pattern(num):
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print(i,end="")
#         print()
# num = int(input())
# pattern(num)

# def p(num):
#     a = num
#     l=0
#     b=0
#     while a>0:
#         b = a%10
#         l = l*10 + b 
#         a = a//10
#     if l ==num:
#         print("Palindrome Number")
#     else:
#         print("Not Palindrome")
# num = int(input())
# p(num)

# def p(a,n):
#     if n==0:
#         return
#     print(a,end=" ")
#     p(a,n-1)
# a = input()
# n = int(input())
# p(a,n)
# from collections import defaultdict
# def p(arr,n):
#     mxc=0
#     mic=n
#     me =0
#     mi =0
#     hash = defaultdict(int)
#     for i in range(n):
#         hash[arr[i]]+=1
#     for a , b in hash.items():
#         if b>mxc:
#             mxc =b 
#             me =a
#         if b<mic:
#             mic =b 
#             mi = a 
#     print(me,mi)
# arr = list(map(int,input().split()))
# n = len(arr)
# p(arr,n)

# def p(arr,n):
#     xorr=0
#     for i in range(n):
#         xorr=xorr^arr[i]
#     print(xorr)

# arr= list(map(int,input().split()))
# n = len(arr)
# p(arr,n)

# def p(arr,n):
#     s = 0
#     m = 0
#     for i in range(n):
#         s += arr[i]
#         m = max(m,s)
#         if s<0:
#             s=0
#     print(m)
# arr = list(map(int,input().split()))
# n = len(arr)
# p(arr,n)


# def a(arr,n):
#     for i in range(n):
#         j=i
#         while j > 0 and arr[j-1]>arr[j]:
#             arr[j-1], arr[j]= arr[j],arr[j-1]
#             j-=1
#     print(arr)
# arr =list(map(int,input().split()))
# n = len(arr)
# a(arr,n)
