# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 22:03:10 2022

@author: Sheyla
"""
# Creamos el menú
import Gestion_archivos

def menu():
    print("**** MENU PRINCIAPL ****")
    print("1. Crear Archivo")
    print("2. Eliminar Archivo")
    print("3. Agregar Contenido")
    print("4. Mostrar contenido de Archivo")
    print("5. Salir")

def crear():
    print("** CREAR ARCHIVO**")
    archivo =  input("Crear archivo: ")
    contenido = input("Contenido del archivo: ")
    Gestion_archivos.crear_archivo(archivo, contenido)
    
def eliminar():
    print("** ELIMINAR ARCHIVO **")
    archivo =  input("Nombre del archivo a eliminar: ")
    Gestion_archivos.eliminar_archivo(archivo)
def agregar ():
    print("** AGREGAR ARCHIVO **")
    archivo =  input("Quiero agregar contenido al archivo: ")
    contenido = input("El contenido adicional del archivo será: ")
    Gestion_archivos.agregar_contenido(archivo, contenido)

def listar():
    print("** MOSTRAR CONTENIDO DE UN ARCHIVO **")
    archivo =  input("Quiero mostrar el contenido del archivo: ")
    print(Gestion_archivos.leer_archivo(archivo))
def salir():
    print("** GRACIAS... VUELVA PRONTO **")
def error():
    print("** OPCIÓN INCORRECTA **")

# LA LOGICA PARA EL MENU DE OPCIONES
opcion = 1
while opcion != 5:
    menu()
    opcion = int(input(" Seleccione una opción [1-5]: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5: 
        salir()
    else: 
        error()
    