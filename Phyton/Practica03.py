# # Ejercicio 1 al 5
# class Persona:
#     def set_nombre(self,nombre):
#         self.nombre=nombre
    
#     def set_edad(self,edad):
#         self.edad=edad
    
#     def get_nombre(self):
#         return (self.nombre)
    
#     def get_edad(self):
#         return (self.edad)
    
#     def print_persona(self):
#         print("Nombre:", self.get_nombre(), "- Edad:", self.get_edad())

#     def __init__(self,nombre,edad):
#         self.set_edad(edad)
#         self.set_nombre(nombre)
        
#     def es_mayor_de_edad (self):
#         return(self.edad >= 18)
    
#     def es_mayor_que (self, otraPersona):
#         return(self.edad > otraPersona.edad)
    
    
# def getMayor(p1,p2):
#     if p1.edad > p2.edad:
#         return p1
#     else:
#         return p2

# Persona1= Persona("Abuelito",90)
# Persona2= Persona("Heidi", 12)
# Persona3= Persona("Pedro",13)

# Persona1.print_persona()
# Persona2.print_persona()
# Persona3.print_persona()
# print("Es mayor de edad",Persona2.es_mayor_de_edad())
# print("Es mayor que",Persona3.es_mayor_que(Persona2))
# getMayor(Persona1, Persona2).print_persona()

# # Ejercicio 6
# class Alumno:
#     def __init__(self, nombre, nota):
#         self.nota=nota
#         self.nombre=nombre
    
#     def verNota(self):
#         return(self.nota)

#     def verNombre(self):
#         return(self.nombre)

#     def imprimir(self):
#         print("Nombre:", self.nombre, "- Nota:", self.nota)
    
#     def aprobado(self):
#         return(self.nota > 6)
    
# Alumno1=Alumno("Pablo",9)
# Alumno1.imprimir()
# print("Aprobado:", Alumno1.aprobado())

# #Ejercicio 7
# class Triangulo:
#     def __init__(self,a,b,c):
#         self.lados=[a,b,c]
   
#     def ladoMayor(self):
#         mayor=0
#         for x in self.lados:
#             if x > mayor:
#                 mayor= x
#         return(mayor)
    
#     def tipoTriangulo(self):
#         max=0
#         for x in self.lados:
#             o = 0
#             for y in self.lados:
#                 if x == y:
#                     o +=1
#             if o > max:
#                 max = o
#         if max == 1:
#             return("Escaleno")
#         elif max == 2:
#             return("Isoceles")
#         else:
#             return("Equilatero")

# t1=Triangulo(1,1,1)
# t2=Triangulo(2,1,1)
# t3=Triangulo(3,2,1)
# print(t1.tipoTriangulo())
# print(t2.tipoTriangulo())
# print(t3.tipoTriangulo())        

# #Ejercicio 8
# class Calculadora:
#     def __init__(self, op1, op2):
#        self.a=op1
#        self.b=op2
#        print("Suma",self.suma())
#        print("Resta",self.resta())
#        print("Division",self.division())
#        print("Multiplicacion",self.multiplicacion())
    
#     def suma(self):
#         return(self.a+self.b)
    
#     def resta(self):
#         return(self.a-self.b)
    
#     def multiplicacion(self):
#         return (self.a*self.b)

#     def division(self):
#         return (self.a/self.b)
    
# n1= int(input("un numero "))
# n2= int( input("otro numero "))
# calcu=Calculadora(n1,n2)