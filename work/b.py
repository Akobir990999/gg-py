# a = 12
# b = 23
# def func(a,b):
#     print(a,b)
# func(a,b)

# ism = "zafar"
# def name():
#     ism = "ali"
#     print(ism)
# name()
# print(ism)
# #rekursa
# def full():
#     print("hello")
#     def name():
#         print("zafar")
#     name()
# full()

# def chine():
#     print("hello")
#     def byd():
#         print("mashinalar")
#     byd()
# chine()

# def add():
#     a = 4
#     b = 5
#     print(a+b)

# def a():
#     add()
#     print("a klass haqida malumot")

# def b():
#     add()
#     print("b klass haqida malumot")

# a()
# b()
# def child():
#     s = 1
#     for i in range(1,11):
#         s*=i
#     print(s)
# child()

def child2(n):
    if n == 1:
        return 1
    else:
        return n*child2(n-1)
print(child2(10))
s = 1
for i in range(1,9999):
    s*=i
print(s)