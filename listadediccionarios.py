# Crear una funcion que reciba una lista de
# diccionarios, cada uno representando una persona
# con nombre y edad. La funcion debe resolver una lista
# ordenada de personas por edad.
#def obtener_edad(persona):
#persona: Un diccionario que representa a una persona.
# Buscamos la clave "edad" en el diccionario y retornamos su valor
#for nombre, edad in persona.items():
#return edad

#def ordenar_por_edad(personas):
#return sorted(personas, key=obtener_edad)

# Ejemplo de uso
#personas = [{"Rafael": 43},{"Pepito":12}]
#personas_ordenadas = ordenar_por_edad(personas)

# Imprimimos el resultado
#for persona in personas_ordenadas:
#for nombre, edad in persona.items():
#print(f"{nombre} tiene {edad} años")

nombres = [{"Mengano":43},{"Pepito":12},{"Fulano":22}]
def ObtenerEdad(persona):
    for edad in persona.items():
        return edad
def OrdenarEdad(persona):
    return sorted(persona, key=ObtenerEdad)

ListaDeDiccionario = [{"Mengano":43},{"Pepito":12},{"Fulano":22}]
PersonasOrden = OrdenarEdad(any)
for persona in PersonasOrden:
    for nombre, edad in persona.items():
        print(f"{nombre} tiene {edad} años")


    