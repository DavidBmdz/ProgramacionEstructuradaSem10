from listasEnlazadas import crear_nodo, mostrar, insertar_final


def invertir(cabeza):
    anterior = None
    actual = cabeza

    while actual is not None:
        siguiente_temp = actual["siguiente"]  # Guardar referencia al siguiente nodo
        actual["siguiente"] = anterior        # Invertir la dirección del puntero
        anterior = actual                    # Avanzar el puntero anterior
        actual = siguiente_temp               # Avanzar el puntero actual

    return anterior  # 'anterior' pasa a ser la nueva cabeza


if __name__ == "__main__":
    cabeza = None
    # Creamos la lista inicial: Ana -> Luis -> Eva -> None
    cabeza = insertar_final(cabeza, "Ana")
    cabeza = insertar_final(cabeza, "Luis")
    cabeza = insertar_final(cabeza, "Eva")

    print("Lista original:")
    mostrar(cabeza)

    print("\nInvertiendo la lista...")
    cabeza = invertir(cabeza)

    print("\nResultado esperado: Eva -> Luis -> Ana -> None")
    print("Resultado obtenido:")
    mostrar(cabeza)