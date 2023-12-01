# 4. Create 'list'-like object, but index starts from 1 and index of 0 raises error.
# Тобто це повинен бути клас, який буде поводити себе так, як list (маючи основні методи),
# але індексація повинна починатись із 1

class CustomList:
    def __init__(self,data = []):
        self._data = data

    def __getitem__(self, index):
        if isinstance(index, int):
            if index == 0:
                raise IndexError("Index starts from 1")
            if index < 0:
                index = len(self._data) + index + 1
            return self._data[index - 1]
        else:
            return self._data[index]

    def __setitem__(self, index, value):
        if isinstance(index, int):
            if index == 0:
                raise IndexError("Index starts from 1")
            if index < 0:
                index = len(self._data) + index + 1
            if index > len(self._data):
                self._data.extend([None] * (index - len(self._data)))
            self._data[index - 1] = value
        else:
            self._data[index] = value

    def __delitem__(self, index):
        if isinstance(index, int):
            if index == 0:
                raise IndexError("Index starts from 1")
            if index < 0:
                index = len(self._data) + index + 1
            del self._data[index - 1]
        else:
            del self._data[index]
    
    def __len__(self):
        return len(self._data)

    def append(self, value):
        self._data.append(value)

    def extend(self, values):
        self._data.extend(values)

    def remove(self, value):
        self._data.remove(value)

    def pop(self, index=-1):
        if index == 0:
            raise IndexError("Index starts from 1")
        return self._data.pop(index - 1)

    def insert(self, index, value):
        if index == 0:
            raise IndexError("Index starts from 1")
        self._data.insert(index - 1, value)

    def index(self, value, start=1, stop=None):
        return self._data.index(value, start - 1 if start else start, stop)

    def count(self, value):
        return self._data.count(value)

    def clear(self):
        self._data.clear()
    
    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index < len(self._data):
            result = self._data[self._iter_index]
            self._iter_index += 1
            return result
        else:
            raise StopIteration

    def __repr__(self):
        return repr(self._data)
    
    

custom_list = CustomList()
custom_list.append('a')
custom_list.extend(['b', 'c',3])
print(custom_list)
print(len(custom_list))

# Операції індексації
print(custom_list[1])
print(custom_list[2])
print(custom_list[-1])
print(custom_list[1])
for i in custom_list:
    print(i)    
