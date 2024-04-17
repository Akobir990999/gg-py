# class student:
#     def __init__(self,name,familiya,age,kurs):
#         self.name=input = name
#         self.familiya=input = familiya
#         self.age=in = age
#         self.kurs = kurs
# st1 = student("akobir","sobirov",12,4)
# st2 = student("ali","valiyev",23,4)

# print(st1.age)
# print(st1.name)
# print(st1.familiya)
# print(st1.kurs)

# print(st2.age)
# print(st2.name)
# print(st2.familiya)
# print(st2.kurs)

# print(st1.__dict__)
# print(st2.__dict__)
# print(220+187)

class Car:
    def __init__(self,ismi,modeli,yili,narxi):
        self.ism = ismi
        self. model = modeli
        self.yil = yili
        self. narx = narxi

car1 = Car("porche 911","porche",2020,50000)
print(car1.__dict__)
car2 = Car("mersades amg","mersades",2022,200000)
print(car2.__dict__)
car3 = Car("mersades gle","mersades",2021,200000)
print(car3.__dict__)
car4 = Car("lamborgini aventador","lamborgini",2023,300000)
print(car4.__dict__)
car5 = Car("nexia 2","nexia",2020,30000) 
print(car5.__dict__)