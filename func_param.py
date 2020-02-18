def printMax (a,b):
    if a > b:
        print(a, 'максимально')
    elif a==b:
        print(a,'равно', b)
    else:
        print(b, 'максимально')
printMax(3,3)

x = input('Введите x: ')
y = input('Введите y: ')
printMax(x,y)