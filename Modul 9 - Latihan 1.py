def data(Nama,Umur,Alamat,Email,DosenWali):

    file = open('Biodata.txt','w' )
    file.write(f'\nNama : {Nama} \nUmur : {Umur} \nAlamat : {Alamat} \nEmail : {Email} \nDosenWali : {DosenWali}')
    file.close()
 
    file = open('Biodata.txt','r')
    text = file.read()
    print(text)
    file.close()

Nama = input("Masukkan Nama: ")
Umur = input("Masukkan Umur: ")
Alamat = input("Masukkan Alamat: ")
Email = input("Masukkan Email: ")
DosenWali = input("Masukkan Dosen Wali: ")
print('\nBerikut Biodatamu')
data(Nama,Umur,Alamat,Email,DosenWali)
