def model_perkalian():
    angka = int(input("Menampilkan model matematika dari angka: "))
    for i in range(1,11):
        hasil = angka * i
        print(f"{angka} x {i} = {hasil}")
        
def model_pembagian():
    angka = int(input("Menampilkan model matematika dengan angka: "))
    for i in range(50,66):
        hasil = float(i / angka)
        print(f"{i} : {angka} = {hasil}")


print("~~ Tabel Matematika ~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
model = input("Masukkan model matematika yang diinginkan: ")
if model != "1" and model != "2":
    print("Pilihan tidak tersedia, jangan ngasal!")
else:
    if(model == "1"): model_perkalian()
    elif(model == "2"): model_pembagian()

        
        #Edit Sedikit
        
