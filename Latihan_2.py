inputName = input("Enter Your Name : ")
if inputName == ("Bond"):
    print("Welcome Agent 007")
else:
    print("Welcome", inputName)


inputNilai = int(input("Masukan Nilai : "))
if inputNilai / 2 == 0:
    print("Genap")
else:
    print("Ganjil")

masukanAngka = input("Masukan Angka : ")
if '.' in masukanAngka:
    masukanAngka = float(masukanAngka)
    print("Bilangan Desimal")
else:
    masukanAngka = int(float(masukanAngka))
    print("Bilanga Bulat")
