import numpy as np
limit = int(input('В каких пределах угадываем? От 1 до ')) #мне стало интересно, как будет меняться число попыток от верхнего предела выборки
#limit = 100 #если нужно именно 100 в решении
def game_core():
    number = np.random.randint(1,limit+1) #загадываем число
    compare = limit #ищущее число, изначально равно нашему диапазону
    interval = limit #вспомогательное число стремящееся к нулю делением на 2, изначально равно ищущему
    count = 0 #счётчик попыток
    for i in range(1, limit+1):
        count += 1 #считаем попытку
        if number==compare:
            return(count)
            break #если нашли - отбой
        elif number<compare: #если искомое меньше
            interval //= 2 #делим вспомогательное на два
            compare -= interval #и отнимаем от ищущего числа
            if interval<1: #исправляем ошибку округления на финальном шаге
                compare -= 1
        else: #если искомое больше
            interval //= 2 #делим вспомогательное на два
            compare += interval #и прибавляем к ищущему числу
            if interval<1: #исправляем ошибку округления на финальном шаге
                compare += 1

def score_game(game_core):
    count_ls = [] #создаём пустой список
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1, limit+1, size=(1000))
    for number in random_array:
        count_ls.append(game_core()) #добавляем к списку число попыток из game_core
    score = int(np.mean(count_ls)) #берём среднее арифметическое по числу попыток
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core)