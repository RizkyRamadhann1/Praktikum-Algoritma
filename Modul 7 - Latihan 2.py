# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:39:05 2022

@author: Rizky Ramadhan
"""

print('Ordinal Number')
print('Ketik 0 untuk menghentikan program')
def angka(nomor):
    a = nomor % 10
    if a == 1:
        return nomor,'st'
    elif a == 2:
        return nomor,'nd'
    elif a == 3:
        return nomor,'rd'
    elif a in range(4,21) or a == 0:
        return nomor,'th'
while True:
    try:
        nomor = abs(int(input('Masukan angka: ')))
        print(angka(nomor))
        if nomor == 0:
            print('Terima kasih telah menggunakan program saya')
            break
    except:
        print('Error -> inputan harus dalam bentuk angka dan tidak kurang dari 0')