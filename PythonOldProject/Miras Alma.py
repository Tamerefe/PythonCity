# class Tasit():
#     def __init__(self,tekerleksayisi,motorhacmi):
#         self.tekerleksayisi = tekerleksayisi
#         self.motorhacmi = motorhacmi

# class Araba(Tasit):
#     pass

# bmw = Araba(4,2000)

# print(bmw.motorhacmi)

# MIRAS TURLERI

class Tasit():
    def __init__(self,tekerleksayisi,motorhacmi):
        self.tekerleksayisi = tekerleksayisi
        self.motorhacmi = motorhacmi

    # def Boyut(self)

class Araba(Tasit):

    def __init__(self,tekerleksayisi,motorhacmi,kapisayisi):
        super(Araba,self).__init__(tekerleksayisi,motorhacmi)
        self.kapisayisi = kapisayisi

        # self.tekerleksayisi = tekerleksayisi
        # self.motorhacmi = motorhacmi
        # self.kapisayisi = kapisayisi

bmw = Araba(4,2000,2)

print(bmw.kapisayisi,bmw.motorhacmi,bmw.tekerleksayisi)
