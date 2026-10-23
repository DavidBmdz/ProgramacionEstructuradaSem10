from listasEnlazadas import crear_nodo, mostrar


def atender(cabeza):
    if cabeza is None:
        return None, None

    nombre_atendido = cabeza["dato"]
    nueva_cabeza = cabeza["siguiente"]
    return nueva_cabeza, nombre_atendido


if __name__ == "__main__":
    # Crear lista: Ana -> Luis -> None
    cabeza = crear_nodo("Ana")
    cabeza["siguiente"] = crear_nodo("Luis")

    print("Antes de atender:")
    mostrar(cabeza)

    cabeza, persona = atender(cabeza)
    print(f"Atendido: {persona}")

    print("Después de atender:")
    mostrar(cabeza)