import random

pokemones = []


def crearEntrenador(tupla):
    entrenador = input("Ingrese el nombre del entrenador: ")
    pokemon = input("Ingrese el nombre del Pokemon: ")

    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)

    nuevo_pokemon = (entrenador, pokemon, ataque, vida)
    tupla.append(nuevo_pokemon)

    print("Pokemon creado correctamente")
    print(nuevo_pokemon)


def listaEntrenador(tupla):
    for i in range(len(tupla) - 1):
        for j in range(len(tupla) - 1 - i):
            if tupla[j][2] > tupla[j + 1][2]:
                tupla[j], tupla[j + 1] = tupla[j + 1], tupla[j]

    print("\n===== LISTA DE POKEMONES =====")

    contador = 1

    for pokemon in tupla:
        print(contador, "-", pokemon[0], "-", pokemon[1],
              "- Ataque:", pokemon[2],
              "- Vida:", pokemon[3])
        contador += 1
def borrarPokemon(tupla):
    if len(tupla) == 0:
        print("No hay pokemones para borrar.")
        return
    vida_buscar = int(input("Ingrese la vida del Pokemon a buscarr: "))

    #ORDENAR POR SELECCION
    for i in range(len(tupla) - 1):
        posicion_minima = i
        for j in range(i + 1, len(tupla)):
            if tupla[j][3] < tupla[posicion_minima][3]:
                posicion_minima = j
        tupla[i], tupla[posicion_minima] = tupla[posicion_minima], tupla[i]
    #BUSQUEDA BINARIA
    inicio = 0
    fin = len(tupla) - 1
    encontrado = -1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if tupla[medio][3] == vida_buscar:
            encontrado = medio
            break
        elif tupla[medio][3] < vida_buscar:
            inicio = medio + 1
        else:
            fin = medio - 1

    if encontrado != -1:
        tupla.pop(encontrado)
        print("Pokemon eliminado correctamente.")
    else:
        print("No se encontró un Pokemon con esa vida.")
def peleaPokemon(lista):
    if len(lista) < 2:
        print("Se necesitan al menos 2 pokemones para pelear.")
        return
    listaEntrenador(lista)
    
    numero1 = int(input("Ingrese el número del primer Pokemon: "))
    numero2 = int(input("Ingrese el número del segundo Pokemon: "))
    
    if numero1 < 1 or numero1 > len(lista) or numero2 < 1 or numero2 > len(lista):
        print("Número de Pokemon inválido.")
        return
    pokemon1 = lista[numero1 - 1]
    pokemon2 = lista[numero2 - 1]
    
    multiplicador1 = random.randint(0, 5)
    multiplicador2 = random.randint(0, 5)
    
    daño1 = pokemon1[2] * multiplicador1
    daño2 = pokemon2[2] * multiplicador2
    
    vida1 = pokemon1[3] - daño2
    vida2 = pokemon2[3] - daño1
    
    print("\n===Pelea Pokemon===")
    print(pokemon1[1], "ataca con", daño1, "de daño. Vida restante:", vida1)
    print(pokemon2[1], "ataca con", daño2, "de daño. Vida restante:", vida2)
    
    if vida1 <= 0 and vida2 <= 0:
        print("¡Empate! Ambos pokemones han caído.")
        lista.remove(pokemon1)
        lista.remove(pokemon2)
    elif vida1 <= 0:
        print(pokemon1[0], "ha ganado la pelea", pokemon2[1])
        lista.remove(pokemon1)
    elif vida2 <= 0:
        print(pokemon2[0], "ha ganado la pelea", pokemon1[1])
        lista.remove(pokemon2)
    elif vida2 > vida1:
        print(pokemon2[0], "ha ganado la pelea", pokemon1[1])
        lista.remove(pokemon1)
    else:
        print("Empate. Amboss perdieron.")
        lista.remove(pokemon1)
        lista.remove(pokemon2)
while True:
    print("\n===== MENU POKEMON=====")
    print("1. Crear Entreandor")
    print("2. Lista Entrenadores")
    print("3. Borrar por Pokemon")
    print("4. Pelea Pokemon")
    print("5. Salir")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        crearEntrenador(pokemones)
    
    elif opcion == "2":
        listaEntrenador(pokemones)
    
    elif opcion == "3":
        borrarPokemon(pokemones)
    
    elif opcion == "4":
        peleaPokemon(pokemones)
    
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
    