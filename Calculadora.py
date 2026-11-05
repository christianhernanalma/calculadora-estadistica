def calcular_media (datos):
    if not datos:
        return 0
    return sum(datos) / len(datos)

#prueba de la funcion 

if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50]
    print(f"La media es: {calcular_media(numeros)}")