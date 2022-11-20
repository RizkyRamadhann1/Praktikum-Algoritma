# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:40:49 2022

@author: Rizky Ramadhan
"""

def penjumlahan(angka = 0, jml = 0, i = 1):
    if (jml <= 0):
        return 0
    else:
        angka = int(input("Masukkan bilangan ke-" + str(i) + ":"))
        if(jml == 1):
            return angka
        else:
            i += 1
            return angka + penjumlahan(angka, jml-1, i)
        
jumlah = int(input("Masukkan Jumlah: "))
nilai = penjumlahan(jml = jumlah)
print("Hasil dari penjumlahan adalah: " + str(nilai))
