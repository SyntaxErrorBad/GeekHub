# HT #09
# 1. Програма-світлофор.
#    Створити програму-емулятор світлофора для авто і пішоходів.
#  Після запуска програми на екран виводиться в лівій половині - колір автомобільного, 
# а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні кольори. 
# Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних 
# світлофорах (пішоходам зелений тільки коли автомобілям червоний).   Приблизний результат роботи наступний:
#       Red        Green
#       Red        Green
#       Red        Green
#       Red        Green
#       Yellow     Red
#       Yellow     Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Yellow     Red
#       Yellow     Red
#       Red        Green

import time

time_delay = 5
cars_lights = ["Red", "Yellow", "Green"]
human_lights = ["Red", "Green"]


def traffic_lights(real_time=False, infinity=False):
    i = 0
    while i < 2:
        for _ in range(10):
            if _ < time_delay-1:
                print("{}     {}".format(cars_lights[0], human_lights[-1]))
            elif _ == time_delay or _ == time_delay-1:
                print("{}    {}".format(cars_lights[1], human_lights[0]))
            else:
                print("{}     {}".format(cars_lights[-1], human_lights[0]))
            if real_time:
                time.sleep(1)
        print("_"*100)
        if not infinity:
            i += 1


traffic_lights(real_time=True)
