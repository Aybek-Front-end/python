x = 50

# область видимости переменной
def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального х на', x)

func(x)
print('х по прежнему', x)