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


def traffic_light_emulator():
    car_colors = ["Red", "Yellow", "Green"]
    pedestrian_colors = ["Red", "Green"]

    car_index = 0
    pedestrian_index = 0

    while True:
        car_color = car_colors[car_index]
        pedestrian_color = pedestrian_colors[pedestrian_index]
        
        print(f"{car_color:<10} {pedestrian_color:>10}")

        time.sleep(1)

        if car_color == "Green":
            pedestrian_index = (pedestrian_index + 1) % len(pedestrian_colors)

        car_index = (car_index + 1) % len(car_colors)

traffic_light_emulator()
