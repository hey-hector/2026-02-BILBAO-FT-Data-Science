#Si sigo el enunciado me vuelvo loqui, así que vamos a hacerlo paso a paso
#PASO 1: tableros. Debería haber 2 versiones de tablero que deberían estar en la misma clase:
    #- 1 por cada jugador: el que veo yo y el que ve mi contrincante:
    
#TABLERO 1: MI TABLERO. Crear un Tablero como una lista de listas de 10x10 que contenga caracteres espacio: " " 
#*de internet*
    
tablero1 = [] #se empieza con una lista vacía y le añadiremos filas (i) y columnas (j) de un rango de 10
for i in range(10):
    fila = [] #se crea la lista vacía de filas
    for j in range(10): #este bucle 'for' está dentro para que haya una columna por cada fila - para que estén asociadas (o eso creo)
        fila.append(" ") #para cada columna (y en consecuencia, cada fila) se le añade el espacio - ¿al final de la lista?
    tablero1.append(fila) #a la lista vacía 'tablero1', se le añade el bucle entero al final

#print(tablero1) - prueba
    
#Así tenemos la lista "tablero1" de 10 filas y 1o columnas (10 listas con 10 elementos) con espacios en blanco

#TABLERO 2: al principio será igual. Luego ya no 

tablero2 = [] #se empieza con una lista vacía y le añadiremos filas (i) y columnas (j) de un rango de 10
for i in range(10):
    fila = [] #se crea la lista vacía de filas
    for j in range(10): #este bucle 'for' está dentro para que haya una columna por cada fila - para que estén asociadas (o eso creo)
        fila.append(" ") #para cada columna (y en consecuencia, cada fila) se le añade el espacio - ¿al final de la lista?
    tablero2.append(fila) #a la lista vacía 'tablero2', se le añade el bucle entero al final

#print(tablero2) - prueba

#Así tenemos las listas "tablero1" y "tablero2" de 10 filas y 1o columnas (10 listas con 10 elementos) con espacios en blanco

#PASO 2: meter los barcos en cada tablero:
# * 4 barcos de 1 posición de eslora
# * 3 barcos de 2 posiciones de eslora
# * 2 barcos de 3 posiciones de eslora
# * 1 barco de 4 posiciones de eslora
#lo voy a hacer como en Mini Hundir La Flota porque no sé cómo hacerlo para que elija los barcos de manera aleatoria

#TABLERO 1:
#tablero1[coordenada_i][coordenada_j]:
#Barco 4 posiciones:
tablero1[1][0] = "B"
tablero1[1][1] = "B"
tablero1[1][2] = "B"
tablero1[1][3] = "B"
#Barco_1 3 posiciones:
tablero1[3][3] = "B"
tablero1[4][3] = "B"
tablero1[5][3] = "B"
#Barco_2 3 posiciones:
tablero1[8][4] = "B"
tablero1[8][5] = "B"
tablero1[8][6] = "B" 
#Barco_1 2 posiciones: 
tablero1[6][9] = "B"
tablero1[7][9] = "B"
#Barco_2 2 posiciones:
tablero1[7][3] = "B"
tablero1[7][4] = "B"
#Barco_3 2 posiciones:
tablero1[0][6] = "B"
tablero1[1][6] = "B"
#Barco_1 4 posiciones:
tablero1[5][5] = "B"
#Barco_2 4 posiciones:
tablero1[9][6] = "B"
#Barco_3 4 posiciones:
tablero1[9][9] = "B"
#Barco_4 4 posiciones:
tablero1[6][4] = "B"
#Esto significa que la coordenada_i es la lista en la que está el elemento y la coordenada_j será la posición dentro de esa lista
#print(tablero1) - prueba

#TABLERO 2: esto  lo tiene que rellenar la máquina. Pero vamos a imaginar que yo soy la máquina también, ¿quién sino?
# Al final lo hacemos tablero[coordenada_i][coordenada_j]:
#Barco 4 posiciones:
tablero2[8][0] = "B"
tablero2[8][1] = "B"
tablero2[8][2] = "B"
tablero2[8][3] = "B"
#Barco_1 3 posiciones:
tablero2[4][3] = "B"
tablero2[5][3] = "B"
tablero2[6][3] = "B"
#Barco_2 3 posiciones:
tablero2[1][4] = "B"
tablero2[2][4] = "B"
tablero2[3][4] = "B" 
#Barco_1 2 posiciones: 
tablero2[6][6] = "B"
tablero2[7][6] = "B"
#Barco_2 2 posiciones:
tablero2[9][3] = "B"
tablero2[9][4] = "B"
#Barco_3 2 posiciones:
tablero2[5][0] = "B"
tablero2[6][0] = "B"
#Barco_1 4 posiciones:
tablero2[1][1] = "B"
#Barco_2 4 posiciones:
tablero2[9][6] = "B"
#Barco_3 4 posiciones:
tablero2[6][9] = "B"
#Barco_4 4 posiciones:
tablero2[4][6] = "B"
#Esto significa que la coordenada_i es la lista en la que está el elemento y la coordenada_j será la posición dentro de esa lista
#print(tablero2) - prueba

#PASO 3: turnos

#JUGADOR 1: el jugador 1 juega en el tablero 2
while True: #se crea este bucle infinito para que nos vuelva a tocar cuando el jugador 2 pierda. Sino se acabaría el juego
    while True: #se crea un ciclo "while" para que la máquina nos pida inputs y vaya imprimiendo hasta que fallemos:
        coordenada_i2 = int(input("Tu turno jugador 1. Meta la fila deseada. Valores 0-9:")) #fila (Nº de lista dentro de la lista)
        coordenada_j2 = int(input("Meta la columna deseada. Valores 0-9:")) #columna (Nº de elemento dentro de la lista)
        print(coordenada_i2, coordenada_j2) 
        print(tablero2[coordenada_i2][coordenada_j2]) #este comando print es para que muestre lo que hay en esa posición: si he acertado, que salga "B"; sino, saldrá " "
        if tablero2[coordenada_i2][coordenada_j2] == "B": 
            tablero2[coordenada_i2][coordenada_j2] = "x"
            print("Tocado en", coordenada_i2, coordenada_j2, "¡¡Te toca de nuevo!!")
            print(tablero2)                        
        elif tablero2[coordenada_i2][coordenada_j2] == " ":
            tablero2[coordenada_i2][coordenada_j2] = "o"
            print("Agua. Sorry :( Turno del jugador 2")
            print(tablero2)
            break
        elif tablero2[coordenada_i2][coordenada_j2] == "o" or tablero2[coordenada_i2][coordenada_j2] == "x":
            print("Aquí ya has disparado. Try Again Next Time :p Turno del jugador 2")
            print(tablero2)
            break       
       
#JUGADOR 2: el jugador 2 juega en el tablero 1
    while True: #se crea un ciclo "while" para que la máquina nos pida inputs y vaya imprimiendo hasta que fallemos:
        coordenada_i1 = int(input("Tu turno jugador 2. Meta la fila deseada. Valores 0-9:")) #fila (Nº de lista dentro de la lista)
        coordenada_j1 = int(input("Meta la columna deseada. Valores 0-9:")) #columna (Nº de elemento dentro de la lista)
        print(coordenada_i1, coordenada_j1) 
        print(tablero1[coordenada_i1][coordenada_j1]) #este comando print es para que muestre lo que hay en esa posición: si he acertado, que salga "B"; sino, saldrá " "
        if tablero1[coordenada_i1][coordenada_j1] == "B": 
            tablero1[coordenada_i1][coordenada_j1] = "x"
            print("Tocado en", coordenada_i1, coordenada_j1,"¡¡Te toca de nuevo!!")
            print(tablero1)
        elif tablero1[coordenada_i1][coordenada_j1] == " ":
            tablero1[coordenada_i1][coordenada_j1] = "o"
            print("Agua. Sorry :( Turno del jugador 1")
            print(tablero1)
            break
        elif tablero1[coordenada_i1][coordenada_j1] == "o" or tablero1[coordenada_i1][coordenada_j1] == "x":
            print("Aquí ya has disparado. Try Again Next Time :p Turno del jugador 1")
            print(tablero1)
            break
    
#MEJORAS: 
# - Meterlo en un class e ir definiendo las funciones para llamar esas funciones desde los archivos .py
# - Poner los tableros bonitos y que se impriman como una tablero real (con sus filas y columnas), no como listas
# - Elegir los barcos de manera aleatoria
# - Que no de error cada vez que no meta en los inputs de coordenadas un valor entre 0 y 9
# - Meter los turnos en un bucle para que no se juegue de manera infinita
# - Hacer que la máquina sea el jugador 2 y dispare de manera aleatoria