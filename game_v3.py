import numpy as np
#
def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем рандомно любое число (predict). Если оно больше загаданного (number)
       то делаем его правым пределом. Если меньше - левым. Находим половину отрезка между левам и правым пределами
       на каждом шаге. Снова устанавливаем новые пределы и находим половину указанного отрезка, пока не получим
       predict == number.
       Функция принимает загаданное число и возвращает число попыток 
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
#
    count = 0
    temp_l = 1 # временные переменные для обозначения левого и правого пределов на каждом шаге
    temp_r = 100
# 
    predict = np.random.randint(1, 101) # первый раз устанавливаем рандомно отправную точку для predict
#  цикл, осуществляющий схему деления уменьшающегося отрезка пополам --------------
    while number != predict:
        count += 1
        if number > predict:
            temp_l=predict
            predict = temp_l+int((temp_r-temp_l)/2)
        elif number < predict:
            temp_r=predict
            predict = temp_l+int((temp_r-temp_l)/2)
        if number == 100 and predict == 99: # здесь угадываем вручную, т.к. округление при %2 идет в меньшую сторону
           predict =100
    # ---------------------------------------------
    # Ваш код заканчивается здесь

    return count
#
def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
