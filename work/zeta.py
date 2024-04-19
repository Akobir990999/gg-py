# class user:
#     def __init__(self,ism,familiya,email,yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.email = email
#         self.yosh = yosh
#     def get_info(self):
#         print(f"foydalanuvchi ismi:{self.ism},familiyasi : {self.familiya},yoshi:{self.yosh},foydalanuvchi emaili:{self.email}")

#     def get_ism(self):
#         print(self.ism)

#     def get_familiya(self):
#         print(self.familiya)
#     def get_em(self):
#         print(self.email)
#     def get_year(self):
#         print(self.yosh)
#     def get_year1(self):
#         print(int(input("yini kirit"))-self.yosh)
# a = user("akobir","kuchkarboev","bobirsobirov873@gmail.com",12)
# a.get_info()
# a.get_familiya()
# a.get_em()
# a.get_year()
# a.get_year1()


# class student:
#     def __init__(self,ism,familiya,yosh):
#         self.ism = ism
#         self.familiya = familiya 
#         self.yosh = yosh
#         self.kurs = 1
#         self.fanlar = []
#     def get_info(self):
#         print(f"mening ismim {self.ism}")
        
#     def set_kurs(self):
#         self.kurs+=1
        
#     def add_subject(self,fan):
#         self.fanlar.append(fan)

# student1 = student("akobir","sobirov",12)
# student1.set_kurs()
# student1.add_subject("matamatika")
# print(student1)

# class avto:
#     def __init__(self,model,rang,tezlik,narx):
#         self.model = model
#         self.rang = rang
#         self.narx = narx
#         self.tezlik = tezlik
#         self.kilometr = 0   
#     def avto_model(self):
#         print(f"mashinani modeli {self.model}")
#     def avto_rang(self):
#         print(f"moshinaning rangi {self.rang}")
#     def avto_narx(self):
#         print(f"avtomobilni narxi {self.narx}")
#     def avto_tezlik(self):
#         print(f"avtomobilni tezligi {self.tezlik}km/h")
#     def update_kilometr(self):
#         self.kilometr+=1
#     def get_info(self):
#         print(f"avtomobil modeli {self.model},narxi {self.narx},tezligi {self.tezlik}km/h,rangi {self.rang}")

# avto1 = avto("mersades","yashil",370,"300000$")
# avto1.avto_model()
# avto1.avto_rang()
# avto1.avto_tezlik()
# avto1.avto_narx()
# avto1.get_info()

class avto_salon:
    def __init__(self,nomi,manzili,*avtomobillar):
        self.nom = nomi
        self.manzil = manzili
        self.avtomobil = avtomobillar
        self.mashinalar = []
    def new_avto(self):
        self.mashinalar.append(self.avtomobil)

    def remowe_avto(self):
        a = input("ochirmoqchi bolgan avtoyingni kirit")
        for i in a:
            if i in self.mashinalar:
                print(remowe(i))

a = avto_salon("a","df","mersades","bmw")
a.new_avto()
a.remowe_avto()
print(self.mashinalar)
    
            