while True:

    rehber = {

        "kisi1":{
        "Cep":"2141522511615215",
        "Is":"12515215235217598",
        "Ev":"876855674596807675"
        },
        "kisi2":{
        "Cep":"798654765654436",
        "Is":"7869457433453423",
        "Ev":"5436754748645363"
        }

    }

    isimler = rehber.keys()
    kisi = input("Kisi Adi :")
    tel = input("Istediginz Telefon :")

    if kisi in isimler:
        flag = True

    else:
        flag = False

    if flag :
        print(rehber.get(kisi).get(tel,"Istediginiz Bilgi Mevcut Degil!"))
        input("Ana Menuye Donmek Icin Enter'a Basin")

    else:
        print("Aradiginiz Kisi Bulunamadi!")
        input("Ana Menuye Donmek Icin Enter'a Basin")
