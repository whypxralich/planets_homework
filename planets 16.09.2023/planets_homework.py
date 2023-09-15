import math
G = 6.673 * 10 **(-11)
m1 = 5.97600 * math.pow(10, 24)
m2 = float(input("Write the mass of another planet: "))
R = float(input("Write the distance to another planet: "))
F = (G * m1 * m2)/(R**2)
print (F)
