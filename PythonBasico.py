#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 16:34:57 2020

@author: breyneroc
"""

""" Sintaxis basica en python """


print("Hola mundo")

# Ingresar datos por teclado
# nombre= input("Ingresar nombre: ")
# print(nombre)

# Python no se declaran variables pero siguen siendo
# iguales a C

numeroC= 3+4j

# Python tiene tipo de dato comlejo
# Type consulta el tipo de dato 

print(type(numeroC))

# Ciclos


for i in range(20):
    print(i)
    
print("Ciclos for")
for i in range(1,20,2):
    print(i)

print("Ciclos while")

i=0

while (i<20):
    print(i)
    # i+=1 es similar a i++ en C
    i+=2

# CONDICIONALES
a,b= 4, 10
c= 2
d= 8

if(a<b):
    print(a)

else:
    print(b)
   
    # elif sirve para hacer mas condicionales
if c<=d:
    print(c)
elif c==2:
    print(True);
    
# Funciones
print("FUNCIONES")
def num(x):
    c=1
    k=c+x
    return k

print(num(1))

# estructuras de datos
# SIMILAR A LOS ARREGLOS
# LISTAS

print("Tipos de estructuas de datos")
p=[]
j=[1,2,3]
print(j)
print(p)
print("mutable")
j[1]=100
print(j)
print(type(p))
# TUPLAS 
print("Tuplas")
u=(1,2,3)
o=()

print(type(o))

print(u)


## COJUNTOS
w={1,2,3,4,5}
print(w)

print(w)
print(type(w))
# DICIONARIOS
Dic={'Nombre': "Euler",'valor':2.718281}
print(Dic)
print(type(Dic))

print("Consultar como agregar y eliminar datos en las estructuras")

# DOCUMENTACION OFICIAL
#https://docs.python.org/3/contents.html

# LIBRERIAS

import math as ma

#Libreria  matematica
# as sirve para renombrarla para invocar mas facil
print(ma.pi)

# Para consultar de forma rapida que funciones contiene una libreria
# utlizamos la funcion dir()

print(dir(ma))
# Para saber que hace cada una de estas funiones
# utilizamos la funcion help()

#print(help(ma))
help(ma)
# Lo recomendable es visitar la pagina oficial de cada libreria
# como numpy, matplotlib, etc en internet

#Para instalar librerias se puede ir a las paginas oficiales

# o instalrlo por terminal usando un instalador de paquetes 
# CMD o Bash
# Puede ser conda o pip 
# conda install numpy 
# pip install numpy
