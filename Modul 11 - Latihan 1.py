class Student:
    'Common base class for all employees'
    stdCount = 1
    
    def __init__(self, Name, NIM, Angkatan):
        self.Name = Name
        self.NIM = NIM
        self.Angkatan = Angkatan
        Student.stdCount = +1
        
    def displayStudent(self):
        print ("Name", self.Name, "NIM", self.NIM, "Angkatan", self.Angkatan)
    
Name = input("Masukkan Nama:")
NIM = input("Masukkan NIM:")
Angkatan = input("Angkatan Tahun:")

std=Student(Name ,NIM , Angkatan)
std.displayStudent()
print("Total Student %d" % Student.stdCount) 
        
    