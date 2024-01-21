# Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе та виводить
# декодоване значення (латинськими літерами).
#    Особливості:
#     - використовуються лише крапки, тире і пробіли (.- )
#     - один пробіл означає нову літеру
#     - три пробіли означають нове слово
#     - результат може бути case-insensetive (на ваш розсуд - велики чи маленькими літерами).
#     - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не будуть.
#     Лише латинські літери.
#     - додайте можливість декодування сервісного сигналу SOS (...---...)
#     Приклад:
#     --. . . -.- .... ..- -...   .. ...   .... . .-. .
#     результат: GEEKHUB IS HERE


def morse_code(morse, code=True):
    morse_dict = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
        "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
        "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
        ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
        "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",
        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
    }
    if code:
        words = morse.split("   ")
        phrase = []
        for word in words:
            word_list = []
            letters = word.split(" ") 
            for letter in letters:
                word_list.append(morse_dict[letter])

            phrase.append(''.join(word_list))
        return (' '.join(phrase)).upper()
    else:
        words = morse.split()
        phrase = ('   '.join(words)).lower()
        coded_phrase = []
        for letter in phrase:
            if letter != " ":
                coded_phrase.append(''.join([i for i, j in morse_dict.items() if j == letter]))
                coded_phrase.append(" ")
            else:
                coded_phrase.append(" ")
        return ''.join(coded_phrase)


morse_input = "--. . . -.- .... ..- -...   .. ...   .... . .-. ."
decoded_text = morse_code("GEEKHUB IS HERE", False)
print(decoded_text)
