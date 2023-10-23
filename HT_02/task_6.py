# HT_02
# 6. Write a script to check whether a value from user input is contained in a group of values.    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#          [1, 2, 'u', 'a', 4, True] --> 5 --> False

m_list = ["hello",2,True,3.2,"nice"]
user = input("Введіть що перевірити:")
print("Чи міститься значення у списку:", user in [str(item) for item in m_list])
