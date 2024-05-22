
import modul as muv
print("<<<<<<<<selamat datang di program sederhana memenejemen stok barang>>>>>>>>>")
print("1.tambah data barang")
print("2.edit data yg telah ditambahkan")
print("3.hapus data barang")
print("4.cari data")
print("5.tampilkan data barang")
print("6.tampilkan jumlah data")
print("7.keluar")

while True :
    pilihan = int(input("masukan pilihan : "))
    if pilihan == 1 :
        muv.nambahdata()
    elif pilihan == 2 :
        muv.mengeditdata()
    elif pilihan == 3 :
        muv.menghapusdata()
    elif pilihan == 4 :
        muv.mencaridata()
    elif pilihan == 5 :
        muv.menampilkandata()
    elif pilihan == 6 :
        muv.totaldata()
    elif pilihan == 7 :
        print("makakasih")
        break