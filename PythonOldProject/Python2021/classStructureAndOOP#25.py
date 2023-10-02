#   class <Class Ismi>():          # class isimleri, genelin aksine buyuk harfle baslar (zorunluluk yok)
        
#       <class attr>               # class attribute, olusturulanin aksine genel degerleri icerir

#  def_ınıt_(self, <attr>):        # init, instantiation yani orneklendirmenin kisaltmasidir
#    self.<instance attr> = attr   # instance attribute'lar, olusturulan ornege ozgudur

#  def <method>(self,<params>):    # methodlar class'a özgü fonksiyonlardir
#    ...
#    return ...

class Flight():
    airline = "THY"

flight1 = Flight()

print(flight1.airline)


class Flight2():
    airline = "THY"

    def __init__(self, code, departure, arrival, time, capacity, passenger):
        self.code = code
        self.departure = departure
        self.arrival = arrival
        self.time = time
        self.capacity = capacity
        self.passenger = passenger

flight2 = Flight2("TK","IST","ANK",60,300,50)

print(flight2.code)

flight3 = Flight2("TK1235", "BOD", "ANT", 42, 255, 111)

print(flight3.departure)

class Flight3():
    airline = "THY"

    def __init__(self, code, departure, arrival, time, capacity, passenger):
        self.code = code
        self.departure = departure
        self.arrival = arrival
        self.time = time
        self.capacity = capacity
        self.passenger = passenger

    def anonce(self, ):
        return "{} number of flights the plane will take off ".format(self.code)


flight4 = Flight3("TK1235", "BOD", "ANT", 42, 255, 111)

print(flight4.anonce)
