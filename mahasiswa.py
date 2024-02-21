import os

def tambah_data(db):
    nim = input("Input NIM:")
    nama_lengkap = input("Input nama lengkap: ")
    alamat = input("Input alamat: ")
    cursor = db.cursor()
    kueri = "INSERT INTO students (nim, nama_lengkap, alamat) VALUES (%s, %s, %s)"
    val = (nim, nama_lengkap, alamat)
    cursor.execute(kueri, val)
    db.commit()
    print("{} Data berhasil disimpan".format(cursor.rowcount))


def tampil_data(db):
    cursor = db.cursor()
    kueri = "SELECT * FROM students"
    cursor.execute(kueri)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for record in results:
            print(record)
    print("------------------------------")

def update_data(db):
    cursor = db.cursor()
    tampil_data(db)
    nim = input("Input NIM: ")
    nama_lengkap = input("Input nama lengkap: ")
    alamat = input("Input alamat: ")

    kueri = "UPDATE students SET nama_lengkap=%s, alamat=%s WHERE nim=%s"
    val = (nama_lengkap, alamat, nim)
    cursor.execute(kueri, val)
    db.commit()
    print("{} Data berhasil diubah".format(cursor.rowcount))


def hapus_data(db):
    cursor = db.cursor()
    tampil_data(db)
    nim = input("Pilih NIM Mahasiswa: ")
    kueri = "DELETE FROM students WHERE nim=%s"
    cursor.execute(kueri, (nim,))
    db.commit()
    print("{} Data berhasil dihapus".format(cursor.rowcount))


def cari_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    kueri = "SELECT * FROM students WHERE nama_lengkap LIKE %s OR alamat LIKE %s"
    cursor.execute(kueri, ('%' + keyword + '%', '%' + keyword + '%'))
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print(f"Data {keyword} tidak ditemukan pada database!")
    else:
        for record in results:
            print(record)

def show_menu(db):
    print("=== PROGRAM DATA MAHASISWA ===")
    print("1. Show Data")
    print("2. Insert Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("----------------")
    menu = input("silahkan pilih menu")

    #clear screen terminal
    os.system("cls")

    match menu:
        case "1":
            tampil_data(db)
        case "2":
            tambah_data(db)
        case "3":
            update_data(db)
        case "4":
            hapus_data(db)
        case "5":
            cari_data(db)
        case "0":
             exit()
        case _:
             print("Pilihan menu tidak dikenali!")