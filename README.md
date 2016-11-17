# numerals - Conversión de enteros a texto: 815 -> ochocientos quince

Esté código fue escrito inicialmente por Chema Cortes en Pascal, migrado a Delphi
y yo le he añadido algunas correcciones menores y la función para expresión de
importes en euros (`as_importe_euros`). Puede convertir hasta miles de billones (europeos, no americanos <https://es.wikipedia.org/wiki/Bill%C3%B3n>).

## Ejemplo de uso

### Usando la función `numeral`:

    >>> from numerals import numeral
    >>> assert numeral(0) == 'cero'
    >>> assert numeral(1) == 'uno'
    >>> assert numeral(12) == 'doce'
    >>> assert numeral(201) == 'doscientos uno'
    >>> assert numeral(16777217) == u'dieciséis millones setecientos setenta y siete mil doscientos diecisiete'

Podemos usar un parámetro por nombre, `en_femenino`, opcional, para indicar si
queremos el texto en femenino o en negativo. Por defecto es `False`, es decir,
 en masculino:

    >>> from numerals import numeral
    >>> assert numeral(201) == 'doscientos uno'
    >>> assert numeral(201, en_femenino=True) == 'doscientas una'

### Usando la función `importe_en_euros`

Esta función espera un número entero, flotante o decimal y devuelve una representación
en texto del importe en euros:

    >>> from numerals import importe_en_euros
    >>> assert importe_en_euros(0.23) == u'cero euros con veintitrés céntimos'
    >>> assert importe_en_euros(0) == u'cero euros'
    >>> assert importe_en_euros(810) == u'ochocientos diez euros'
    >>> assert importe_en_euros(810.0) == u'ochocientos diez euros'
    >>> assert importe_en_euros(Decimal('810.0')) == u'ochocientos diez euros'
    >>> assert importe_en_euros(484.23) == u'cuatrocientos ochenta y cuatro euros con veintitrés céntimos'

## Compatibilidad

Funciona en Python 2.7 y 3.x
