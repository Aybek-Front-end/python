number = 23
running = True

while running:
    guess = int(input('Введите целое число: ')) 

    if guess == number:
        print('Поздровляю вы угодали')
        running = False # Остановка цикла while
    elif guess < number:
        print('Нет, Загаданное число немного больше этого.')
    else:
        print('Нет загадонное число немного меньше этого.')
else:
    print ('Цикл while закончен.')
    # Здесь можете выполнить всё что вам нужно

print ('Завершено!')