print('Программа')

start = ('Старт')
running = True

while running:
    guess = input('Введите команду: ')

    if guess == start:
        print('Запуск...')
        
        for i in range(1, 11):
            print(i)

        running = False

    else:
        print('Ошибка! Команда не распознана')
else:
    print('Программа запущенна успешно!')


