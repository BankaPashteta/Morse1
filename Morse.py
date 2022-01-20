rus_alph = {"А": '.-', "Б": '-...', "В": '.--', "Г": '--.', "Д": '-..', "Е": '.', "Ё": '.',
            "Ж": '...-', "З": '--..', "И": '..', "Й": '.---', "К": '-.-', "Л": '.-..',
            "М": '--', "Н": '-.', "О": '---', "П": '.--.', "Р": '.-.', "С": '...', "Т": '-',
            "У": '..-', "Ф": '..-.', "Х": '....', "Ц": '-.-.', "Ч": '---.', "Ш": '----',
            "Щ": '--.-', "Ъ": '--.--', "Ы": '-.--', "Ь": '-..-', "Э": '..-..', "Ю": '..--',
            "Я": '.-.-', ' ': '-----', '.': '......', ',': '.-.-.-', "'": '.----.'}
eng_alph = {'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.",
            'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.",
            'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-", 'U': "..-",
            'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--..", ' ': '-----',
            '.': '......', ',': '.-.-.-', "'": '.----.'}
av_symb = {'Ф', 'R', 'Д', 'Э', 'I', 'N', 'Т', 'О', 'B', 'O', ' ', 'З', 'K', 'С', 'Х', 'V', 'Е',
           'A', '.', 'P', 'Г', 'J', 'M', 'К', 'G', 'А', 'И', 'Ж', 'C', 'F', 'L', 'Я', 'E', 'Y',
           'D', 'П', 'Ю', 'Л', 'U', 'Ё', 'У', 'Ч', 'Ъ', 'Б', 'W', 'Ы', 'Р', ',', 'М', 'X', 'Q',
           'T', 'Й', 'В', 'Щ', 'Ш', 'Z', 'S', 'Н', 'Ь', 'H', 'Ц', "'"}


def isRus(text):
    # Проверка является ли текст русским
    for letter in text:
        if letter.upper() in rus_alph.keys():
            continue
        else:
            return False
    return True


def isMorse(text):
    # Проверка является ли введенный текст азбукой морзе
    for letter in text:
        if letter == ' ' or letter == '-' or letter == '.':
            continue
        else:
            return False
    return True


def rus_to_morse(text):
    # Переводим с русского на морзе
    s = []
    for i in text:
        s.append(rus_alph[i.upper()])
    return ' '.join(s)


def eng_to_morse(text):
    # Переводим с английского на морзе
    s = []
    for i in text:
        s.append(eng_alph[i.upper()])
    return ' '.join(s)


def value_to_key(value, dictionary):
    # Получаем ключ по значению
    for elem in dictionary.items():
        if value == elem[1]:
            return elem[0]


def morse_to_eng(code):
    # Переводим морзе на английский язык
    decoded = ''
    words_morse = code.split('_____')
    for w in words_morse:
        letters_morse = w.split()
        for lm in letters_morse:
            decoded += value_to_key(lm, eng_alph)
        decoded += ' '
    return decoded[:-1]


def morse_to_ru(code):
    # Переводим морзе на русский язык
    decoded = ''
    words_morse = code.split('_____')
    for w in words_morse:
        letters_morse = w.split()
        for lm in letters_morse:
            decoded += value_to_key(lm, rus_alph)  # Вставь названия русского словаря
        decoded += ' '
    return decoded[:-1]


def main():
    print('Допустимые символы - кириллица, латиница, пробел, апостроф, точка и запятая')
    c = input('Введите текст на русском, на английском или на морзе \n')
    # Получаем текст
    a = not isMorse(c)  # Проверяем не является ли текст языком морзе
    if a:
        # Проверка на наличие недопустимых символов
        for j in c:
            if j.upper() not in av_symb:
                print('Недопустимый символ -', j)
                return
        b = isRus(c)  # Проверяем не является ли текст русским
        if b:
            text = rus_to_morse(c)
        else:
            text = eng_to_morse(c)
    else:
        b = input('На какой язык перевести расшифованный текст?\nна русский - 1 / на английский'
                  ' - 2\n')
        if b == '1':
            text = morse_to_ru(c)
        else:
            text = morse_to_eng(c)
    print(text)


main()
