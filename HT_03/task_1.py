#HT_03
#1. Write a script that will run through a list of tuples and replace the last value for each tuple. 
#The list of tuples can be hardcoded. The "replacement" value is entered by user. The number of elements in the tuples must be different.

tuples = [(1, 2, 3), (4, 5), (6, 7, 8, 9),()]
item = int(input("Число: "))
new_tuple_list = []
for i in tuples:
    if len(i) != 0:
        tup = list(i)
        tup[-1] = item
        new_tuple_list.append(tuple(tup)) 
    else:
        new_tuple_list.append(i)

print(new_tuple_list)
