
print("NOMOR 1")

def profil(nama, alamat, gender, umur, hobi):
    print("Nama saya", nama)
    print("Alamat saya", alamat)
    print("Umur saya", umur)
    print("Jenis kelamin saya", gender)

profil("Fauzan", "Bogor", "Laki-laki", "21", "main basket")

print("NOMOR 2")

def nilaiKelulusan(nilai):
    if nilai <= 60:
        print ("gagal")
    elif  61 <= nilai <= 70:
        print ("baik")
    elif 71 <= nilai <= 80:
        print ("sangat baik")
    elif  81 <= nilai <= 100:
        print ("istimewa")
    else :
        print ("Nilai tidak benar")
    
nilaiKelulusan(100)

print("NOMOR 3")

def cetakGanjil(batasAngka):
    for nilai in range(1, batasAngka + 1, 2):
        print(nilai)

batasAngka = 100
cetakGanjil(batasAngka)