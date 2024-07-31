list = [7,18,22,29,34,28]
def damePromedio(list):
    suma = 0
    lon = 0
    
    for i in list:
        if i%2 == 0:
            print(i)
            suma += i
            lon += 1
            
    return suma/lon

print(damePromedio(list))