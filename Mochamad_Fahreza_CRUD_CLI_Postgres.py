import psycopg2
import os

DB_NAME = "toko_makanan"
DB_USER = "postgres"
DB_PASS = "Reza27"
DB_HOST = "localhost"
DB_PORT = "5432"
try:
    db = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("Server Telah Tersambung")
except:
    print("Server Belum Tersambung")
    
cur = db.cursor()

def insert_data(db):
  kode    = input("Masukan Kode Makanan  : ")
  nama    = input("Masukan Nama Makanan  : ")
  harga   = input("Masukan Harga Makanan : ")
  jm      = input("Masukan Jenis Makanan : ")
  val   = (kode,nama,harga,jm)
  cursor = db.cursor()
  sql    = "INSERT INTO makanan (kode_makanan,nama,harga,jenis_makanan) VALUES (%s, %s,%s,%s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} Data berhasil disimpan".format(cursor.rowcount))


def Tampil_data(db):
  cursor = db.cursor()
  sql    = "SELECT * FROM makanan"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  Tampil_data(db)
  kode    = input("Masukan Kode Makanan Yang Mau di Ubah  : ")
  nama    = input("Masukan Nama Makanan  : ")
  harga   = input("Masukan Harga Makanan : ")
  jm      = input("Masukan Jenis Makanan : ")


  sql = "UPDATE makanan SET  nama =%s, harga=%s , jenis_makanan=%s WHERE kode_makanan=%s"
  val = (nama,harga,jm,kode)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def Hapus_data(db):
  cursor = db.cursor()
  Tampil_data(db)
  kode = input("Masukan Kode Makanan : ")
  sql = "DELETE FROM makanan WHERE kode_makanan = '" + str(kode) + " ' "
  val = (kode)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def Cari_data(db):
  cursor  = db.cursor()
  key = input("Kata kunci: ")
  sql     = "SELECT * FROM makanan WHERE kode_makanan = '" + key + "'"
  val     = ("%{}%".format(key), "%{}%".format(key),"%{}%".format(key))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def Menu(db):
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    Tampil_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    Hapus_data(db)
  elif menu == "5":
    Cari_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu Tidak ada!")

if __name__ == "__main__":
  Menu(db)
  