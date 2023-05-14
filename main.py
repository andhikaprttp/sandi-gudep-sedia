# Membuat kamus sandi Gudep Sedia
kamus_gudep_sedia = {'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e'}

# Fungsi untuk mengenkripsi pesan dengan sandi Gudep Sedia
def enkripsi_gudep_sedia(pesan):
    pesan_terenkripsi = ''
    for karakter in pesan:
        if karakter in kamus_gudep_sedia:
            pesan_terenkripsi += kamus_gudep_sedia[karakter]
        else:
            pesan_terenkripsi += karakter
    return pesan_terenkripsi

# Fungsi untuk mendekripsi pesan dengan sandi Gudep Sedia
def dekripsi_gudep_sedia(pesan_terenkripsi):
    pesan_terdekripsi = ''
    for karakter in pesan_terenkripsi:
        if karakter in kamus_gudep_sedia.values():
            for huruf, kode in kamus_gudep_sedia.items():
                if kode == karakter:
                    pesan_terdekripsi += huruf
        else:
            pesan_terdekripsi += karakter
    return pesan_terdekripsi

# Meminta input pesan dari pengguna
pesan = input("Masukkan pesan yang ingin dienkripsi/didekripsi: ")

# Meminta input tipe operasi (enkripsi/mendekripsi)
operasi = input("Pilih tipe operasi (E: enkripsi, D: dekripsi): ")

# Memanggil fungsi enkripsi atau dekripsi sesuai dengan tipe operasi yang dipilih
if operasi.upper() == 'E':
    pesan_terenkripsi = enkripsi_gudep_sedia(pesan)
    print("Pesan terenkripsi:", pesan_terenkripsi)
elif operasi.upper() == 'D':
    pesan_terdekripsi = dekripsi_gudep_sedia(pesan)
    print("Pesan terdekripsi:", pesan_terdekripsi)
else:
    print("Tipe operasi tidak valid.")
# Andhika Pratama Putra 
