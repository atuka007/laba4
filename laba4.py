import re

digit_to_word = {'0': 'ноль','1': 'один','2': 'два','3': 'три','4': 'четыре',
    '5': 'пять','6': 'шесть','7': 'семь','8': 'восемь','9': 'девять'}

def number_to_words(number): # Преобразует число в строку с названиями цифр
    return ' '.join(digit_to_word[digit] for digit in str(number))

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            nums = re.findall(r'-?\d{3,}[13579]', content) # Ищем все целые числа (нечетные и более 3 цифр, возможно отрицательные)
            numbers = [int(num) for num in nums]

            print(f"Найденные числа: {numbers}")
            print(f"Количество чисел: {len(numbers)}")
            if numbers:
                print(f"Максимальное число: {max(numbers)}")
                print(f"Прописью: {number_to_words(max(numbers))}")
            else:
                print("\nНе найдено подходящих чисел.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
file_path = 'input.txt'
process_file(file_path)
