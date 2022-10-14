print("This Program will determine the number of days of a given a month")
print("Enter -1 to stop the program")
Bulan = int(input("Enter the month(1-12): "))

while Bulan >= 0 or Bulan < -1:
    if Bulan >= 13 or Bulan == 0 or Bulan < -1:
        print("Invalid value entered : ",Bulan)
    elif Bulan in (1,3,5,7,8,10,12):
        print("There are 31 days in the Month")
    elif Bulan in (4,6,9,11):
        print("There are 30 days in the Month")
    elif Bulan == 2:
        Tahun = int(input("Please enter the year (e.g., 2021): "))
        if (Tahun % 4 == 0 ):
                print("There are 29 days in the Month")
        else:
                print("There are 28 days in the Month")
    print("Enter -1 to stop the program")
    Bulan = int(input("Enter the month(1-12): "))
while Bulan == -1:
    print("Terima kasih telah menggunakan program saya. Sampai berjumpa lagi")
    Bulan += 1