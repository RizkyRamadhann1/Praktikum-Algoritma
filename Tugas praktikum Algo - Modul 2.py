import math as m 

print("Menghitung jarak antara dua titik di permukaan bumi") 
L1 = float(input("Masukkan lintang kota pertama: ")) 
B1 = float(input("Masukkan Bujur kota pertama: ")) 
L2 = float(input("Masukkan lintang kota kedua: ")) 
B2 = float(input("Masukkan Bujur kota kedua: ")) 

a = L2 - L1 
b = B2 - B1 

rumus = m.sin(m.radians(a/2))**2
m.cos(m.radians(L1))*m.cos(m.radians(L2))*m.sin(m.radians(b/2))**2 
rumus1 = 2*m.asin(m.sqrt(rumus)) 
r = 6371.01 

hasil = rumus1*r 
print("\nJarak antara dua titik adalah: ",abs(hasil),"Km") 