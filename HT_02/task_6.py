# HT_02
# 6. Write a script to check whether a value from user input is contained in a group of values.    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#          [1, 2, 'u', 'a', 4, True] --> 5 --> False
# HT_02
# 6. Write a script to check whether a value from user input is contained in a group of values.    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#          [1, 2, 'u', 'a', 4, True] --> 5 --> False

m_list = ["hello",2,True,3.2,"nice"]

#Варіант 1
def type_input(item):
    if item.isdigit():
        return float(item)
    elif item == "True":
        return True
    elif item == "False":
        return False
    else:
        return str
user = input("Введіть що перевірити:")
print("Чи міститься значення у списку:", type_input(user) in m_list)

#Вараінт 2
def choose_type(ch_type):
    if ch_type == "bool":
        return bool(input("Введіть що перевірити:"))
    elif ch_type == "int":
        return int(input("Введіть що перевірити:"))
    elif ch_type == "float":
        return float(input("Введіть що перевірити:"))
    elif ch_type == "str":
        return str(input("Введіть що перевірити:"))
    else:
        print("Нажаль такого немає")

user = choose_type(input("Введіть тип яких хочете перевірити [str,int,float,bool]: "))
print("Чи міститься значення у списку:", user in m_list)
