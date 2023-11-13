# 2. Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. 
# Файл також додайте в репозиторій. На екран повинен вивестись список із трьома блоками - 
# символи з початку, із середини та з кінця файлу. Кількість символів в блоках - та, яка введена 
# в другому параметрі. Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, 
# ніж є в файлі або, наприклад, файл із двох символів і треба вивести по одному символу, то що 
# виводити на місці середнього блоку символів?). Не забудьте додати перевірку чи файл існує.
def display_file_blocks(file_path, block_size):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        file_good = True
        if len(content) <= 2:
            print("Занадто малий файл")
            file_good = False
        elif len(content)//3 < block_size:
            block_size = len(content)//3
            file_good = True
        elif block_size > len(content):
            block_size = len(content)
            file_good = True

        if file_good:
            middle_index = len(content) // 2

            start_block = content[:block_size]
            middle_block = content[middle_index - block_size // 2:middle_index + block_size]
            end_block = content[-block_size:]

            print(f"Символи з початку файлу ({block_size} символів):\n{start_block}")
            print(f"Символи з середини файлу ({block_size} символів):\n{middle_block}")
            print(f"Символи з кінця файлу ({block_size} символів):\n{end_block}")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не існує.")
    except Exception as e:
        print(f"Виникла помилка: {str(e)}")


display_file_blocks("Task2_files\\sample.txt", 10)
