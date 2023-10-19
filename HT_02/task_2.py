# HT_02
# 2. Write a script which accepts two sequences of comma-separated colors from user. Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.


color_1,color_2 = (input("Color list 1: ")).split(","), (input("Color list 2: ")).split(",")
print(set(color_1)-set(color_2))

