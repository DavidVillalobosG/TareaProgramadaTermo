#Fecha de creación: 20/6/2020 2:00pm
#Última actualización: 13/7/2020
#Versión 3.8.3

#Importación de librerías

import tkinter as tk
import numpy as np
import random
import clase_simulacion

#Definición de funciones

def esCeldaLibre(matriz,fila,columna):
    #Siente que deberia ser -1 en vez de -2 pero con -1 las particulas desaparecen cuando tocan el borde
    if fila<0 or fila>(clase_simulacion.Simulacion.TAM_MATRIZ_Y -2) or columna<0 or columna>(clase_simulacion.Simulacion.TAM_MATRIZ_X -2):
        return False
    return matriz[fila,columna]==clase_simulacion.Simulacion.VALOR_CAFE 

def encontrarVecinosLibres(matriz,fila,columna):
    """
    Entrada: matriz, fila y columna de la celda
    Salida: lista de los pares ordenados de los vecinos libres
    """
    listaVecinosLibres=[]
    if esCeldaLibre(matriz,fila-1,columna):
        listaVecinosLibres.append((fila-1,columna))
    if esCeldaLibre(matriz,fila+1,columna):
        listaVecinosLibres.append((fila+1,columna))
    if esCeldaLibre(matriz,fila,columna-1):
        listaVecinosLibres.append((fila,columna-1))
    if esCeldaLibre(matriz,fila,columna+1):
        listaVecinosLibres.append((fila,columna+1))
    return listaVecinosLibres

def encontrarPosicionSiguiente(listaVecinosLibres):
    """
    listaVecinosLibres debe contener al menos un elemento
    """
    posicionLista=random.randint(0,len(listaVecinosLibres)-1)
    return listaVecinosLibres[posicionLista]

def buscarCremas(matriz):
    listaCremas=[]
    for fila in range(0,clase_simulacion.Simulacion.TAM_MATRIZ_Y-1):
        for columna in range(0,clase_simulacion.Simulacion.TAM_MATRIZ_X-1):
            if matriz[fila,columna]==clase_simulacion.Simulacion.VALOR_CREMA:
                listaCremas.append((fila,columna))
    return listaCremas

def calcularNuevaMatriz(matriz):
    listaCremas=buscarCremas(matriz)
    matrizOriginal=matriz*1
    for (fila,columna) in listaCremas:
        listaVecinosLibres=encontrarVecinosLibres(matriz,fila,columna)
        if len(listaVecinosLibres)>0:
            (nueva_fila,nueva_columna)=encontrarPosicionSiguiente(listaVecinosLibres)
            matriz[nueva_fila,nueva_columna]=clase_simulacion.Simulacion.VALOR_CREMA
    for (fila,columna) in listaCremas:
        listaVecinosLibres=encontrarVecinosLibres(matrizOriginal,fila,columna)
        if len(listaVecinosLibres)==0:
            matriz[fila,columna]=clase_simulacion.Simulacion.VALOR_CREMA
        elif len(listaVecinosLibres)>0:
            matriz[fila,columna]=clase_simulacion.Simulacion.VALOR_CAFE
    
    
    
