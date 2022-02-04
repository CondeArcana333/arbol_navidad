# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:19:35 2021

@author: Daniel
"""

n=2
a=int(input("escribe un numero"))
ciclo=True
while ciclo:
    if a%n==0:
        print("no es primo ")
        n=n+1
        ciclo=False
    elif a%n!=0:
        print("es primo")
        ciclo=False
        