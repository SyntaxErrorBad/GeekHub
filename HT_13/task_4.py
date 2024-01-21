# 4. Create 'list'-like object, but index starts from 1 and index of 0 raises error.
# Тобто це повинен бути клас, який буде поводити себе так, як list (маючи основні методи),
# але індексація повинна починатись із 1

class NewCustom(list):
    def adjust_index(self, key):
        if key >= 1:
            return key - 1
        elif key == 0:
            raise IndexError("Index starts from 1")
        else:
            return key

    def __getitem__(self, key):
        key = self.adjust_index(key)
        return super(NewCustom, self).__getitem__(key)
    
    def __setitem__(self, key,value):
        key = self.adjust_index(key)
        return super(NewCustom, self).__setitem__(key,value)

    def __delitem__(self, key):
        key = self.adjust_index(key)
        return super(NewCustom, self).__delitem__(key)

    def index(self, value):
        return (super(NewCustom, self).index(value))+1
    
    def pop(self, key):
        return super(NewCustom, self).pop(key - 1)

    def insert(self, key, element):
        return super(NewCustom, self).insert(key-1,element)
    
    

custom_list = NewCustom()
custom_list.append('a')
custom_list.append('b')
print(custom_list)
custom_list.reverse()
custom_list.extend(['b', 'c',3])
print(custom_list)
print(len(custom_list))
print(custom_list[1])
print(custom_list[-1])
print(custom_list.index('b'))
custom_list.pop(-1)
print(custom_list)
custom_list.insert(2,"c")
print(custom_list)
custom_list[1] = "g"
print(custom_list)
print(custom_list.count("b"))
del custom_list[1]
print(custom_list)
for i in custom_list:
    print(i)       
