# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:14:41 2022

@author: Sheyla
"""
# creamos un archivo txt mediante spyder
# llenamos con texto dicho archivo
#el archivo es de tipo escritura lleva wt
archivo = open("archivo_de_prueba.txt","wt")
contenido = "Linea1 hola amigos ¿Cómo están?\nLinea2 Bienvenidos"
archivo.write(contenido)
archivo.close()
