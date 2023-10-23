#HT_03
#2. Write a script to remove an empty elements from a list.    Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

new_list = []

for element in test_list:
    if len(element) != 0:
        if len(element[0]) != 0:
            new_list.append(element)

print(new_list)
