# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:37:56 2020

@author: Rony
"""


numero1=float(input('Ingrese primer valor : '))
numero2=float(input('Ingrese suegundo valor : '))

def suma(a,b):
  return a+b
adicion=round(suma(numero1,numero2),2)

def res(a,b):
  return a-b
diferencia=round(res(numero1,numero2),2)

def prod(a,b):
  return a*b
producto=round(prod(numero1,numero2),2)

def division(a,b):
    return a/b
division=round(division(numero1,numero2),2)

def raiz(a,b):
  return a**(1/b)
raiz=round(raiz(numero1,numero2),2)

def exponente(a,b):
  return a**b
exponente=round(exponente(numero1,numero2),2)

def CocienteDeLaDivision(a,b):
  return a//b
CocienteDeLaDivision=CocienteDeLaDivision(numero1,numero2)

def residuo(a,b):
  return a%b
residuo=round(residuo(numero1,numero2),2)

def maximo(a,b):
  return max(a,b)
maximo=round(maximo(numero1,numero2),2)

def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice] #le damos la posicion indice en la lista de operadoes
     posicion = indice

     while posicion>0 and unaLista[posicion-1]>valorActual: 
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1

     unaLista[posicion]=valorActual
     
     
listaSinOrdenar=[adicion,diferencia,producto,division,raiz,exponente,CocienteDeLaDivision,residuo,maximo]

unaLista =[adicion,diferencia,producto,division,raiz,exponente,CocienteDeLaDivision,residuo,maximo]

ordenamientoPorInsercion(unaLista)

print('-------------------------------------------------------------------------------------------')
print(listaSinOrdenar)
print('-------------------------------------------------------------------------------------------')
print(unaLista)