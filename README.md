# Studi_Kasus_6_DDP_Rafik_Anugrah_Yana

Nama: Rafik Anugrah Yana

NIM: 2609116086

Kelas: C 2026

1.Penjelasan singkat program
![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/1.png)

Kode ini berfungsi untuk import library json ke file python dan membuat function baca data untuk read(r)/membaca file invataris.json. terdapat penanganan error jika file json tidak ditemukan FileNotFoundError terjadi dan program menjalankan return [], sehingga dianggap belum ada data dan program akan menampilkan data kosong[]. disini saya tidak memakai path karena file json masih satu folder dengan file python

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/2.png)

Kode ini merupakan function untuk menampilkan barang, jadi disini function baca data di panggil menggunakan barang, lalu terdapat print untuk menampilkan judul, lalu terdapat kondisi jika jumlah data dalam barang adalah 0, jika iya maka program akan menampilkan  pesan "Belum ada data barang.". Jika terdapat data, bagian for i, data in enumerate(barang, 1) akan melakukan perulangan untuk setiap barang sekaligus memberikan nomor mulai dari 1, lalu data['nama'], data['stok'], dan data['harga'] digunakan untuk mengambil nama, stok, dan harga dari setiap barang dan menampilkannya

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/3.png)

Kode ini merupakan function tambah barang yang berfungsi untuk menambah data ke dalam file json, Program mengambil data lama dari baca_data() yang di definisikan menjadi barang, kemudian meminta nama, stok, dan harga barang. try-except digunakan untuk memastikan stok dan harga berupa angka. Setelah itu, data baru dimasukkan menggunakan append(), lalu json.dump() menyimpan kembali seluruh data ke file JSON

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/4.png)

Kode ini merupakan function untuk tampilan menu, while True membuat menu terus muncul sampai pengguna memilih keluar, kemudian input() digunakan untuk menerima pilihan 1–3. Jika memilih 1, program menjalankan tampilkan_barang(), jika memilih 2 menjalankan tambah_barang(), dan jika memilih 3, break menghentikan perulangan dan program selesai. Jika input selain 1–3, program menampilkan pesan "Pilihan tidak valid.". Terakhir, menu() digunakan untuk menjalankan fungsi tersebut

2. Output Program

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/output%201.png)

Tampilan menu utama, terdapat input angka 1-3

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/output%202.png)

Tampilan ketika input 1 untuk melihat semua data yang sesuai dengan file json

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/isi%20file%20json%20sebelum.png)

isi file json 

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/output%203.png)

Tampilan ketika ingin menambahkan data

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/isi%20file%20json%20sesudah.png)

isi file json ketika sudah menambahkan data dari program

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/output%204.png)

Tampilan ketika keluar dari program 

![alt text](https://github.com/sleepnpeace/Studi_Kasus_6_DDP_Rafik_Anugrah_Yana/blob/main/images/output%205.png)

Bukti jika data masih kesimpan saat ingin run ulang program dan ingin melihat di dalam program
