def calcular_media (datos):
    if not datos:
        return 0
    return sum(datos) / len(datos)

#prueba de la funcion 

if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50]
    print(f"La media es: {calcular_media(numeros)}")

def calcular_mediana(datos):
    n = len(datos)
    if not datos:
        return 0
    datos_ordenados = sorted(datos)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
        return mediana
    elif n % 2 == 1:
        mediana = datos_ordenados[n//2]
        return mediana
#prueba de la segunda funcion 
if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50, 60]
    print(f"La mediana es: {calcular_mediana(numeros)}")

#funcion para calcular la moda
def calcular_moda(datos):
    
    modas = []
    conteo_mas_alta = 0
    
    if not datos:
        return 0
    for n in datos:
        
        if datos.count(n) > conteo_mas_alta:
            conteo_mas_alta = datos.count(n)
            modas = [n]
        elif datos.count(n) == conteo_mas_alta and n not in modas:
            modas.append(n)
    return modas 

#prueba de la tercera funcion
if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50, 10, 20]
    print(f"La moda es: {calcular_moda(numeros)}")
