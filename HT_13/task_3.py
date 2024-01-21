# 3. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    def get_count(self):
        return Counter.count
    

counter1 = Counter()
counter2 = Counter()
print(counter1.get_count())
counter3 = Counter()
print(counter1.get_count())
