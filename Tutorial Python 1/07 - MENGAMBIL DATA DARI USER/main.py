# Episode input user

# Data yang dimasukkan pasti string
data = input("Masukkan data : ")
print("data = ", data, "type =", type(data))

# Jika kita ingin mengambil int, maka
angka = float(input("Masukkan angka :"))
angka = int(input("Masukkan angka :"))

print("data = ", angka, "type =", type(angka))

# Bagaimana dengan boolean
data_boolean = bool(int(input("Masukkan nilai boolean :"))) # dicasting ke dalam integer terlebih dahulu

print("data = ", data_boolean, "type =", type(data_boolean))

#selesai