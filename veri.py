import sqlite3

VeriDosyasi = "todo.db"

def veritabani():
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS gorevler (id INTEGER PRIMARY KEY AUTOINCREMENT, metin TEXT NOT NULL,tamamlandi INTEGER DEFAULT 0)")# Tablo oluştur
    conn.commit()
    conn.close()
    print("Veritabanı ve tablo oluşturuldu.")

def gorev_ekle(metin):
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "INSERT INTO gorevler (metin) VALUES (?)"
    cursor.execute(sql, (metin,))

    conn.commit()
    conn.close()
    print(f'{metin} görevi eklendi.')

def gorevleri_getir():
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "SELECT id, metin, tamamlandi FROM gorevler"
    cursor.execute(sql)

    gorevler = cursor.fetchall()
    conn.close()
    return gorevler 

def gorevi_tamamla(gorev_id):
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "UPDATE gorevler SET tamamlandi = 1 WHERE id =?"
    cursor.execute(sql, (gorev_id,))

    conn.commit()
    conn.close()
    print(f"{gorev_id} id'li görev tamamlandı olarak işaretlendi.")

def gorevi_guncelle(gorev_id, tamamlandi):
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "UPDATE gorevler SET tamamlandi = ? WHERE id =?" 
    cursor.execute(sql,(1 if tamamlandi else 0, gorev_id))
    conn.commit()
    conn.close()

def gorevi_sil(gorev_id):
    conn = sqlite3.connect(VeriDosyasi)
    cursor = conn.cursor()

    sql = "DELETE FROM gorevler WHERE id =?"
    cursor.execute(sql, (gorev_id,))

    conn.commit()
    conn.close()
    print(f"ID: {gorev_id} olan görev silindi.")

