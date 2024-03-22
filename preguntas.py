"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01(data):
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0 
    with open(data, "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas= linea.strip().split('\t')
            # Asegurarse de que hay al menos dos columnas
            if len(columnas)>=2:
                # Intentar convertir el segundo elemento (columna) a entero
                try: 
                    valor= int(columnas[1])
                    suma += valor
                # Si no se puede convertir a entero, ignorar esta línea
                except ValueError:
                    pass
    return(suma)

resultado = pregunta_01("data.csv")
print(resultado) 



def pregunta_02(data):
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    conteo = {}
    with open(data, "r") as archivo:
        for linea in archivo:
            columna_primera= linea.strip().split('\t')[0]
            conteo[columna_primera] = conteo.get(columna_primera, 0) + 1

    # Ordenar el conteo alfabéticamente por las letras
    conteo_ordenado = sorted(conteo.items())
    # Convertir el conteo ordenado en una lista de tuplas
    lista_tuplas = [(letra, cantidad) for letra, cantidad in conteo_ordenado]

    return lista_tuplas

resultado = pregunta_02("data.csv")
print(resultado)


def pregunta_03(data):
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    suma_por_letra = {}
    with open(data, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            letra = columnas[0]
            columna2 = columnas[1]
            try:
                valor_columna2 = int(columna2)
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor_columna2
            except ValueError:
                # Ignorar líneas donde la segunda columna no es un valor numérico
                pass

    # Ordenar el resultado alfabéticamente por las letras
    suma_por_letra_ordenada = sorted(suma_por_letra.items())

    # Convertir la suma ordenada en una lista de tuplas
    lista_tuplas = [(letra, suma) for letra, suma in suma_por_letra_ordenada]

    return lista_tuplas

# Llamar a la función con el nombre del archivo
resultado = pregunta_03('data.csv')
print(resultado)

def pregunta_04(data):
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    conteo_meses = {}
    with open(data, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            fecha = columnas[2]
            mes = fecha.split('-')[1]  # Extraer el mes de la fecha
            conteo_meses[mes] = conteo_meses.get(mes, 0) + 1

    # Ordenar el conteo alfabéticamente por los meses
    conteo_meses_ordenado = sorted(conteo_meses.items())

    # Convertir el conteo ordenado en una lista de tuplas
    lista_tuplas = [(mes, cantidad) for mes, cantidad in conteo_meses_ordenado]

    return lista_tuplas

resultado = pregunta_04('data.csv')
print(resultado)


def pregunta_05(data):
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    max_min_por_letra = {}
    with open(data, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            letra = columnas[0]
            valor_columna2 = int(columnas[1])  # Convertir el valor de la columna 2 a entero
            # Actualizar el máximo y mínimo para esta letra
            if letra not in max_min_por_letra:
                max_min_por_letra[letra] = (valor_columna2, valor_columna2)
            else:
                max_min_por_letra[letra] = (max(max_min_por_letra[letra][0], valor_columna2),
                                            min(max_min_por_letra[letra][1], valor_columna2))

    # Ordenar el resultado alfabéticamente por las letras
    max_min_por_letra_ordenado = sorted(max_min_por_letra.items())

    # Convertir el resultado ordenado en una lista de tuplas
    lista_tuplas = [(letra, max_min[0], max_min[1]) for letra, max_min in max_min_por_letra_ordenado]

    return lista_tuplas

# Llamar a la función con el nombre del archivo
resultado = pregunta_05('data.csv')
print(resultado)



def pregunta_06(data):
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    valores_por_clave = {}
    with open(data, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            diccionario_codificado = columnas[4]
            # Dividir el diccionario codificado en claves y valores
            pares_clave_valor = diccionario_codificado.split(',')
            for par in pares_clave_valor:
                clave, valor = par.split(':')
                valor = int(valor)
                if clave not in valores_por_clave:
                    # Si la clave no está en el diccionario, inicializar con el valor actual
                    valores_por_clave[clave] = (valor, valor)
                else:
                    # Actualizar el mínimo y máximo para esta clave
                    min_valor, max_valor = valores_por_clave[clave]
                    valores_por_clave[clave] = (min(min_valor, valor), max(max_valor, valor))

    # Ordenar el resultado alfabéticamente por las claves
    valores_por_clave_ordenados = sorted(valores_por_clave.items())

    # Convertir el resultado ordenado en una lista de tuplas
    lista_tuplas = [(clave, min_max[0], min_max[1]) for clave, min_max in valores_por_clave_ordenados]

    return lista_tuplas

# Llamar a la función con el nombre del archivo
resultado = pregunta_06('data.csv')
print(resultado)


def pregunta_07(data):
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    asociaciones = {}
    with open(data, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            valor_columna2 = int(columnas[1])
            letra_columna0 = columnas[0]
            if valor_columna2 not in asociaciones:
                asociaciones[valor_columna2] = [letra_columna0]
            else:
                asociaciones[valor_columna2].append(letra_columna0)

    # Convertir el diccionario de asociaciones en una lista de tuplas
    lista_tuplas = [(valor, letras) for valor, letras in asociaciones.items()]

    # Ordenar la lista de tuplas por el valor de la columna 2
    lista_tuplas.sort(key=lambda x: x[0])

    return lista_tuplas

# Llamar a la función con el nombre del archivo
resultado = pregunta_07('data.csv')
print(resultado)
    


def pregunta_08(data):
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    asociaciones = {}
    with open(data, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            valor_columna2 = int(columnas[1])
            letra_columna0 = columnas[0]
            if valor_columna2 not in asociaciones:
                asociaciones[valor_columna2] = [letra_columna0]
            else:
                asociaciones[valor_columna2].append(letra_columna0)

    # Convertir el diccionario de asociaciones en una lista de tuplas
    lista_tuplas = [(valor, sorted(set(letras))) for valor, letras in asociaciones.items()]

    lista_tuplas.sort(key=lambda x: x[0])
   
    return lista_tuplas

# Llamar a la función con el nombre del archivo
resultado = pregunta_08('data.csv')
print(resultado)


def pregunta_09(data):
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    conteo_claves = {}
    with open(data, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            diccionario_codificado = columnas[4]
            # Dividir el diccionario codificado en claves y valores
            pares_clave_valor = diccionario_codificado.split(',')
            for par in pares_clave_valor:
                clave, _ = par.split(':')
                conteo_claves[clave] = conteo_claves.get(clave, 0) + 1
    conteo_claves_ordenado = dict(sorted(conteo_claves.items()))

    return conteo_claves_ordenado

# Llamar a la función con el nombre del archivo
resultado = pregunta_09('data.csv')
print(resultado)


def pregunta_10(data):
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    conteo_elementos = []
    with open(data, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            letra_columna1 = columnas[0]
            elementos_columna4 = len(columnas[3].split(','))
            elementos_columna5 = len(columnas[4].split(','))
            conteo_elementos.append((letra_columna1, elementos_columna4, elementos_columna5))

    return conteo_elementos

# Llamar a la función con el nombre del archivo
resultado = pregunta_10('data.csv')
print(resultado)


def pregunta_11(data):
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_por_letra = {}
    with open(data, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            letras_columna4 = columnas[3].split(',')
            valor_columna2 = int(columnas[1])
            for letra in letras_columna4:
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor_columna2

    conteo_claves_ordenado = dict(sorted(suma_por_letra.items()))

    return conteo_claves_ordenado


resultado = pregunta_11('data.csv')
print(resultado)

def pregunta_12(data):
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    # Creamos un diccionario vacío para almacenar los resultados
    suma_columna5_dict = {}

    # Abrimos el archivo en modo lectura
    with open(data, 'r') as file:
        # Iteramos sobre cada línea del archivo
        for line in file:
            # Dividimos la línea en sus elementos separados por tabulaciones
            elements = line.strip().split('\t')
            
            # Obtenemos la clave de la columna 1 y el valor de la columna 5
            key = elements[0]
            value_str = elements[4]
            
            # Dividimos los pares clave-valor en la columna 5
            pairs = value_str.split(',')
            
            # Sumamos los valores numéricos de la columna 5
            suma_columna5 = 0
            for pair in pairs:
                # Dividimos el par clave-valor
                _, val = pair.split(':')
                # Convertimos el valor a entero y lo sumamos
                suma_columna5 += int(val)
            
            # Agregamos la suma al diccionario
            if key in suma_columna5_dict:
                suma_columna5_dict[key] += suma_columna5
            else:
                suma_columna5_dict[key] = suma_columna5
    
    suma_columna5_dict_ordenado = {k: suma_columna5_dict[k] for k in sorted(suma_columna5_dict)}
    
    # Devolvemos el diccionario con las sumas
    return suma_columna5_dict_ordenado

# Llamamos a la función y mostramos el resultado
resultado = pregunta_12("data.csv")
print(resultado)
