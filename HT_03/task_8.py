#HT_03
#Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.
for i in range(0,int(input("Number: ")) + 1):
    if i % 17 == 0:
        print(i)