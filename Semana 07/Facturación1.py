# -*- coding: utf-8 -*-
"""

"""
#Dado el subtotal, calcular el IGV y el total
import Financieros
subtotal = 800.77
print(f"el subtotal es: {subtotal}")
print(f"el igv es: {Financieros.obtenerIGVSubtotal(subtotal): .2f}")
print(f"el total es: {Financieros.obtenerTotalconSubtotal(subtotal): .2f}")

