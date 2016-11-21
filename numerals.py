#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

"""
Para convertir un número en una cadena literal del número.

Convertido de clipper a python en Septiembre 2001
por Chema Cortes
"""


__author__ = 'Chema Cortés'
__date__ = 'Agosto 1995'
__modified_by = 'Juan Ignacio Rodríguez de León'

_n1 = ("un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho",
       "nueve", "diez", "once", "doce", "trece", "catorce", "quince",
       "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte")

_n11 = ("un", "dós", "trés", "cuatro", "cinco",
        "séis", "siete", "ocho", "nueve")

_n2 = ("dieci", "veinti", "treinta", "cuarenta", "cincuenta", "sesenta",
       "setenta", "ochenta", "noventa")

_n3 = ("ciento", "dosc", "tresc", "cuatroc", "quin", "seisc",
       "setec", "ochoc", "novec")


def numeral(numero, en_femenino=False):
    '''
    Obtiene a partir de un número su representacón textual

    - numero        Número a convertir (entero)
    - en_femenino   True si el Literal se desea en femenino
                    P.e.:   201     -->    "doscientas una"
                    por defecto False

    >>> from numerals import numeral
    >>> print numeral(201)
    doscientos uno
    >>> print numeral(1111)
    mil ciento once
    >>> print numeral(0)
    cero
    >>>
    '''

    if numero < 0:
        resultado = "menos "+aux_numeral(-numero, en_femenino)
    elif numero == 0:
        resultado = "cero"
    else:
        resultado = aux_numeral(numero, en_femenino)

    # Excepciones a considerar
    if not en_femenino and numero % 10 == 1 and numero % 100 != 11:
        resultado += "o"
##    if 'veintiun billones ' in resultado:
##        resultado = resultado.replace('veintiun billones ', 'veintiún billones ')
    if 'veintiun ' in resultado:
        resultado = resultado.replace('veintiun ', 'veintiún ')
    return resultado


# Función auxiliar recursiva
def aux_numeral(n, en_femenino=0):

    # Localizar los billones
    prim, resto = divmod(n, 1000000000000)
    if prim != 0:
        if prim == 1:
            resultado = "un billón"
        else:
            resultado = aux_numeral(prim, False) + " billones"  # Billones siempre es masculino
        if resto!=0:
            resultado += " "+aux_numeral(resto, en_femenino)
    else:  # Localizar millones
        prim, resto = divmod(n, 1000000)
        if prim != 0:
            if prim == 1:
                resultado = "un millón"
            else:
                resultado = aux_numeral(prim, False) + " millones"  # Millones es masculino
            if resto != 0:
                resultado += " " + aux_numeral(resto, en_femenino)
        else:  # Localizar los miles
            prim, resto = divmod(n, 1000)
            if prim != 0:
                if prim == 1:
                    resultado = "mil"
                else:
                    resultado = aux_numeral(prim, en_femenino) + " mil"
                if resto != 0:
                    resultado += " " + aux_numeral(resto,en_femenino)
            else:  # Localizar los cientos
                prim, resto = divmod(n, 100)
                if prim != 0:
                    if prim == 1:
                        if resto == 0:
                            resultado = "cien"
                        else:
                            resultado = "ciento"
                    else:
                        resultado = _n3[prim-1]
                        if en_femenino:
                            resultado += "ientas"
                        else:
                            resultado += "ientos"
                    if resto != 0:
                        resultado += " " + aux_numeral(resto, en_femenino)
                else: # Localizar las decenas
                    if en_femenino and n == 1:
                        resultado = "una"
                    elif n <= 20:
                        resultado = _n1[n-1]
                    else:
                        prim, resto = divmod(n, 10)
                        resultado = _n2[prim-1]
                        if resto != 0:
                            if prim == 2:
                                resultado += _n11[resto-1]
                            else:
                                resultado += " y " + _n1[resto-1]
                            if en_femenino and resto == 1:
                                resultado += "a"
    return resultado

def importe_en_euros(importe):
    '''Devuelve una representación textual de un importe en euros en letras.
    '''
    total_en_centimos = int(round(importe*100))
    euros, centimos = divmod(total_en_centimos, 100)
    num_euros = numeral(euros)
    if num_euros.endswith('uno'):
        num_euros = num_euros[0:-1]
    buff = [num_euros, 'euro' if euros == 1 else 'euros']
    if centimos:
        num_cents = numeral(centimos)
        if num_cents.endswith('uno'):
            num_cents = num_cents[0:-1]
        buff.extend(['con', num_cents, 'céntimos' if centimos > 1 else 'céntimo'])
    return ' '.join(buff)

