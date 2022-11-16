# #Ejercicio 1
# print ("Hello World")

# #Ejercicio 2
# print(3+4)

# #Ejercicio 3
# nombre = input("Ingrese su nombre ")
# print ("Hola ",nombre)

# # ejercicio 4
# n1= int(input("un numero "))
# n2= int( input("otro numero "))
# print(n1+n2)

# #ejercicio 5
# n1= int(input("un numero "))
# n2= int( input("otro numero "))
# if (n1 > n2):
#     print (n1)
# else:
#     print(n2)

# #ejercicio 6
# n1= int(input("un numero "))
# n2= int(input("otro numero "))
# n3= int(input("otro mas "))
# lista = [n1,n2,n3]
# lista.sort(reverse=True)
# print("El mayor es: ",lista[0])

# #Ejercicio 7
# n1= int(input("un numero "))
# if (n1 % 2 == 0):
#     print("Es par")
# else:
#     print("No es par")

# #Ejercicio 8
# numeros = [2,3,5,7]
# n1= int(input("un numero "))
# for num in numeros:
#     if (n1 % num == 0):
#         print("Es divisible")
#         break

# #Ejercicio 9
# numeros = [2,3,5,7]
# ninguno = True
# n1= int(input("un numero "))
# for num in numeros:
#     if (n1 % num == 0):
#         print("Es divisible por ", num)
#         ninguno= False
# if ninguno:
#     print("no es divisible por ninguno")

# #Ejercicio 10
# n1= int(input("un numero "))
# i = 1
# while n1 > i :
#     if n1 % i == 0:
#         print("Es divisible por ", i)
#     i=i+1

# #Ejercicio 11
# n1= int(input("un numero "))
# primo = "es"
# i = 2
# while n1 > i :
#     if n1 % i == 0:
#         primo = "NO es"
#         break
#     i=i+1
# print("El numero ", n1, primo, "primo")

# #Ejercicio 12
# n1= float(input("un numero "))
# if n1 <= 3:
#     print("deficiente")
# elif n1 <= 5:
#     print("Insuficiente")
# elif n1 <= 6:
#     print("Suficiente")
# elif n1 <= 7:
#     print("Bien")
# elif n1 <= 9:
#     print("Notable")
# elif n1 <= 10:
#     print("Sobresaliente")  
# else: 
#     print("nota inventada")      

# #Ejercicio 13
# i=1
# while i <= 30 :
#     cadena = ""
#     o= 1
#     while o<=i:
#         cadena =cadena + str(i)
#         o+=1
#     print(cadena)
#     i+=1

# #Ejercicio 14
# n1= int(input("un numero "))
# while n1 >= 1 :
#     cadena = ""
#     o= 1
#     while o<=n1:
#         cadena =cadena + str(n1)
#         o+=1
#     print(cadena)
#     n1-=1

#Ejercicio 15
for i in range(1,501):
    cadena = ""
    if i % 4 == 0:
        cadena = cadena + " - Multiplo de 4"
    if i % 9 == 0:
        cadena = cadena + " - Multiplo de 9"
    print(str(i)+cadena)      
    if i % 5 == 0:
        print("---------------------------------------------------")  
    