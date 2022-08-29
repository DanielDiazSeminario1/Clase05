# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 16:59:09 2022

@author: Sheyla
"""
# Importamos la libreria camelcase
import camelcase
# Hacer una cadena llamada nombre
nombre = "daniel omar diaz seminario"
# mostrar en mayúscula
print(nombre.upper())
# que nos muestre en formato título
# las primeras letras de cada palabra se muestra
# en mayuscula cuando está en formato título
print(nombre.title())
#Necesitamos crear un objeto llamado cam
cam = camelcase.CamelCase()
print("con camelcase:... ")
# Imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# Al definir el objeto, incluimos los argumentos
#'daniel' y 'omar'
cam2 = camelcase.CamelCase('daniel','omar')
print(cam2.hump(nombre))
