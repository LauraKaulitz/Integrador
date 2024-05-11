#calcular el area de un triangulo

area= lambda x, y: x + y / 2 

for a in range (1, 4):
    for i in range(5, 8):
         print(
         f"El área del triángulo de base {a} y altura {i} es {area(a, i)}."
        )
# ordenar una lista de cadenas por longitud

lista_letra=["uno", "dosmil", "cinco", "veinte"]
longitud=sorted(lista_letra, key = lambda x:len(x))
print(longitud)
         
#filtrar una lista de numeros negativos
         
lista=[-1, -2, -3, 1, 2, 3]
negativos=list(filter(lambda a: (a < 0), lista))
print(negativos)

