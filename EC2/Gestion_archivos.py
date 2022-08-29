# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:45:55 2022

@author: Sheyla
"""
#Creamos los métodos
# para crear archivo, recibe como parametro el nombre
# del archivo y el contenido del archivo
import os  
def  crear_archivo(nombre,contenido):
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()
# Para eliminar recibe como parametro el nombre del archivo
# a eliminar
def eliminar_archivo(nombre):
    os.remove(nombre)
# Para agregar contenido a un archivo plano, debe existir un archivo
# se envia como parámetro el nombre y el contenido del archivo
def agregar_contenido(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()
# Para leer un archivo, ya debe de existir un archivo plano
#(ejemplo: .txt, py, java)
# Recibe como parámetro el nombre del archivo a leer
# y devuelve el contenido del archivo
def leer_archivo(nombre):
    archivo = open(nombre, "rt", encoding='utf8')
    contenido =  archivo.read()
    return contenido
