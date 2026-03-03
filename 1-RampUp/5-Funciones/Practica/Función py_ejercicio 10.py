def piramide(filas):
    for i in range(filas,0,-1): #filas
        for j in list(range(i,0,-1)): #columnas
            print(j, end = " ")
        print() #salto de línea para que cambie en cada fila o con función \n. También se podría poner print(list(range(i,0,-1)))   