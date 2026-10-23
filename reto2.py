from listasEnlazadas import crear_nodo, mostrar, insertar_final


def insertar_despues(cabeza, referente, nuevo_dato):
    actual = cabeza
    while actual is not None:
        if actual["dato"] == referente:
            nuevo = crear_nodo(nuevo_dato)
            # 1. Conectamos el nuevo nodo con el resto de la lista
            nuevo["siguiente"] = actual["siguiente"]
            # 2. Conectamos el nodo referente con el nuevo nodo
            actual["siguiente"] = nuevo
            return True
        actual = actual["siguiente"]
    return False


if __name__ == "__main__":
    cabeza = None
    # Creamos la lista inicial: Ana -> Luis -> None
    cabeza = insertar_final(cabeza, "Ana")
    cabeza = insertar_final(cabeza, "Luis")

    print("Lista inicial:")
    mostrar(cabeza)

    print("\nInsertando a 'Eva' después de 'Ana'...")
    exito = insertar_despues(cabeza, "Ana", "Eva")
    print(f"¿Inserción exitosa?: {exito}")

    print("\nResultado esperado: Ana -> Eva -> Luis -> None")
    print("Resultado obtenido:")
    mostrar(cabeza)