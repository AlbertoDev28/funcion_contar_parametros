"""
Crea una función contar_coincidencias que
reciba una lista y una función para contar cuántos
elementos cumplen con la condición.
• Ejemplo de uso:
numeros = [1, 2, 3, 4, 5, 6]
resultado = contar_coincidencias(numeros, es_impar)
print("Cantidad de impares:", resultado)
• Salida esperada:
Cantidad de impares: 3
"""


def contar_coincidencias(lista, impar):
     original = list(lista)
     nueva_lista = []

     for elemento in original:
         if impar(elemento) is not None:
             nueva_lista.append(impar(elemento))

     return nueva_lista

def impar(numeros):
    if numeros % 2 == 1:
        return numeros


numeros = [1, 2, 3, 4, 5, 6]
resultado = contar_coincidencias(numeros, impar)
print(f"cantidad de impares: {len(resultado)}")

