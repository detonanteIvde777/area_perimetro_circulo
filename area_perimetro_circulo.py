#programa para calcular el area y el permetro de un circulo

# libreria
import math 


print("                           ")
print("  Area y perimtro del circulo  ")
print("                           ")

# imput
r = imput("Ingrese el valor del radiodel circulo: ")
r = int(r)

#procedimiento
a = math.pi*r*r
p = 2*math.pi*r

# output
print("                                     ")
print("             resultados              ")
print("                                     ")
print("El area del circulo es: " + str(a))
print("El perimetro delcirculo es: " + str(p))
print("                                     ")