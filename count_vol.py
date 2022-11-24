import math
def pyramidVol(luasAlas,tinggiLimas):
    return 1/3*luasAlas*luasAlas*tinggiLimas

def ballVol(jari_jari):
    return 4/3*3.14*jari_jari*jari_jari*jari_jari

#Prisama Segiatiga
def prismaSegitiga(alasPrisma,tinggiPrisma,panjangPrisma):
    return (1/2*alasPrisma*tinggiPrisma)*panjangPrisma    

# Prisma Segiempat
def prismaEmpat(panjang,lebar,tinggi):
    return panjang*lebar*tinggi

#Prisma Segilima
def prismaSegilima(panjang,lebar,tinggi):
    return 1/2*5*panjang*lebar*tinggi

def volKrucut(jari_jari,tinggi):
    return 1/3*3.14*jari_jari*jari_jari*tinggi

print("Pilihlah salah satu bangun ruang yang ingin di hitung volumenya :")
print("1. Limas")
print("2. Bola")
print("3. Prisma")
print("4. Kerucut")

pilihan = input ("Masukan Pilihan anda : ")
if pilihan in ("1","2","3","4"):
    if pilihan == "1":
        bilanganSatu = int(input("Masukan Bilangan 1 : "))
        bilanganDua = int(input("Masukan Bilangan 2 : "))
        print("hasil = ",pyramidVol(bilanganSatu,bilanganDua))
    elif pilihan == "2":
        jumlahJari = int(input("Masukan Jari-jari : "))
        print("hasil = ",ballVol(jumlahJari))
    elif pilihan == "3":
        print("Pilihlah Salah satu dari pilihan di bawah : ")
        print("1. Prisma Segitiga")
        print("2. Prisma Segiempat")
        print("3. Prisma Segilima")
        modePrisma = int(input("Tentukan Pilihan anda : "))
        # if modePrisma in (1,2,3):
        if modePrisma == 1:
                panjangAlas = int(input("Masukan Panjang alas : "))
                tinggiPris = int(input("Masukan tinggi  : "))
                panjangPris = int(input("Masukan tinggi primas segitiga : "))
                print("hasil : ", prismaSegitiga(panjangAlas,tinggiPris,panjangPris))
        elif modePrisma == 2:
                pPrisma = int(input("Masukan Panjang  : "))
                tPrisma = int(input("Masukan Tinggi : "))
                lPrisma = int(input("Masukan Lebar : "))
                print("Hasil : ", prismaEmpat(pPrisma,tPrisma,lPrisma))
        elif modePrisma == 3:
                pPrisma = int(input("Masukan Panjang  : "))
                lPrisma = int(input("Masukan Lebar : "))   
                tPrisma = int(input("Masukan Tinggi : "))
                print("hasil : ",prismaSegilima(pPrisma,lPrisma,tPrisma))
        else :
                print("Prisma yang anda cari belum tersedia di kalkulator ini")
    elif pilihan == "4":
        jumlahJari = int(input("Masukan jari-jari : "))   
        masukanTinggi = int(input("Masukan Tinggi : "))
        print("hasil : ", volKrucut(jumlahJari,masukanTinggi)) 