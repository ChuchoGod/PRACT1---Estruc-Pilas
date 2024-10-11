CAPACIDAD_MAXIMA = 8
pila = []
tope = 0

def insertar(pila, elemento):
    global tope
    if tope < CAPACIDAD_MAXIMA:
        pila.append(elemento)
        tope += 1
        print(f"Insertar({elemento}) -> Pila: {pila}, Tope: {tope}")
    else:
        print(f"Error: Desbordamiento al intentar insertar {elemento}")

def eliminar(pila):
    global tope
    if tope > 0:
        elemento = pila.pop()
        tope -= 1
        print(f"Eliminar({elemento}) -> Pila: {pila}, Tope: {tope}")
    else:
        print("Error: Subdesbordamiento al intentar eliminar")

insertar(pila, 'X')  # a
insertar(pila, 'Y')  # b
eliminar(pila)       # c
eliminar(pila)       # d
eliminar(pila)       # e
insertar(pila, 'V')  # f
insertar(pila, 'W')  # g
eliminar(pila)       # h
insertar(pila, 'R')  # i

print(f"Estado final de la pila: {pila}, Tope: {tope}, Elementos en la pila: {tope}")
