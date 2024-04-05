# #1
# def powera3(a):
#     print(a**3)
# powera3(2)
# #2
# def powera234(a):
#     print(a**2)
#     print(a**3)
#     print(a**4)
# powera234(12)
# #3
# def mean(a,b):
#     print((a+b)/2)
#     print((a*b)**0.5)
# mean(12,23)
# #4
# def voidtringle(a,b,c):
#     p = a+b+c
#     print(p)
# voidtringle(12,12,12)
# #6
# def digitCountSum():
#     num = int(input("son kirit:"))
#     sum = 0
#     count = 0
#     while num > 0:
#         a = num%10
#         num//=10
#         count+=1
#         sum+=a
#     print(count,sum)
# digitCountSum()
# #7
# def invertDigit():
#     a = (input("son kirit:"))
#     print(a[::-1])
    
# invertDigit()
# # 10
# def swap(a,b):
#     a,b = b,a
#     return a,b
# print(swap(12,23))
##11
# def minmax(a,b):
#     if a < b:
#         print(f"kattasi b={b} kichigi a={a}")
#     elif a > b:
#         print(f"kattasi a = {a} kichigi b={b}")
#     elif a == b:
#         print("ikkalasi bir xil")
# minmax(12,23)
##16
# def ishora(a):
#     if a < 0:
#         print(f"a={a} son manfiy")
#     elif a > 0:
#         print(f"a={a} son musbat")
#     elif a == 0:
#         print(f"a={a} son nolga teng")
# ishora(12)
# ishora(0)
# ishora(-12)

# def calc(a,b,op):
#     if op == "+":
#         print(a+b)
#     elif op == "-":
#         print(a-b)
#     elif op == "*":
#         print(a*b)
#     elif op == "/":
#         print(a/b)
# calc(12,12,"+")
# calc(23,12,"-")
# calc(12,12,"*")
# calc(12,12,"/")

# #21
# def sumrange(a,b):
#     if a < b:
#         s = 0
#         for i in range(a,b):
#             s+=i
#         print(s)
#     elif a > b: 
#         n = 0
#         for j in range(b,a):
#             n+=j
#         print(n)
#     else:
#         print("sonlar teng")
# sumrange(12,24)
# #24
# def even(k):
#     if k%2==0:
#         print("true")
#     elif k%2==1:
#         print("false")
# even(12)
# even(13)
# even(34567)    
# #25
# def issquare(k):
#     a = k**0.5
#     if int(a)**2==k:
#         print("true")
#     else:
#         print("false")
# issquare(9)










