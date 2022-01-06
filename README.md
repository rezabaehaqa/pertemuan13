# pertemuan13
```sh
Nama    : A. Reza Baehaqa Jamroni
Nim     : 312110494
Matkul  : Bahasa Perograman
```
### Eksepsi (Exception)
Eksepsi (exception) merupakan suatu kesalahan (error) yang terjadi saat proses eksekusi program sedang berjalan, kesalahan ini akan menyebabkan program berakhir dengan tidak normal. Kesalahan-kesalahan ini dapat diidentifikasikan dengan nama tertentu dan direpresentasikan sebagai objek di dalam python.

### Standart Exception
| Nama                | Istilah                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Exception           |	Kelas dasar untuk semua pengecualian / exception                                                                          |
| StopIteration       |	Dibesarkan ketika metode (iterator) berikutnya dari iterator tidak mengarah ke objek apa pun.                             |
| SystemExit	      |Dibesarkan oleh fungsi sys.exit ().                                                                                        |
| StandardError	      |Kelas dasar untuk semua pengecualian built-in kecuali StopIteration dan SystemExit.                                        |
| ArithmeticError	  |Kelas dasar untuk semua kesalahan yang terjadi untuk perhitungan numerik.                                                  |
| OverflowError	      |Dibesarkan saat perhitungan melebihi batas maksimum untuk tipe numerik.                                                    |
| FloatingPointError  |	Dibesarkan saat perhitungan floating point gagal.                                                                         |
| ZeroDivisonError	  | Dibesarkan saat pembagian atau modulo nol dilakukan untuk semua tipe numerik.                                             |
| AssertionError	  | Dibesarkan jika terjadi kegagalan pernyataan Assert.                                                                      |
| AttributeError	  | Dibesarkan jika terjadi kegagalan referensi atribut atau penugasan.                                                       |
| EOFError	          | Dibesarkan bila tidak ada input dari fungsi raw_input () atau input () dan akhir file tercapai.                           |
| ImportError	      | Dibesarkan saat sebuah pernyataan impor gagal.                                                                            |
| KeyboardInterrupt	  | Dibesarkan saat pengguna menyela eksekusi program, biasanya dengan menekan Ctrl + c.                                      |
| LookupError	      | Kelas dasar untuk semua kesalahan pencarian.                                                                              |
| IndexError	      | Dibesarkan saat sebuah indeks tidak ditemukan secara berurutan.                                                           |
| KeyError	          | Dibesarkan saat kunci yang ditentukan tidak ditemukan dalam kamus.                                                        |
| NameError	          | Dibesarkan saat pengenal tidak ditemukan di namespace lokal atau global.                                                  |
| UnboundLocalError	  | Dibesarkan saat mencoba mengakses variabel lokal dalam suatu fungsi atau metode namun tidak ada nilai yang ditugaskan  padanya. |
| EnvironmentError    | Kelas dasar untuk semua pengecualian yang terjadi di luar lingkungan Python.                                              |
| IOError	          | Dibesarkan saat operasi input / output gagal, seperti pernyataan cetak atau fungsi open () saat mencoba membuka file yang tidak ada. |
| OSError	          | Dibangkitkan untuk kesalahan terkait sistem operasi.                                                                      |
| SyntaxError   	  | Dibesarkan saat ada kesalahan dengan sintaks Python.                                                                      |
| IndentationError	  | Dibesarkan saat indentasi tidak ditentukan dengan benar.                                                                  |
| SystemError	      | Dibesarkan saat penafsir menemukan masalah internal, namun bila kesalahan ini ditemui juru bahasa Python tidak keluar.    |

### Implementasi
perhatikan program berikut
```sh
a = 1
b = 'X'
print(a+b)
```
Program ini mencoba untuk menjumlahkan variabel a+b namun variabel b memiliki tipe data string, sehingga hal ini akan memicu bangkitnya eksepsi karena akan terjadi error.
Dalam kasus ini eksepsi yang dibangkitkan adalah TypeError dimana operan tidak didukung penjumlahan antara tipe integer dan string.
### raise
raise amenggunakan kata kunci sebagai berikut .
```sh
raise #Exception("# pesan eror")
```
### try_exception
except bentuk umumnya seperti berikut:
```sh
try:
    # kode
except TipeEksepsi:
    # Penanganan kesalahan
```
perhatikan program berikut :
```sh
import sys
try:
    a = int(input("Masukan nilai a : "))
    b = int(input("Masukan nilai b : "))
except ValueError:
    print("Nilai harus bertipe numerik")
    sys.exit()
hasil=a+b
print("Hasil Penjumlahan :",hasil)
```
Pada contoh program di atas kita akan menjumlahkan nilai a dan b yang akan di masukan oleh pengguna. Karena inputan dari pengguna memungkinkan terjadi kesalahan maka perintah tersebut kita tempatkan di dalam blok try, apabila terjadi eksepsi dengan tipe ValueError maka kode di dalam blok except akan di eksekusi.<p>
Selain itu kita juga menggunakan perintah exit() di dalam modul sys untuk menghentikan eksekusi program yang sedang berjalan saat terjadi eksepsi.
Apabila tidak terjadi eksepsi maka kode di dalam blok except tidak akan di eksekusi oleh program dan langsung melompat ke perintah program selanjutnya.
