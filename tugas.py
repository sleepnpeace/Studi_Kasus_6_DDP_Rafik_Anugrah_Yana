import json

def baca_data():
    try:
        with open("inventaris.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def tampilkan_barang():
    barang = baca_data()

    print("\nData Inventaris Barang")

    if len(barang) == 0:
        print("Belum ada data barang.")
    else:
        for i, data in enumerate(barang, 1):
            print(f"{i}. {data['nama']} | Stok: {data['stok']} | Harga: Rp{data['harga']}")

def tambah_barang():
    barang = baca_data()

    print("\nTambah Barang")

    nama = input("Nama barang: ")
    
    try:
        stok = int(input("Jumlah stok: "))
        harga = int(input("Harga barang: "))
    except ValueError:
        print("Stok dan harga harus berupa angka.")
        return

    data_baru = {
        "nama": nama,
        "stok": stok,
        "harga": harga
    }

    barang.append(data_baru)

    with open("inventaris.json", "w") as file:
        json.dump(barang, file, indent=4)

    print("Barang berhasil ditambahkan.")

def menu():
    while True:
        print("\nSistem Manajemen Inventaris")
        print("1. Lihat semua barang")
        print("2. Tambah barang")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            tampilkan_barang()

        elif pilihan == "2":
            tambah_barang()

        elif pilihan == "3":
            print("Terima Kasih dan Sampai jumpa Lagi.")
            break

        else:
            print("Pilihan tidak valid.")
menu()