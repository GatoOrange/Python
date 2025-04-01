##Holaa Aritmetica basica
##git add #git commit -m "blablabla" ##git push 
x = 2
b = x + 4
print (b)
print (float(17) + 23)
s = 117
print (s)
print (type (s))
l = float (s)
print (l)
print (type(l))
#String
d="123"
print (d)
print (type (d))
f = int(d)
print (type(f))
print (f + 545)

#Input

Nam = input ("¿Quién eres? ")

print ("Bienvenido", Nam)

x = 1 + 2 * 3 - 8 / 4
print (x)


#Condicional

x = input ("Ingrese un número: ")
Y = int(x)

if Y <10:
    print("pequeño")
if Y > 20: 
    print("Grandote")

print("Fin de la cita.")

#Comparasion Operators 

x = (int(input("Escriba un número de 1 a 10: ")))
print (type(x))
if x == 5 :
    print ("Igual a 5")
if x > 4:
    print ("Mayor que 4")
if x >= 5:
    print ("Es igual o mayor a 5")
if x < 6 :
    print ("Es menor que 6")
if x <= 5: 
    print ("Es igual o menor a 5")
if x != 6:
    print ("No es igual a 6")


#if else elif 

j = int(input ("Elija un número del 1 al 20: ") )
if j < 5 :
    print ("Pequeño")
elif j < 15 :
    print ("Mediano")
else:
    print ("Grande")
print ("Es todo :D")