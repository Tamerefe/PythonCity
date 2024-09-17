import random

# Rastgele isim ve ülke havuzları
names_male = ["Ahmet", "Mehmet", "Can", "Ali", "Murat"]
names_female = ["Ayşe", "Fatma", "Elif", "Zeynep", "Merve"]
countries = ["Türkiye", "Almanya", "Japonya", "Amerika", "İngiltere"]

# Rastgele olaylar listesi (Yeni statler için güncellendi)
events = [
    ("Boşanıyorsunuz. Eğlenceli olsun diye, hiçbir eş evi terk etmiyor.", 0, -2000, -20, 0, -10, 0, 0, -5),
    ("İflas! Tüm paranızdan sadece 200 TL kaldı.", 0, -3000, -30, 0, 0, 0, 0, 0),
    ("Büyük bir yangın çıkıyor, eviniz zarar gördü.", -40, -5000, -50, 0, -5, -10, 0, 0),
    ("Hastalık günü: Bir gün işe/okula gitmiyorsunuz.", -10, 0, 0, 0, 0, -5, -5, 0),
    ("Bir çocuk evlat edindiniz.", 0, -1000, 20, 0, 10, 0, 0, 0),
    ("Aldatıldınız!", 0, 0, -30, 0, -15, 0, 0, 0),
    ("İşsiz kaldınız, yeni bir kariyer seçmek zorundasınız.", 0, -2000, -20, 0, 0, -20, 0, 0),
    ("Yeni bir eve taşındınız.", 0, -3000, 10, 0, 5, 0, 0, 0),
    ("Evde bir odayı yeniden dekore ettiniz.", 0, -500, 15, 0, 0, 0, 0, 10),
    ("Orta yaş krizi: Tüm paranızı eğlenceye, kıyafetlere, arabalara harcadınız.", 0, -5000, 30, 0, 0, 0, 0, 0),
    ("Bir parti verdiniz!", 0, -1000, 20, 0, 15, 0, 0, 0),
    ("Ailecek dans ettiniz.", 0, 0, 10, 0, 10, 0, 0, 5),
    ("Yeni bir saç stili ve rengi yaptırdınız.", 0, -500, 5, 0, 0, 0, 0, 0),
    ("Bir bebek evlat edindiniz.", 0, -1000, 20, 0, 0, 0, 0, 0),
    ("Bir arkadaşınızla okulu astınız.", 0, 0, -10, 0, 0, 0, 0, 0),
    ("Havuz partisi verdiniz.", 0, -500, 15, 0, 10, 0, 0, 5),
    ("Tüm ailenizle kahvaltı, öğle veya akşam yemeği yediniz.", 0, 0, 10, 0, 5, 0, 0, 0),
    ("Havai fişek patlarken yüzünüze çarptı.", -20, 0, -10, 0, 0, 0, -10, 0),
    ("Bir tatil günü seçtiniz ve evi tatil gibi dekore ettiniz.", 0, -500, 20, 0, 5, 0, 0, 0),
    ("Tatile çıktınız.", 0, -3000, 30, 0, 10, 0, 0, 0),
    ("Bir misafir evinize taşındı.", 0, 0, 10, 0, 10, 0, 0, 0),
    ("Zorla askere alındınız.", -10, 0, 0, 0, 0, 10, 20, 0),
    ("Biriyle düello ettiniz.", -15, 0, -10, 0, 0, 0, 10, 0),
    ("Soyuldunuz!", 0, -500, -20, 0, 0, -5, 0, 0),
    ("Parkta piknik yaptınız.", 0, -100, 10, 0, 5, 0, 0, 5),
    ("Bir kitap yazdınız.", 0, 500, 20, 10, 0, 0, 0, 5),  # Zeka artar
    ("Bir yazar oldunuz ve yazdığınız kitaplar sayesinde para kazandınız.", 0, 1000, 20, 10, 0, 10, 0, 5),  # Zeka ve kariyer artar
    ("Freelance bir iş aldınız ve para kazandınız.", 0, 1500, 20, 0, 0, 15, 0, 0),  # Kariyer artar
    ("Online bir işten para kazandınız.", 0, 2000, 15, 0, 0, 10, 0, 0),  # Kariyer artar
    ("Lotto'dan büyük bir ödül kazandınız!", 0, 10000, 40, 0, 0, 0, 0, 0),  # Sadece para
    ("Bir YouTube videosu çektiniz ve viral oldu, para kazandınız.", 0, 3000, 25, 0, 10, 10, 0, 0),  # Sosyal beceri ve kariyer artar
    ("Borsada yatırım yaptınız ve para kazandınız.", 0, 5000, 30, 0, 0, 15, 0, 0),  # Kariyer artar
    ("Bir komşuya yardım ettiniz ve karşılığında ödeme aldınız.", 0, 800, 15, 0, 10, 0, 0, 5),
    ("Bir iş kurdunuz ve başarılı oldunuz, para kazandınız.", 0, 7000, 35, 0, 0, 20, 0, 0),  # Kariyer artar
    ("Bir yemek siparişi verdiniz ve pizza kuryesiyle flört ettiniz.", 0, 0, 15, 0, 10, 0, 0, 0),
    ("Bir komşunuzu eve davet ettiniz ve onu bir odada kilitlediniz.", 0, 0, -30, 0, -20, 0, 0, 0),
    ("Bir randevuya çıktınız.", 0, -200, 20, 0, 10, 0, 0, 0),
    ("Bir topluluk etkinliğine katıldınız ve yeni arkadaşlar edindiniz.", 0, 0, 20, 0, 10, 0, 0, 0),
    ("Bir kişisel gelişim kitabı okudunuz, zekanız ve mutluluğunuz arttı.", 0, 0, 15, 10, 0, 0, 0, 0),  # Zeka artar
    ("Tüm kıyafetlerinizi değiştirdiniz, yeni bir tarz oluşturdunuz.", 0, -500, 10, 0, 5, 0, 0, 0),
    ("Bir balık tuttunuz ve onu duvara astınız.", 0, -100, 5, 0, 0, 0, 0, 5),  # Hobi artar
    ("Bir YouTube kanalı açtınız, para kazanmaya başladınız.", 0, 1000, 20, 0, 10, 15, 0, 0),  # Sosyal beceri ve kariyer artar
    ("Bir blog yazmaya başladınız ve kazancınız arttı.", 0, 2000, 15, 10, 0, 10, 0, 0),  # Zeka ve kariyer artar
]

class Character:
    def __init__(self):
        # Rastgele cinsiyet seçimi
        self.gender = random.choice(["Erkek", "Kadın"])
        
        # Cinsiyete göre isim havuzundan isim seçimi
        if self.gender == "Erkek":
            self.name = random.choice(names_male)
        else:
            self.name = random.choice(names_female)
        
        # Rastgele ülke seçimi
        self.country = random.choice(countries)
        
        # Yaş 0'dan başlıyor
        self.age = 0  
        
        # Sağlık, Para, Mutluluk gibi değerler rastgele atanıyor
        self.health = random.randint(50, 100)  # Sağlık 50-100 arası rastgele
        self.money = random.randint(1000, 10000)  # Para 1000-10000 TL arası rastgele
        self.happiness = random.randint(20, 80)  # Mutluluk 20-80 arası rastgele
        self.intelligence = random.randint(0, 100)  # Zeka 0-100 arası
        self.social_skill = random.randint(0, 100)  # Sosyal beceri 0-100 arası
        self.career_experience = random.randint(0, 100)  # Kariyer deneyimi 0-100 arası
        self.physical_strength = random.randint(0, 100)  # Fiziksel güç 0-100 arası
        self.hobby_skill = random.randint(0, 100)  # Hobi becerisi 0-100 arası

    def show_status(self):
        print(f"\n--- {self.name}'in Durumu ---")
        print(f"Cinsiyet: {self.gender}")
        print(f"Ülke: {self.country}")
        print(f"Yaş: {self.age}")
        print(f"Sağlık: {self.health}")
        print(f"Para: {self.money} TL")
        print(f"Mutluluk: {self.happiness}")
        print(f"Zeka: {self.intelligence}")
        print(f"Sosyal Beceri: {self.social_skill}")
        print(f"Kariyer Deneyimi: {self.career_experience}")
        print(f"Fiziksel Güç: {self.physical_strength}")
        print(f"Hobi Beceri: {self.hobby_skill}")
        print("----------------------------\n")

    def is_alive(self):
        return self.health > 0

class LifeSimulation:
    def __init__(self, character):
        self.character = character
    
    def play_turn(self):
        if not self.character.is_alive():
            print("Karakteriniz hayatta değil. Oyun bitti!")
            return False

        self.character.age += 1
        print(f"\n{self.character.age} yaşına girdiniz.")
        
        # Rastgele olaylar oluştur
        event = random.choice(events)
        self.process_event(event)
        return True
    
    def process_event(self, event):
        description, health_change, money_change, happiness_change, intelligence_change, social_change, career_change, strength_change, hobby_change = event
        print(f"Olay: {description}")
        
        # Karakter özelliklerini güncelle
        self.character.health += health_change
        self.character.money += money_change
        self.character.happiness += happiness_change
        self.character.intelligence += intelligence_change
        self.character.social_skill += social_change
        self.character.career_experience += career_change
        self.character.physical_strength += strength_change
        self.character.hobby_skill += hobby_change
        
        # Sınırları kontrol et
        self.character.health = max(0, min(100, self.character.health))
        # self.character.money = max(0, self.character.money)  # Negatif olmayı engelleyen kodu kaldırıyoruz
        self.character.happiness = max(0, min(100, self.character.happiness))
        self.character.intelligence = max(0, min(100, self.character.intelligence))
        self.character.social_skill = max(0, min(100, self.character.social_skill))
        self.character.career_experience = max(0, min(100, self.character.career_experience))
        self.character.physical_strength = max(0, min(100, self.character.physical_strength))
        self.character.hobby_skill = max(0, min(100, self.character.hobby_skill))
        
        # Karakter durumunu göster
        self.character.show_status()

# Ana oyun döngüsü
def main():
    print("My Life Simülasyonuna Hoş Geldiniz!")
    print("Devam etmek için Enter'a basın, çıkmak için 'q' yazın")
    
    # Karakter yarat
    character = Character()
    simulation = LifeSimulation(character)
    
    # Karakterin başlangıç durumunu göster
    character.show_status()
    
    # Oyun döngüsü
    while simulation.play_turn():  # Sonsuz döngü, q girilince döngüden çıkılacak
        user_input = input("Yılı ilerlet: ")
        if user_input.lower() == 'q':  # Eğer 'q' yazarsa döngüyü kır
            break
    
    print("Oyun sona erdi.")

# Oyun başlatma
if __name__ == "__main__":
    main()
