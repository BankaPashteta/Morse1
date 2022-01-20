rus_alph = {"А": '.-', "Б": '-...', "В": '.--', "Г": '--.', "Д": '-..', "Е": '.', "Ё": '.',
            "Ж": '...-', "З": '--..', "И": '..', "Й": '.---', "К": '-.-', "Л": '.-..',
            "М": '--', "Н": '-.', "О": '---', "П": '.--.', "Р": '.-.', "С": '...', "Т": '-',
            "У": '..-', "Ф": '..-.', "Х": '....', "Ц": '-.-.', "Ч": '---.', "Ш": '----',
            "Щ": '--.-', "Ъ": '--.--', "Ы": '-.--', "Ь": '-..-', "Э": '..-..', "Ю": '..--',
            "Я": '.-.-', ' ': '-----', '.': '......', ',': '.-.-.-'}
eng_alph = {'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.",
            'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.",
            'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-", 'U': "..-",
            'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--..", ' ': '-----',
            '.': '......', ',': '.-.-.-'}


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
        for l in letters_morse:
            decoded += value_to_key(l, rus_alph)  # Вставь названия русского словаря
        decoded += ' '
    return decoded[:-1]


def main():
    c = input('Введите текст\n')
    # Получаем текст
    a = input('Вы ходить зашифровать или расшифровать текст?\nрасшифровать - 1 / зашифровать - 2\n')
    # Определяем что пользователю надо
    if a == '2':
        b = input('На каком языке написан текст?\nна русском - 1 / на английском - 2\n')
        print('*пробелы обозначаются пятью нижними подчёркиваниями')
        if b == '1':
            text = rus_to_morse(c)
        else:
            text = eng_to_morse(c)
    else:
        b = input('На какой язык перевести расшифованный текс?\nна русский - 1 / на английский - 2\n')
        if b == '1':
            text = morse_to_ru(c)
        else:
            text = morse_to_eng(c)
    print(text)


main()
