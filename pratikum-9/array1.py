# Deklarasi array menyimpan angka ganjil dan genap
ganjil = []
genap = []

# Meminta input pengguna
for i in range(10):
    angka = int(input(f"masukan angka ke-{i+i}: "))

    # memisahkan ganjil dan genap
    if angka % 2 == 0:
        genap.append(angka)
    else:
        ganjil.append(angka)

# menampilkan hasil
print(f"Angka genap: {genap}")
print(f"Angka ganjil: {ganjil}")