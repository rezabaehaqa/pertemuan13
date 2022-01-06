import sys
try:
    a = int(input("Masukan nilai a : "))
    b = int(input("Masukan nilai b : "))
except ValueError:
    print("Nilai harus bertipe numerik")
    sys.exit()
hasil=a+b
print("Hasil Penjumlahan :",hasil)