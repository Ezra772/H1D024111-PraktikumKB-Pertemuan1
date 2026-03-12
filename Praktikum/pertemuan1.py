import random
import datetime


# library datetime
start_time = datetime.datetime.now()

# struktur data
riwayat_tebakan = []

# library random
angka_rahasia = random.randint(1, 20)

print("Game Tebak Angka")
print("Tebak angka antara 1 - 20")

while True:  # struktur kontrol perulangan
    tebakan = int(input("Masukkan angka tebakan: "))
    
    riwayat_tebakan.append(tebakan)

    if tebakan < angka_rahasia:
        print("Terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Terlalu besar")
    else:
        print("Benar! Kamu menang")
        break

print("Riwayat tebakan:", riwayat_tebakan)

end_time = datetime.datetime.now()
durasi = end_time - start_time
print("Durasi menebak:", durasi)