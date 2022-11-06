"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)


def binary_predict(number:int=1) -> int:
    """Оптимизированное угадывание числа из диапазона от 1 до 100.
       Бинарный вариант.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    first_number = 1
    last_number = 100

    while True:
        count += 1
        predict_number = (first_number + last_number) // 2 # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number > predict_number:
            first_number = predict_number + 1
        else:
            last_number = predict_number - 1
    return(count)

def score_game(predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов 
    угадывает наш алгоритм

    Args:
        predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = (np.mean(count_ls)) # находим среднее количество попыток

    print(f'Aлгоритм {predict.__name__} угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
    score_game(binary_predict)