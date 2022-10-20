b = 0
c = 0
nilai = 0
while b == 0: 
    a = str(input("Masukkan nilai: "))
    if a.upper() == 'A' :
        c += 1
        nilai += 4.00
        print("Nilai : 4.00")
    elif a.upper() == 'A-':
        c += 1
        nilai += 3.75
        print("Nilai: 3.75")
    elif a.upper() == 'B+':
        c += 1
        nilai += 3.50
        print("Nilai: 3.50")
    elif a.upper() == 'B' :
        c += 1
        nilai += 3.00
        print("Nilai: 3.00")
    elif a.upper() == 'B-':
        c += 1
        nilai += 2.75
        print("Nilai: 2.75")
    elif a.upper() == 'C+':
        c += 1
        nilai += 2.50
        print("Nilai: 2.50")
    elif a.upper() == 'C':
        c += 1
        nilai += 2.00
        print("Nilai: 2.00")
    elif a.upper() == 'C-':
        c += 1
        nilai += 1.75
        print("Nilai: 1.75")
    elif a.upper() == 'D':
        c += 1
        nilai += 1.50
        print("Nilai: 1.50")
    elif a.upper() == 'E':
        c += 1
        nilai += 1.25
        print("Nilai: 1.25")
    elif a == '':
        break
    else:
        print("Masukkan nilai yang benar")
        
rata = nilai/c
print(f"rata rata: {rata}")