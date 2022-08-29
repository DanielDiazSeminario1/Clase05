# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 17:06:15 2022

@author: Sheyla
"""
# Dado el total, calcular el IGV y el subtotal
import Financieros
total = 1000.49
print(f"El subtotal es: {Financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"El IGV es: {Financieros.obtenerIGVconTotal(total): .2f}")
print(f"El total es: {total}")
