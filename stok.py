from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from collections import defaultdict

# Rapor arayüzü
class Rapor(ABC):
    @abstractmethod
    def olustur(self):
        pass

# Stok Yönetimi Sınıfı
class Stok:
    def __init__(self):
        self.urunler = {}
        self.kritik_seviye = 5  # Kritik stok seviyesi eşiği
    
    def urun_ekle(self, isim, miktar):
        if isim in self.urunler:
            self.urunler[isim] += miktar
        else:
            self.urunler[isim] = miktar
    
    def urun_sat(self, isim, miktar):
        if isim in self.urunler and self.urunler[isim] >= miktar:
            self.urunler[isim] -= miktar
            return True
        return False
    
    def stok_durumu(self):
        return self.urunler
    
    def kritik_stok_kontrol(self):
        return {isim: miktar for isim, miktar in self.urunler.items() if miktar <= self.kritik_seviye}

# Satış Yönetimi Sınıfı
class Satis:
    def __init__(self):
        self.satis_kayitlari = []
    
    def satis_kaydet(self, urun, miktar):
        self.satis_kayitlari.append({"tarih": datetime.now(), "urun": urun, "miktar": miktar})
    
    def satislari_getir(self, baslangic_tarihi, bitis_tarihi):
        return [satis for satis in self.satis_kayitlari if baslangic_tarihi <= satis["tarih"] <= bitis_tarihi]

# Günlük Satış Raporu Sınıfı
class GunlukSatisRaporu(Rapor):
    def __init__(self, satis):
        self.satis = satis
    
    def olustur(self):
        bugun = datetime.now().date()
        baslangic_tarihi = datetime(bugun.year, bugun.month, bugun.day)
        bitis_tarihi = baslangic_tarihi + timedelta(days=1)
        gunluk_satislar = self.satis.satislari_getir(baslangic_tarihi, bitis_tarihi)
        ozet = defaultdict(int)
        for satis in gunluk_satislar:
            ozet[satis["urun"]] += satis["miktar"]
        return ozet

# Haftalık Satış Raporu Sınıfı
class HaftalikSatisRaporu(Rapor):
    def __init__(self, satis):
        self.satis = satis
    
    def olustur(self):
        bugun = datetime.now().date()
        baslangic_tarihi = datetime(bugun.year, bugun.month, bugun.day) - timedelta(days=bugun.weekday())
        bitis_tarihi = baslangic_tarihi + timedelta(days=7)
        haftalik_satislar = self.satis.satislari_getir(baslangic_tarihi, bitis_tarihi)
        ozet = defaultdict(int)
        for satis in haftalik_satislar:
            ozet[satis["urun"]] += satis["miktar"]
        return ozet

# Market Sistemi Simülasyonu
stok = Stok()
satis = Satis()

# Başlangıç stoğu ekleme
stok.urun_ekle("Elma", 20)
stok.urun_ekle("Muz", 15)
stok.urun_ekle("Süt", 10)

# Satışları simüle etme
satis.satis_kaydet("Elma", 5)
satis.satis_kaydet("Muz", 3)
satis.satis_kaydet("Süt", 2)
stok.urun_sat("Elma", 5)
stok.urun_sat("Muz", 3)
stok.urun_sat("Süt", 2)

# Raporları oluşturma
gunluk_rapor = GunlukSatisRaporu(satis)
haftalik_rapor = HaftalikSatisRaporu(satis)

print("Günlük Satış Raporu:", gunluk_rapor.olustur())
print("Haftalık Satış Raporu:", haftalik_rapor.olustur())
print("Kritik Stok Seviyeleri:", stok.kritik_stok_kontrol())