try:
    def perpangkatan():
        print('\nIni merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti')
        angka = input("Masukkan angka: ")
        if angka == '':
            print("Program selesai")
            return 0
        pangkat = input("Masukkan perpangkatan: ")
        hasil = int(angka) ** int(pangkat)
        print(f'hasil perpangkatan: {(hasil)}')
        perpangkatan()
    perpangkatan() 
except:
    print("Perpangkatan harus di isi dan dalam bentuk bilangan bulat")
    perpangkatan()