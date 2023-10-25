kendaraan_impian = ["X-Diavel", "Motor", "1262 CC", "Merah", "2"]
kendaraan_impian.append ("Rp.878.900.000")
kendaraan_impian.append  ("Manual")
kendaraan_impian.insert (2, "Ducati")
print (kendaraan_impian)

pesan = """
menu:
1. Menghitung luas persegi
2. Menghitung luas lingkaran
3. Menghitung luas segitiga
pilih menu:
"""

pilihan = input(pesan)

match pilihan: 
    case "1":
        print ("1. untuk menghitung Luas Persegi")
        sisi = int(input("masukkan luas persegi"))
        LuasPersegi = sisi*sisi
        print ("luas persegi dengan sisi", sisi, "adalah", LuasPersegi)
    case "2":
        print ("2. untuk menghitung luas lingkaran")
        r = float(input("masukkan jari-jari lingkaran: "))
        LuasLingkaran = 3.14 * (r * r)
        print ("luas lingkaran dengan jari-jari", r, "adalah", LuasLingkaran)
    case "3":
        print ("3. untuk menghitung luas segitiga")
        alas = int(input("masukkan alas: "))
        tinggi = int(input("masukkan tinggi: "))
        LuasSegitiga = 1/2*(alas*tinggi)
        print ("luas segitiga dan alas", alas, "dan tinggi", "adalah", LuasSegitiga)
    case "4": print ("salah input, silahkan masukkan kata kunci yang benar!")
