from statistics import mode
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print('No es un numero primo')
            return False
    print('Es un numero primo')
    VectorPrimo.append(num)
    return True
# Punto1
VectorNum = []
Sumatoria = 0
Productoria = 1
VectorSumatoria = []
VectorProductoria = []
Elementos = int(input('Digite la cantidad de elementos del vector: '))
for i in range(Elementos):
    num = float(input(f'Digite el numero en la posicion: {i} '))
    Sumatoria = Sumatoria + num
    Productoria = Productoria * num
    VectorNum.append(num)
    VectorSumatoria.append(Sumatoria)
    VectorProductoria.append(Productoria)
print(f'Los elementos del vector son: {VectorNum}')
print(f'La sumatoria es: {Sumatoria} y su vector es: {VectorSumatoria}')
print(f'La productoria es: {Productoria} y su vector es: {VectorProductoria}')
print(f'El elemento de menor valor del vector es: {min(VectorNum)}')
print(f'El elemento de mayor valor del vector es: {max(VectorNum)}')
# Punto2
VectorNum2 = []
VectorPar = []
VectorImpar = []
VectorPrimo = []
Elementos2 = int(input('Digite la cantidad de elementos del vector: '))
for i in range(Elementos2):
    num2 = int(input(f'Digite el numero en la posicion: {i} '))
    VectorNum2.append(num2)
    if(num2 % 2 == 0):
        es_primo(num2)
        VectorPar.append(num2)
    else: 
        es_primo(num2)
        VectorImpar.append(num2)
print(f'Los elementos del vector son : {VectorNum2}')
print(f'Los numeros pares son : {VectorPar}')
print(f'Los numeros impares son : {VectorImpar}')
print(f'Los numeros primos son : {VectorPrimo}')
# Punto3
VectorNum3 = []
VectorNum4 = []
VectorSuma = []
VectorResta = []
Elementos3 = int(input('Digite la cantidad de elementos para los vectores: '))
for i in range(Elementos3):
    num3 = float(input(f'Digite el numero del vector 1 en la posicion: {i} '))
    num4 = float(input(f'Digite el numero del vector 2 en la posicion: {i} '))
    suma = num3 + num4
    resta = num3 - num4
    VectorSuma.append(suma)
    VectorResta.append(resta)
    VectorNum3.append(num3)
    VectorNum4.append(num4)
print(f'Los elementos del vector 1 son: {VectorNum3}')
print(f'Los elementos del vector 2 son: {VectorNum4}')
print(f'El resultado de su suma es : {VectorSuma}')
print(f'El resultado de su resta es : {VectorResta}')
# Punto4
VectorNum5 = []
Elementos4 = int(input('Digite la cantidad de elementos del vector: '))
for i in range(Elementos4):
    num5 = float(input(f'Digite el numero del vector en la posicion: {i} '))
    VectorNum5.append(num5)
print(f'El numero que mas se repite es: {mode(VectorNum5)}')
# Punto5
VectorNum6 = []
VectorProductoria2 = []
VectorSumatoria2 = []
VectorTotal = []
Productoria2 = 1
Sumatoria2 = 0
Elementos5 = int(input('Digite la cantidad de elementos del vector: '))
par = int(Elementos5 / 2)
if(Elementos5 % 2 == 0):
    for i in range(par):
        num6 = float(input(f'Digite el numero de la primera mitad del vector en la posicion: {i} '))
        Productoria2 = Productoria2 * num6
        VectorProductoria2.append(Productoria2)
        VectorNum6.append(num6)
        VectorTotal.append(Productoria2)
    for i in range(par):
        num7 = float(input(f'Digite el numero de la segunda mitad del vector en la posicion: {i} '))
        Sumatoria2 = Sumatoria2 + num7
        VectorSumatoria2.append(Sumatoria2)
        VectorNum6.append(num7)
        VectorTotal.append(Sumatoria2)
    print(f'El vector es: {VectorNum6}')
    print(f'Su productoria es: {Productoria2} y su vector en la primera mitad es : {VectorProductoria2}')
    print(f'Su sumatoria es: {Sumatoria2} y su vector en la segunda mitad es: {VectorSumatoria2}')
    print(f'El vector resultante es : {VectorTotal}')
else:
    print('Por favor digite una longitud de vector que sea par')
# Punto6
VectorNum7 = []
Elementos6 = int(input('Digite la cantidad de elementos del vector: '))
if(Elementos6 % 2 == 0):
    for i in range(Elementos6):
        num9 = float(input(f'Digite el numero del vector en la posicion: {i} '))
        VectorNum7.append(num9)
    medio = int(len(VectorNum7) / 2)
    primeramitad = VectorNum7[:medio]
    segundamitad = VectorNum7[medio:]
    if(primeramitad == segundamitad[::-1]):
        print(f'El vector: {VectorNum7} es simetrico')
    else:
        print(f'El vector: {VectorNum7} no es simetrico')
elif(Elementos6 <= 1):
    print('Digite un numero mayor a 1')
else:
    for i in range(Elementos6):
        num10 = float(input(f'Digite el numero del vector en la posicion: {i} '))
        VectorNum7.append(num10)
    print(f'El vector es : {VectorNum7}')
    medio = int(len(VectorNum7) / 2)
    VectorNum7.pop(medio)
    print(f'Ignorando el numero del medio seria asi: {VectorNum7}')
    primeramitad = VectorNum7[:medio]
    segundamitad = VectorNum7[medio:]
    if(primeramitad == segundamitad[::-1]):
        print(f'El vector sin el numero del medio: {VectorNum7} es simetrico')
    else:
        print('El vector no es simetrico')
# Punto7
VectorA = []
VectorB = []
ElementosVectores = int(input('Digite la cantidad de elementos para los vectores: '))
for i in range(ElementosVectores):
    numeroA = float(input(f'Digite el numero del vector A en la posicion: {i} '))
    VectorA.append(numeroA)
for i in range(ElementosVectores):
    numeroB = float(input(f'Digite el numero del vector B en la posicion: {i} '))
    VectorB.append(numeroB)
Va = set(VectorA)
Vb = set(VectorB)
union = Va | Vb
interseccion = Va & Vb  
diferenciaAB = Va - Vb
diferenciaBA = Vb - Va
print(f'La union tiene como elementos : {union} ')
print(f'La interseccion tiene como elementos : {interseccion} ')
print(f'La diferencia de A - B tiene como elementos : {diferenciaAB} ')
print(f'La diferencia de B - A tiene como elementos : {diferenciaBA} ')
