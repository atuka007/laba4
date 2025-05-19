import re

def number_to_words(num):
    if num == 0:
        return "ноль"

    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот","шестьсот", "семьсот", "восемьсот", "девятьсот"]
    thousands = ["", "тысяча", "тысячи", "тысяч"]
    words = []

    if num >= 1000: # Обрабатываем тысячи
        thousand_part = num // 1000
        num %= 1000
        if thousand_part > 0:
            if thousand_part >= 100:
                h = thousand_part // 100
                words.append(hundreds[h])
                thousand_part %= 100
            if thousand_part >= 20:
                t = thousand_part // 10
                words.append(tens[t])
                thousand_part %= 10
            if thousand_part >= 10:
                words.append(teens[thousand_part - 10])
                thousand_part = 0
            if thousand_part > 0:
                if thousand_part == 1:
                    words.append('одна')
                elif thousand_part == 2:
                    words.append('две')
                else:
                    words.append(units[thousand_part])
            last_digit = thousand_part % 10 # Определяем правильную форму слова "тысяча"
            if 2 <= last_digit <= 4:
                words.append(thousands[2])
            elif last_digit == 1:
                words.append(thousands[1])
            else:
                words.append(thousands[3])

    if num >= 100:  # Обрабатываем сотни
        h = num // 100
        words.append(hundreds[h])
        num %= 100

    if num >= 20:  # Обрабатываем десятки
        t = num // 10
        words.append(tens[t])
        num %= 10

    if num >= 10:  # Обрабатываем 10-19
        words.append(teens[num - 10])
        num = 0

    if num > 0:  # Обрабатываем единицы
        words.append(units[num])

    return ' '.join(words).strip()

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            numbers = re.findall(r'\d{4,}', content) # Возвращает список совпадений

            filtered_numbers = []
            for num_str in numbers:
                num = int(num_str)
                if num % 2 != 0:
                    filtered_numbers.append(num)

            print(f"Количество чисел: {len(filtered_numbers)}")
            if filtered_numbers:
                max_num = max(filtered_numbers)
                print(f"Максимальное число: {max_num}")
                print(f"Прописью: {number_to_words(max_num)}")
            else:
                print("Не найдено подходящих чисел.")

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = 'input.txt'
process_file(file_path)