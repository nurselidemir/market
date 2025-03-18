class MaliModul:
    def __init__(self):
        self.gelirler = []
        self.giderler = []
    
    def gelir_ekle(self, miktar, aciklama=""):
        self.gelirler.append({"miktar": miktar, "aciklama": aciklama})
    
    def gider_ekle(self, miktar, aciklama=""):
        self.giderler.append({"miktar": miktar, "aciklama": aciklama})
    
    def toplam_gelir(self):
        return sum(g["miktar"] for g in self.gelirler)
    
    def toplam_gider(self):
        return sum(g["miktar"] for g in self.giderler)
    
    def kar_zarar_hesapla(self):
        kar_zarar = self.toplam_gelir() - self.toplam_gider()
        return kar_zarar, "Kar" if kar_zarar > 0 else "Zarar" if kar_zarar < 0 else "Başabaş"

# Kullanım örneği
mali = MaliModul()
mali.gelir_ekle(5000, "Ürün Satışı")
mali.gider_ekle(2000, "Kira")
mali.gider_ekle(1000, "Maaşlar")

kar_zarar, durum = mali.kar_zarar_hesapla()
print(f"Toplam Gelir: {mali.toplam_gelir()} TL")
print(f"Toplam Gider: {mali.toplam_gider()} TL")
print(f"Kar/Zarar: {kar_zarar} TL ({durum})")
