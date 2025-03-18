import sqlite3

# Veritabanı bağlantısı
conn = sqlite3.connect("market.db")
cursor = conn.cursor()

# Ürünler tablosunu oluştur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS urunler (
        id INTEGER PRIMARY KEY,
        ad TEXT NOT NULL,
        fiyat REAL NOT NULL,
        stok INTEGER NOT NULL
    )
''')

# Satışlar tablosu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS satislar (
        id INTEGER PRIMARY KEY,
        urun_ad TEXT NOT NULL,
        miktar INTEGER NOT NULL,
        toplam_fiyat REAL NOT NULL
    )
''')
conn.commit()

def urunleri_listele():
    cursor.execute("SELECT * FROM urunler")
    urunler = cursor.fetchall()
    print("\n--- Ürün Listesi ---")
    for urun in urunler:
        print(f"{urun[0]} - {urun[1]}: {urun[2]} TL (Stok: {urun[3]})")
    return urunler

def sepete_ekle(sepet):
    urun_id = int(input("Ürün ID: "))
    miktar = int(input("Miktar: "))
    cursor.execute("SELECT ad, fiyat, stok FROM urunler WHERE id = ?", (urun_id,))
    urun = cursor.fetchone()
    
    if urun and miktar <= urun[2]:
        sepet.append((urun[0], miktar, urun[1] * miktar))
        print(f"{urun[0]} sepete eklendi. {miktar} adet, Toplam: {urun[1] * miktar} TL")
    else:
        print("Geçersiz ürün veya yetersiz stok!")

def satis_tamamla(sepet):
    toplam_tutar = sum(item[2] for item in sepet)
    for item in sepet:
        cursor.execute("INSERT INTO satislar (urun_ad, miktar, toplam_fiyat) VALUES (?, ?, ?)", item)
        cursor.execute("UPDATE urunler SET stok = stok - ? WHERE ad = ?", (item[1], item[0]))
    conn.commit()
    print(f"\nSatış tamamlandı! Toplam: {toplam_tutar} TL")
    sepet.clear()

def main():
    sepet = []
    while True:
        print("\n1. Ürünleri Listele\n2. Sepete Ekle\n3. Satışı Tamamla\n4. Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            urunleri_listele()
        elif secim == "2":
            sepete_ekle(sepet)
        elif secim == "3":
            satis_tamamla(sepet)
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()

# Veritabanı bağlantısını kapatma
conn.close()
