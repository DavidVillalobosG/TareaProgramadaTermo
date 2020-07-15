#Fecha de creación: 19/6/2020 9:30pm
#Última actualización: 13/7/2020
#Versión 3.8.3

#Importación de librerías

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from funciones import calcularNuevaMatriz

#Definición de la clase Simulacion

class Simulacion:
    
    """Definición de atributos"""
    
    TAM_MATRIZ_X = 100
    TAM_MATRIZ_Y = 100
    TAM_GOTA_X = 10
    TAM_GOTA_Y = 10
    TAM_PIXELS = 8
    VALOR_CAFE = 0
    VALOR_CREMA = 1
    COLOR_CAFE = "brown4"
    COLOR_CREMA = "linen"
    ESPERA = 0
    iteraciones = 0
    
    """Definición de métodos"""
    
    def __init__(self):
        """Creación de la matriz"""
        self.inicializarMatriz()
        """Creación de la ventana de simulación"""
        self.ventana = tk.Tk()
        self.canvas = tk.Canvas(width=self.TAM_MATRIZ_X*self.TAM_PIXELS,height=self.TAM_MATRIZ_Y*self.TAM_PIXELS,bg=self.COLOR_CAFE)
        self.canvas.pack()
        self.dibujarMatriz()
        """Iniciar main loop"""
        self.ventana.after(self.ESPERA,self.animarMatriz)
        self.ventana.mainloop()
        
    def inicializarMatriz(self):
        """Café"""
        self.matriz = np.ones((self.TAM_MATRIZ_X,self.TAM_MATRIZ_Y))*self.VALOR_CAFE
        """Gota de crema en el café"""
        for x in range(self.TAM_MATRIZ_X//2-self.TAM_GOTA_X//2,self.TAM_MATRIZ_X//2+self.TAM_GOTA_X//2):
            for y in range(self.TAM_MATRIZ_Y//2-self.TAM_GOTA_Y//2,self.TAM_MATRIZ_Y//2+self.TAM_GOTA_Y//2):                         
                self.matriz[x,y]=self.VALOR_CREMA

    def dibujarMatriz(self):
        """Café"""
        self.canvas.delete("all")
        """Crema"""
        for x in range(0,self.TAM_MATRIZ_X - 1):
            for y in range(0,self.TAM_MATRIZ_Y - 1):
                if self.matriz[x,y] == self.VALOR_CREMA:
                    x_inicio = x*self.TAM_PIXELS
                    y_inicio = y*self.TAM_PIXELS
                    self.canvas.create_rectangle(x_inicio,y_inicio,x_inicio+self.TAM_PIXELS-1,y_inicio+self.TAM_PIXELS-1,outline=self.COLOR_CREMA,fill=self.COLOR_CREMA)
        tk.Label(self.canvas,text=self.iteraciones).place(x=20,y=20)

    def animarMatriz(self):
        self.actualizarMatriz()
        self.ventana.after(self.ESPERA,self.animarMatriz)
                    
    def actualizarMatriz(self):
        calcularNuevaMatriz(self.matriz)
        self.iteraciones=self.iteraciones+1
        self.dibujarMatriz()
        self.entropia()
        self.contarentropia()
        if self.iteraciones < 20001:
            plt.scatter(x=self.iteraciones, y=self.ENTROPIA_ITERACION)
            plt.pause(0.0000001)

    def entropia(self):
        self.LISTA_ENTROPIA = []
        self.CONTADOR_ENTROPIA = 0
        self.ENTROPIA_SECTOR = 0
        for k in range(0,10):
            for i in range(10*k,(10+10*k)):
                for m in range(0,10):
                    for j in range(10*m,(10+10*m)):
                        if self.matriz[i][j] == self.VALOR_CREMA:
                            self.CONTADOR_ENTROPIA = self.CONTADOR_ENTROPIA + 1
                self.PROB_SECTOR = self.CONTADOR_ENTROPIA/100
                self.LISTA_ENTROPIA.append(self.PROB_SECTOR)
                self.CONTADOR_ENTROPIA = 0
                self.ENTROPIA_SECTOR = 0


    def contarentropia(self):
        while 0 in self.LISTA_ENTROPIA: self.LISTA_ENTROPIA.remove(0)
        self.ENTROPIA_ITERACION = 0
        for i in range(len(self.LISTA_ENTROPIA)):
            self.ENTROPIA_ITERACION = self.ENTROPIA_ITERACION + (self.LISTA_ENTROPIA[i]*np.log(self.LISTA_ENTROPIA[i]))
        self.ENTROPIA_ITERACION = -1*self.ENTROPIA_ITERACION
    


             


  
                                 
                                 
                                 
                                 
    
    
