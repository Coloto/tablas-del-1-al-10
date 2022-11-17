print('Tablas de multiplicar')
tablas=[1,2,3,4,5,6,7,8,9,10]
for x in tablas:
    print(f'Tabla del {x}')
    for y in range(10):
        resultado=x*y
        print(f'{x} * {y} es {resultado}')
