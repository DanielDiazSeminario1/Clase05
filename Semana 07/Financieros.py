# -*- coding: utf-8 -*-
"""
Los módulos me permitirán crear librerias
de funcionalidades que puedas utilizar o reutilizar
en cualquier momento
"""
"""Variable"""
igv = 0.18

def obtenerIGVSubtotal(subtotal):
    return subtotal*igv
def obtenerTotalconSubtotal(subtotal):
    # Subtotal + igv*subtotal
    # Subtotal*(1+0.18)
    return subtotal*(1+igv)
def obtenerSubtotalconTotal(total):
    return total/(1+igv)
def obtenerIGVconTotal (total):
    return total - obtenerSubtotalconTotal(total)
