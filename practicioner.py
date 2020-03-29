#identacion
if 5 > 2:
    print ("5 es mas grsnde que 2")

print("\n")

#variables
print("muestra valo de una variable:")
x = 'Fulano'

print(x)

print("\n")

#asigna valores en multiples variables
print("asigna valores a varisbles inline")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("\n")

#condicional if
print("condicional if")

a = 200
b = 33

if b > a:
  print("b es mas grande que a")
else:
  print("b es menor que a")
 

print("\n")

#concatenar
# en texto los une, en numeros los suma
print("concatena valores")
x = "Armando "
y = "CM"
z =  x + y
print(z)

print("\n")

#suma
print("suma 5 + 5")
x = 5
y = 5
z = x + y
print(z)
print("\n")

print("uso de var += num")
age = 30
age += 20
#age = age + 20
print (age)
print('\n')

#funciones
# define una variable fuers de ls funcion
print("funciones")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#definen var fuera de la funciom y renombrada dentro de la funcion
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# listas
myList = [1, 2, 3, 4]
A = [myList] * 3
print(A)

myList[ 2 ] = 45
print(myList)

print("\n")

myList = [1024, 3, True, 6.5]

print("\n")
print("puzzle 2")

n, count = 5, 0
for _ in range(n):
	n -= 1
	count +=1
print(count)

print("\n")
# inputs
print("inputs")
print("\n")

name = input("escribe tu nombre:")
print(" tu nombre es", name, "y tiene", len(name), "letras")

print("\n")
age = input("digita tu edad")
age = int(age) 
print("%s is %d years old." % (name, age))