# #Ejercicio 1
# def tresNumeros(a,b,c):
#     lista=[a,b,c]
#     lista.sort(reverse=True)
#     if lista[0]>lista[1]:  
#         return (lista[0])
#     else:
#         return (-1)

# a = int(input("Ingrese un numero "))
# b = int(input("Ingrese un numero "))
# c = int(input("Ingrese un numero "))
# print("El mayor es ", tresNumeros(a,b,c))

# #Ejercicio 2
# from datetime import datetime

# def validarFecha(a,b,c):
        
#     while True:
#         try:
#             fecha_texto = a+"/"+b+"/"+c
#             fecha=datetime.strptime(a+"/"+b+"/"+c, '%d/%m/%Y')
#             return (True)
#         except ValueError:
#             return(False)

# a = (input("Ingrese un numero "))
# b = (input("Ingrese un numero "))
# c = (input("Ingrese un numero "))
# print("El resultado es", validarFecha(a,b,c))

# #Ejercicio 3
# def calcularCambio(costo, monto):
#     billetes=[500,100,50,20,10,5,1]
#     vuelto = monto-costo
#     for billete in billetes:
#         i= 0
#         while vuelto >= billete:
#             i+=1
#             vuelto -=billete
#         if i >0:
#             print("Entregar ", i," billetes de ", billete)

# a = int(input("Ingrese un valor "))
# b = int(input("Ingrese un pago "))
# if b > a:
#     calcularCambio(a,b)
# else:
#     print("no alcanza")

# #Ejercicio 4
# def cuadrado(n):
#     i=0
#     while i < n:
#         print("**********")
#         i+=1

# def triangulo(n):
#     i=1
#     while i<=n:
#         o=1
#         cadena ="**"
#         while o < i:
#             cadena+="**"
#             o+=1
#         print(cadena)
#         i+=1

# a = int(input("Ingrese un numero "))
# cuadrado(a)
# a = int(input("Ingrese un numero "))
# triangulo(a)

# # Ejercicio 5
# a = int(input("Ingrese un numero "))
# cuadrado= lambda x: x**2
# print(cuadrado(a)==(a**2))

# #Ejercicio 6
# a = int(input("Ingrese un numero "))
# esPar = lambda x: x%2==0
# print(esPar(a)==(a % 2 == 0))

# #Ejercicio 7
# lista=[]
# a = int(input("Ingrese un numero "))
# i=1
# cuadrado = lambda x: x**2
# while i <= a:
#     lista.append(cuadrado(i))
#     i+=1
# lista.sort
# print(lista[-1:-10:-1])
# print(lista[-9:])

# #Ejercicio 8
# lista1=["Alfa","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Julliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-Ray","Yankee","Zulu"]
# lista2=["Whiskey","Romeo","Zulu"]

# def limpiaListas(l1,l2):
#     print(l1)
#     print(l2)
#     limpia = lambda x,y: x.remove(y)
#     for palabra in l2:
#         limpia(l1,palabra)
#     print(l1)

# limpiaListas(lista1, lista2)

# #Ejercicio 9
# lista1=["Alfa","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Julliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-Ray","Yankee","Zulu"]
# lista2=["Whiskey","Romeo","Zulu"]

# def ordenada(lista):
#     i=lista[0]
#     result=True
#     for x in lista:
#         if i > x:
#             result=False
#             break
#         i=x
#     return(result)

# print(ordenada(lista1))
# print(ordenada(lista2))

# #Ejercicio 10
# def capicua(palabra):
#     result=True
#     fin=len(palabra)-1
#     for x in palabra:
#         if x != palabra[fin]:
#             result=False
#             break
#         fin -=1
#     return(result)

# print("kayak",capicua("kayak"))
# print("elefante",capicua("Elefante"))

# #Ejercicio 11
# entrada=input("Ingrese cadena ")
# algo=int((80-len(entrada))/2)
# espacios=""
# i=0 
# while i < algo:
#     espacios +=" "
#     i+=1
# print(espacios,entrada)

# #Ejercicio 12
# def fechaLinda(tupla):
#     meses=["Enero","Febrero","Marzo", "Abril","Mayo", "Junio", "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
#     print(tupla[0],"de",meses[int(tupla[1])-1],"de 20"+tupla[2])

# fechaLinda(["07","11","22"])
# fechaLinda(["12","10","17"])
# fechaLinda(["13","02","18"])

# #Ejercicio 13
# frase=input("Ingrese cadena ")
# frase = "mi vieja mula ya no es lo que era ya no es lo que era"
# conjunto = set(frase.split())
# print(sorted(sorted(conjunto),key=len))

# #Ejercicio 14
# def limpiar(diccionario, claves):
#     exito=False
#     for x in claves:
#         if x in diccionario:
#             diccionario.pop(x)
#             exito=True
#     return(exito)

# dict={
#   "a": "Alfa",
#   "b": "Bravo",
#   "c": "Charly",
#   "d": "Delta",
#   "e": "Echo",
#   "f": "Foxtrot"
# }
# clavs=["g","z"]

# print(dict)
# print(clavs)
# print(limpiar(dict,clavs))
# print(dict)

# #Ejercicio 15
# def recortar(cadena, inicio, cantidad):
#     return(cadena[0:inicio]+cadena[inicio+cantidad:])
    
# frase="Mi vieja mula ya no es lo que era ya no es lo que era ya no es lo que era"
# #frase="1234567890123456789012345678901234567890"
# print(recortar(frase, 15, 7))

