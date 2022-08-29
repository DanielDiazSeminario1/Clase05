# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:51:40 2022

@author: Sheyla
"""
""" creamos un archivo txt llamado noticia en el cual pondremos 
la noticia de cualquier página, una vez hecho eso pondremos el siguiente
código para abrir el archivo"""
noticia =  open("noticia.txt","rt",encoding = 'utf8')
mostrar_texto = noticia.read()
print(mostrar_texto)    