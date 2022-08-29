# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:24:40 2022

@author: Sheyla
"""
# como voy a agregar algo a un archivo creado uso at
# \n es para agregar el contenido en una linea final
archivo = open("noticia.txt","at")
contenido = "\nFuente: RPP"
archivo.write(contenido)
archivo.close()
