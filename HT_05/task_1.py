# HT #05
# 1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь). У випадку некоректного введеного значення - виводити відповідне повідомлення.
months = {
    "winter" : [12,1,2],
    "spring" : [3,4,5],
    "summer" : [6,7,8],
    "autumn" : [9,10,12]
}

def season(month_n):
    for seas, mon in months.items():
        if month_n in mon:
            return seas
    return "There is no such month"

print(season(int(input("Month: "))))