import sqlite3

VeriDosyasi = "todo.db"

def veritabani():
    conn = sqlite3.connect(VeriDosyasi)# Bağlantı oluştur
    cursor = conn.cursor()# İmleç oluştur

    cursor.execute("CREATE TABLE IF NOT EXISTS gorevler (id INTEGER PRIMARY KEY AUTOINCREMENT, metin TEXT NOT NULL,tamamlandi INTEGER DEFAULT 0)")# Tablo oluştur
    conn.commit()# Değişiklikleri kaydet
    conn.close()# Bağlantıyı kapat
    print("Veritabanı ve tablo oluşturuldu.")

def gorev_ekle(metin):
    # Veritabanına görev ekler
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "INSERT INTO gorevler (metin) VALUES (?)"# SQL Injection için önlem
    cursor.execute(sql, (metin,))# değerler demet olarak verilir.

    conn.commit()
    conn.close()
    print(f'{metin} görevi eklendi.')

def gorevleri_getir():
    #Veri tabanınndan görev alır.
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "SELECT id, metin, tamamlandi FROM gorevler"
    cursor.execute(sql)# SQL sorgusu çalıştır

    gorevler = cursor.fetchall()# Tüm görevleri al
    conn.close()
    return gorevler # Görevleri döndür

def gorevi_tamamla(gorev_id):
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "UPDATE gorevler SET tamamlandi = 1 WHERE id =?"# Görevi tamamlandı olarak işaretle
    cursor.execute(sql, (gorev_id,))# değerler demet olarak verilir.

    conn.commit()# Değişiklikleri kaydet
    conn.close()# Bağlantıyı kapat
    print(f"{gorev_id} id'li görev tamamlandı olarak işaretlendi.")

def gorevi_guncelle(gorev_id, tamamlandi):
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "UPDATE gorevler SET tamamlandi = ? WHERE id =?" 
    cursor.execute(sql,(1 if tamamlandi else 0, gorev_id))# değerler demet olarak verilir.
    conn.commit()# Değişiklikleri kaydet
    conn.close()

def gorevi_sil(gorev_id):
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "DELETE FROM gorevler WHERE id =?"# Görevi sil
    cursor.execute(sql, (gorev_id,))# değerler demet olarak verilir.

    conn.commit()
    conn.close()
    print(f"ID: {gorev_id} olan görev silindi.")

