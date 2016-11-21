#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import unittest
import numerals

class Uso(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(numerals.numeral(1), 'uno')
        self.assertEqual(numerals.numeral(2), 'dos')
        self.assertEqual(numerals.numeral(3), 'tres')
        self.assertEqual(numerals.numeral(4), 'cuatro')
        self.assertEqual(numerals.numeral(5), 'cinco')
        self.assertEqual(numerals.numeral(6), 'seis')
        self.assertEqual(numerals.numeral(7), 'siete')
        self.assertEqual(numerals.numeral(8), 'ocho')
        self.assertEqual(numerals.numeral(9), 'nueve')
        self.assertEqual(numerals.numeral(10), 'diez')
       
    def test_decenas(self):
        self.assertEqual(numerals.numeral(11), 'once')
        self.assertEqual(numerals.numeral(12), 'doce')
        self.assertEqual(numerals.numeral(13), 'trece')
        self.assertEqual(numerals.numeral(14), 'catorce')
        self.assertEqual(numerals.numeral(15), 'quince')
        self.assertEqual(numerals.numeral(16), 'dieciséis')
        self.assertEqual(numerals.numeral(17), 'diecisiete')
        self.assertEqual(numerals.numeral(18), 'dieciocho')
        self.assertEqual(numerals.numeral(19), 'diecinueve')
        self.assertEqual(numerals.numeral(20), 'veinte')
        self.assertEqual(numerals.numeral(21), 'veintiuno')
        self.assertEqual(numerals.numeral(22), 'veintidós')
        self.assertEqual(numerals.numeral(23), 'veintitrés')
        self.assertEqual(numerals.numeral(24), 'veinticuatro')
        self.assertEqual(numerals.numeral(25), 'veinticinco')
        self.assertEqual(numerals.numeral(26), 'veintiséis')
        self.assertEqual(numerals.numeral(27), 'veintisiete')
        self.assertEqual(numerals.numeral(28), 'veintiocho')
        self.assertEqual(numerals.numeral(29), 'veintinueve')
        self.assertEqual(numerals.numeral(30), 'treinta')
        self.assertEqual(numerals.numeral(62), 'sesenta y dos')
        self.assertEqual(numerals.numeral(98), 'noventa y ocho')
        self.assertEqual(numerals.numeral(99), 'noventa y nueve')
       
    def test_centenas(self):
        self.assertEqual(numerals.numeral(100), 'cien')
        self.assertEqual(numerals.numeral(101), 'ciento uno')
        self.assertEqual(numerals.numeral(102), 'ciento dos')
        self.assertEqual(numerals.numeral(198), 'ciento noventa y ocho')
        self.assertEqual(numerals.numeral(745), 'setecientos cuarenta y cinco')
        self.assertEqual(numerals.numeral(998), 'novecientos noventa y ocho')
        self.assertEqual(numerals.numeral(999), 'novecientos noventa y nueve')
        

    def test_dieciseis_con_acento(self):
        self.assertEqual(numerals.numeral(16), 'dieciséis')

    def test_veintiseis_con_acento(self):
        self.assertEqual(numerals.numeral(26), 'veintiséis')

    def test_random(self):
        self.assertEqual(numerals.numeral(201), 'doscientos uno')
        self.assertEqual(numerals.numeral(1111), 'mil ciento once')
        self.assertEqual(numerals.numeral(1023), 'mil veintitrés')
        self.assertEqual(numerals.numeral(1223), 'mil doscientos veintitrés')

    def test_miles(self):
        self.assertEqual(numerals.numeral(1000), 'mil')
        self.assertEqual(numerals.numeral(1001), 'mil uno')
        self.assertEqual(numerals.numeral(1002), 'mil dos')
        self.assertEqual(numerals.numeral(7103), 'siete mil ciento tres')
        self.assertEqual(numerals.numeral(7130), 'siete mil ciento treinta')
        self.assertEqual(
            numerals.numeral(8977),
            'ocho mil novecientos setenta y siete'
            )
        self.assertEqual(
            numerals.numeral(8977, en_femenino=True),
            'ocho mil novecientas setenta y siete'
            )

        self.assertEqual(numerals.numeral(1998), 'mil novecientos noventa y ocho')
        self.assertEqual(numerals.numeral(1999), 'mil novecientos noventa y nueve')

    def test_decenas_de_miles(self):
        self.assertEqual(numerals.numeral(10000), 'diez mil')
        self.assertEqual(numerals.numeral(10001), 'diez mil uno')
        self.assertEqual(numerals.numeral(10002), 'diez mil dos')
        self.assertEqual(
            numerals.numeral(42758),
            'cuarenta y dos mil setecientos cincuenta y ocho'
            )
        self.assertEqual(
            numerals.numeral(42758, en_femenino=True),
            'cuarenta y dos mil setecientas cincuenta y ocho'
            )

        self.assertEqual(
            numerals.numeral(58455),
            'cincuenta y ocho mil cuatrocientos cincuenta y cinco'
            )
        self.assertEqual(
            numerals.numeral(19998),
            'diecinueve mil novecientos noventa y ocho'
            )
        self.assertEqual(
            numerals.numeral(19999),
            'diecinueve mil novecientos noventa y nueve'
            )

    def test_cientos_de_miles(self):
        self.assertEqual(numerals.numeral(100000), 'cien mil')
        self.assertEqual(numerals.numeral(100001), 'cien mil uno')
        self.assertEqual(numerals.numeral(100002), 'cien mil dos')
        self.assertEqual(
            numerals.numeral(278482),
            'doscientos setenta y ocho mil cuatrocientos ochenta y dos'
            )
        self.assertEqual(
            numerals.numeral(278482, en_femenino=True),
            'doscientas setenta y ocho mil cuatrocientas ochenta y dos'
            )
        self.assertEqual(
            numerals.numeral(199998),
            'ciento noventa y nueve mil novecientos noventa y ocho'
            )
        self.assertEqual(
            numerals.numeral(199999),
            'ciento noventa y nueve mil novecientos noventa y nueve'
            )
            
    def test_millones(self):
        self.assertEqual(numerals.numeral(1000000), 'un millón')
        self.assertEqual(numerals.numeral(1000001), 'un millón uno')
        self.assertEqual(numerals.numeral(1000002), 'un millón dos')
        self.assertEqual(
            numerals.numeral(2057672),
            'dos millones cincuenta y siete mil'
            ' seiscientos setenta y dos'
            )
        self.assertEqual(
            numerals.numeral(2057672, en_femenino=True),
            'dos millones cincuenta y siete mil'
            ' seiscientas setenta y dos'
            )
        self.assertEqual(
            numerals.numeral(4728272),
            'cuatro millones setecientos veintiocho mil'
            ' doscientos setenta y dos'
            )
        self.assertEqual(
            numerals.numeral(4728272, en_femenino=True),
            'cuatro millones setecientas veintiocho mil'
            ' doscientas setenta y dos'
            )
        self.assertEqual(
            numerals.numeral(1999998),
            'un millón novecientos noventa y nueve'
            ' mil novecientos noventa y ocho'
            )
        self.assertEqual(
            numerals.numeral(1999999),
            'un millón novecientos noventa y nueve'
            ' mil novecientos noventa y nueve'
            )

    def test_decenas_de_millones(self):
        self.assertEqual(numerals.numeral(10000000), 'diez millones')
        self.assertEqual(numerals.numeral(10000001), 'diez millones uno')
        self.assertEqual(
            numerals.numeral(21048428),
            'veintiún millones cuarenta y ocho mil'
            ' cuatrocientos veintiocho'
            )
        self.assertEqual(
            numerals.numeral(99999998),
            'noventa y nueve millones'
            ' novecientos noventa y nueve mil'
            ' novecientos noventa y ocho'
            )
        self.assertEqual(
            numerals.numeral(99999999),
            'noventa y nueve millones'
            ' novecientos noventa y nueve mil'
            ' novecientos noventa y nueve'
            )
    
    def test_zero(self):
        self.assertEqual(numerals.numeral(0), 'cero')

    def test_negattivo(self):
        self.assertEqual(numerals.numeral(-4), 'menos cuatro')


class Excepciones(unittest.TestCase):

    def test_fuckin_21(self):
        self.assertEqual(
            numerals.numeral(21),
            'veintiuno'
            )

    def test_fuckin_210(self):
        self.assertEqual(
            numerals.numeral(210),
            'doscientos diez'
            )

    def test_fuckin_2121(self):
        self.assertEqual(
            numerals.numeral(2110),
            'dos mil ciento diez'
            )

    def test_fuckin_21021(self):
        self.assertEqual(
            numerals.numeral(21021),
            'veintiún mil veintiuno'
            )

        self.assertEqual(
            numerals.numeral(21021, en_femenino=True),
            'veintiuna mil veintiuna'
            )

    def test_fuckin_21021021(self):
        self.assertEqual(
            numerals.numeral(21021021),
            'veintiún millones veintiún mil veintiuno'
            )

        self.assertEqual(
            numerals.numeral(21021, en_femenino=True),
            'veintiuna mil veintiuna'
            )

    def test_fuckink_21_billions(self):
        self.assertEqual(
            numerals.numeral(21021021021021),
            'veintiún billones veintiún mil veintiún millones'
            ' veintiún mil veintiuno'
            )

class Euros(unittest.TestCase):

    def test_cero(self):
        self.assertEqual(
            numerals.importe_en_euros(0),
            'cero euros'
            )
        self.assertEqual(
            numerals.importe_en_euros(0.0),
            'cero euros'
            )

    def test_un_centimo(self):
        self.assertEqual(
            numerals.importe_en_euros(0.01),
            'cero euros con un céntimo'
            )
    
    def test_un_euro(self):
        self.assertEqual(
            numerals.importe_en_euros(1),
            'un euro'
            )

    def test_cero_euros(self):
        self.assertEqual(
            numerals.importe_en_euros(0.0),
            'cero euros'
            )

    def test_231_euros_con_75_centimos(self):
        self.assertEqual(
            numerals.importe_en_euros(231.75),
            'doscientos treinta y un euros con setenta y cinco céntimos'
            )

    def test_centimos_01_a_20(self):
        self.assertEqual(numerals.importe_en_euros(0.01), 'cero euros con un céntimo')
        self.assertEqual(numerals.importe_en_euros(0.02), 'cero euros con dos céntimos')
        self.assertEqual(numerals.importe_en_euros(0.03), 'cero euros con tres céntimos')
        self.assertEqual(numerals.importe_en_euros(0.04), 'cero euros con cuatro céntimos')
        self.assertEqual(numerals.importe_en_euros(0.05), 'cero euros con cinco céntimos')
        self.assertEqual(numerals.importe_en_euros(0.06), 'cero euros con seis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.07), 'cero euros con siete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.08), 'cero euros con ocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.09), 'cero euros con nueve céntimos')
        self.assertEqual(numerals.importe_en_euros(0.10), 'cero euros con diez céntimos')
        self.assertEqual(numerals.importe_en_euros(0.11), 'cero euros con once céntimos')
        self.assertEqual(numerals.importe_en_euros(0.12), 'cero euros con doce céntimos')
        self.assertEqual(numerals.importe_en_euros(0.13), 'cero euros con trece céntimos')
        self.assertEqual(numerals.importe_en_euros(0.14), 'cero euros con catorce céntimos')
        self.assertEqual(numerals.importe_en_euros(0.15), 'cero euros con quince céntimos')
        self.assertEqual(numerals.importe_en_euros(0.16), 'cero euros con dieciséis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.17), 'cero euros con diecisiete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.18), 'cero euros con dieciocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.19), 'cero euros con diecinueve céntimos')
        self.assertEqual(numerals.importe_en_euros(0.20), 'cero euros con veinte céntimos')

    def test_centimos_21_a_40(self):
        self.assertEqual(numerals.importe_en_euros(0.21), 'cero euros con veintiun céntimos')
        self.assertEqual(numerals.importe_en_euros(0.22), 'cero euros con veintidós céntimos')
        self.assertEqual(numerals.importe_en_euros(0.23), 'cero euros con veintitrés céntimos')
        self.assertEqual(numerals.importe_en_euros(0.24), 'cero euros con veinticuatro céntimos')
        self.assertEqual(numerals.importe_en_euros(0.25), 'cero euros con veinticinco céntimos')
        self.assertEqual(numerals.importe_en_euros(0.26), 'cero euros con veintiséis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.27), 'cero euros con veintisiete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.28), 'cero euros con veintiocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.29), 'cero euros con veintinueve céntimos')
        self.assertEqual(numerals.importe_en_euros(0.30), 'cero euros con treinta céntimos')
        self.assertEqual(numerals.importe_en_euros(0.31), 'cero euros con treinta y un céntimos')
        self.assertEqual(numerals.importe_en_euros(0.32), 'cero euros con treinta y dos céntimos')
        self.assertEqual(numerals.importe_en_euros(0.33), 'cero euros con treinta y tres céntimos')
        self.assertEqual(numerals.importe_en_euros(0.34), 'cero euros con treinta y cuatro céntimos')
        self.assertEqual(numerals.importe_en_euros(0.35), 'cero euros con treinta y cinco céntimos')
        self.assertEqual(numerals.importe_en_euros(0.36), 'cero euros con treinta y seis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.37), 'cero euros con treinta y siete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.38), 'cero euros con treinta y ocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.39), 'cero euros con treinta y nueve céntimos')
        self.assertEqual(numerals.importe_en_euros(0.40), 'cero euros con cuarenta céntimos')
    
    def test_centimos_41_a_60(self):
        self.assertEqual(numerals.importe_en_euros(0.41), 'cero euros con cuarenta y un céntimos')
        self.assertEqual(numerals.importe_en_euros(0.42), 'cero euros con cuarenta y dos céntimos')
        self.assertEqual(numerals.importe_en_euros(0.43), 'cero euros con cuarenta y tres céntimos')
        self.assertEqual(numerals.importe_en_euros(0.44), 'cero euros con cuarenta y cuatro céntimos')
        self.assertEqual(numerals.importe_en_euros(0.45), 'cero euros con cuarenta y cinco céntimos')
        self.assertEqual(numerals.importe_en_euros(0.46), 'cero euros con cuarenta y seis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.47), 'cero euros con cuarenta y siete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.48), 'cero euros con cuarenta y ocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.49), 'cero euros con cuarenta y nueve céntimos')
        self.assertEqual(numerals.importe_en_euros(0.50), 'cero euros con cincuenta céntimos')
        self.assertEqual(numerals.importe_en_euros(0.51), 'cero euros con cincuenta y un céntimos')
        self.assertEqual(numerals.importe_en_euros(0.52), 'cero euros con cincuenta y dos céntimos')
        self.assertEqual(numerals.importe_en_euros(0.53), 'cero euros con cincuenta y tres céntimos')
        self.assertEqual(numerals.importe_en_euros(0.54), 'cero euros con cincuenta y cuatro céntimos')
        self.assertEqual(numerals.importe_en_euros(0.55), 'cero euros con cincuenta y cinco céntimos')
        self.assertEqual(numerals.importe_en_euros(0.56), 'cero euros con cincuenta y seis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.57), 'cero euros con cincuenta y siete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.58), 'cero euros con cincuenta y ocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.59), 'cero euros con cincuenta y nueve céntimos')

    def test_centimos_61_a_80(self):
        self.assertEqual(numerals.importe_en_euros(0.60), 'cero euros con sesenta céntimos')
        self.assertEqual(numerals.importe_en_euros(0.61), 'cero euros con sesenta y un céntimos')
        self.assertEqual(numerals.importe_en_euros(0.62), 'cero euros con sesenta y dos céntimos')
        self.assertEqual(numerals.importe_en_euros(0.63), 'cero euros con sesenta y tres céntimos')
        self.assertEqual(numerals.importe_en_euros(0.64), 'cero euros con sesenta y cuatro céntimos')
        self.assertEqual(numerals.importe_en_euros(0.65), 'cero euros con sesenta y cinco céntimos')
        self.assertEqual(numerals.importe_en_euros(0.66), 'cero euros con sesenta y seis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.67), 'cero euros con sesenta y siete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.68), 'cero euros con sesenta y ocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.69), 'cero euros con sesenta y nueve céntimos')
        self.assertEqual(numerals.importe_en_euros(0.70), 'cero euros con setenta céntimos')
        self.assertEqual(numerals.importe_en_euros(0.71), 'cero euros con setenta y un céntimos')
        self.assertEqual(numerals.importe_en_euros(0.72), 'cero euros con setenta y dos céntimos')
        self.assertEqual(numerals.importe_en_euros(0.73), 'cero euros con setenta y tres céntimos')
        self.assertEqual(numerals.importe_en_euros(0.74), 'cero euros con setenta y cuatro céntimos')
        self.assertEqual(numerals.importe_en_euros(0.75), 'cero euros con setenta y cinco céntimos')
        self.assertEqual(numerals.importe_en_euros(0.76), 'cero euros con setenta y seis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.77), 'cero euros con setenta y siete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.78), 'cero euros con setenta y ocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.79), 'cero euros con setenta y nueve céntimos')
        self.assertEqual(numerals.importe_en_euros(0.80), 'cero euros con ochenta céntimos')

    def test_centimos_81_a_99(self):
        self.assertEqual(numerals.importe_en_euros(0.81), 'cero euros con ochenta y un céntimos')
        self.assertEqual(numerals.importe_en_euros(0.82), 'cero euros con ochenta y dos céntimos')
        self.assertEqual(numerals.importe_en_euros(0.83), 'cero euros con ochenta y tres céntimos')
        self.assertEqual(numerals.importe_en_euros(0.84), 'cero euros con ochenta y cuatro céntimos')
        self.assertEqual(numerals.importe_en_euros(0.85), 'cero euros con ochenta y cinco céntimos')
        self.assertEqual(numerals.importe_en_euros(0.86), 'cero euros con ochenta y seis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.87), 'cero euros con ochenta y siete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.88), 'cero euros con ochenta y ocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.89), 'cero euros con ochenta y nueve céntimos')
        self.assertEqual(numerals.importe_en_euros(0.90), 'cero euros con noventa céntimos')
        self.assertEqual(numerals.importe_en_euros(0.91), 'cero euros con noventa y un céntimos')
        self.assertEqual(numerals.importe_en_euros(0.92), 'cero euros con noventa y dos céntimos')
        self.assertEqual(numerals.importe_en_euros(0.93), 'cero euros con noventa y tres céntimos')
        self.assertEqual(numerals.importe_en_euros(0.94), 'cero euros con noventa y cuatro céntimos')
        self.assertEqual(numerals.importe_en_euros(0.95), 'cero euros con noventa y cinco céntimos')
        self.assertEqual(numerals.importe_en_euros(0.96), 'cero euros con noventa y seis céntimos')
        self.assertEqual(numerals.importe_en_euros(0.97), 'cero euros con noventa y siete céntimos')
        self.assertEqual(numerals.importe_en_euros(0.98), 'cero euros con noventa y ocho céntimos')
        self.assertEqual(numerals.importe_en_euros(0.99), 'cero euros con noventa y nueve céntimos')

    def test_random(self):
        self.assertEqual(
            numerals.importe_en_euros(484.23),
            'cuatrocientos ochenta y cuatro euros con veintitrés céntimos'
            )

if __name__ == '__main__':
    unittest.main()
