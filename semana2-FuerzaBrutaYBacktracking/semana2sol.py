import time

def mostrarMenu():
    print("\n---- MENU ------")
    print("1.-  Bubble Sort")
    print("2.-  Polinomios")
    print("3.-  SEND + M O R E = M O N E Y")
    print("4.- Problema del p a st o r (acertijo del l o b o, la cabra y la col)")
    print("5.- Salir")

def bubbleSort(arr: list):
    lon = len(arr)
    for actual in range(lon):
        for siguiente in range(lon - 1):
            if arr[actual] > arr[siguiente]:
                arr[siguiente] = arr[actual]
                arr[actual] = arr[siguiente]

def polinomioPorFuerzaBruta(valorInicial):
    poli = 8*(valorInicial**4) + 7*(valorInicial**4)

def criptoaritmoPorFuerzaBruta():
    for s in range(1,10):
        for e in range(10):
            for n in range(10):
                for d in range(10):
                    for m in range(1,10):
                        for o in range(10):
                            for r in range(10):
                                for y in range(10):
                                    if len(set([s, e, n, d, m, o, r, y])) == 8:
                                        send = s * 1000 + e * 100 + n * 10 + d
                                        more = m * 1000 + o * 100 + r * 10 + e
                                        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
                                        if send + more == money:
                                            return {'S': s, 'E': e, 'N': n, 'D': d,
                                                    'M': m, 'O': o, 'R': r, 'Y': y}
    return None
    
while True:
    mostrarMenu()
    opcion = int(input("Seleccione una opcion: \n==> "))
    if opcion == 5:
        break
    elif opcion == 1:
        arr = [5,12,43,2,1,64,32,6]
        print("Lista original:", arr, "\n")
        time.sleep(2)
        bubbleSort(arr)
        print("Lista ordenada:", arr)
        time.sleep(4)
        
    elif opcion == 2:
        valorInicial = int(input("Ingrese un numero: ==> "))
        polinomioPorFuerzaBruta(valorInicial)
    
    elif opcion == 3:
        print(" SEND +")
        print(" MORE")
        print("------")
        print("MONEY")
        criptoaritmoPorFuerzaBruta()
        solution = criptoaritmoPorFuerzaBruta()
        for letter, digit in solution.items():
            print(f"{letter}: {digit}")
        
        

