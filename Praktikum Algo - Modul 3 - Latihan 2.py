
import math

A = int(input("Masukan nilai A: "))
B = int(input("Masukan nilai B: "))
C = int(input("Masukan nilai C: "))

if (A == 0):
    print("Bukan  Merupakan Persamaan Kuadrat")
    
else:
    D = pow(B, 2)-(4*A*C)
    if (D == 0):
        x1 = (-B)/(2*A)
        x2 = x1
        print("Persamaan kuadrat " + str(A) + "x^2 + (" + str(B) + ")x + " + str(C))
        print("Determinannya = " + str(D))
        print("Merupakan Akar Kembar")
        print("Akar = " + str(x2))
    elif (D < 0):
        print("Persamaan kuadrat " + str(A) + "x^2 + " + str(B) + "x + " + str (C))
        print("Determinannya = " + str(D))
        print("Merupakan Akar Imaginer")
        print("Akar x1 = -" + str(B) + " + Akar" +  str(D) + "/2*" + str (A))
        print("Akar x2 = -" + str(B) + " - Akar" +  str(D) + "/2*" + str (A))
    elif (D > 0):
        x1 = ((-B)+math.sqrt(D))/(2*A)
        x2 = ((-B)-math.sqrt(D))/(2*A)
        print("Persamaan kuadrat " + str(A) + "x^2 + " + str(B) +"x + " + str(C))
        print("Determinannya = " + str(D))
        print("Memiliki Akar Berbeda")
        print("Akar x1 = " + str(x1))
        print("Akar x2 = " + str(x2))
    
    
    
