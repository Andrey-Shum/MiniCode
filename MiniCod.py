# ____________Строки Индексы и Срезы____________________________________________

#  Ввод строки и отображения на экране ее первого и последнего символа
#  (в виде одной строки).
text = input('Текст пожалуйста: ')
print(text[0]+text[-1])

# Отображения первых четырех символов из введенной строки.
# (Строка гарантированно длиннее)
text = input("Текст пожалуйста: ")
print(text[:4])
# или однострочное
print(input('Текст пожалуйста: ')[:4])

# Отображения последних трёх символов из введенной строки.
# (Строка гарантированно длиннее)
text = input('Текст пожалуйста: ')
print(text[-3:])
# или однострочное
print(input('Текст пожалуйста: ')[-3:])

# Отображения всех символов с нечетными индексами из введенной строки
print(input('Текст пожалуйста: ')[1::2])

# Из первой строки выделить всё символы с чётными индексами,
# а из второй - с нечетными.
# Объединить строки через пробел и вывести на экран.
text1 = input('Текст №1 пожалуйста: ')
text2 = input('Текст №2 пожалуйста: ')
print(text1[0::2] + " " + text2[1::2])

# Отобразить первые пять символов в обратном порядке (Разворот).
# (Строка гарантированно длиннее)
print(input('Текст пожалуйста: ')[4::-1])

# Вводятся два слова (через пробел в одной строке). Длина первого слова меньше
# второго.
# Необходимо обрезать второе слово до длины первого и отобразить.
text1, text2 = map(str, input('два слова через пробел длинна 1 < 2: ').split())
len1 = str(len(text1))
print(text2[:int(len1)])

# Вводятся два слова (через пробел в одной строке). Длина второго слова меньше
# первого.
# Из этих слов выделить символы с нечетными индексами с обрезкой первого слова
# до длины второго.
# Сравнить полученные строки между собой на равенство и результат
# (True или False) вывести на экран.
a, b = map(str, input('два слова через пробел длина 2 < 1: ').split())
a2 = a[1::2]
b2 = b[1::2]
a3 = a2[:len(b2)]
print(b2 == a3)


# Выводит построчно. Каждое число из строки numbers
numbers = '1 2 3 4 5 6 7'

numbers_splited = numbers.split()
# Разбиваем строковую последовательность по пробелам в список
numbers_new = '\n'.join(numbers_splited)
# Формируем новую строковую из списка с переносами
print(numbers_new)
#
numbers_new = '\n'.join(numbers.replace(' ', ''))
# replace - метод замены одного на другое в строке
print(numbers_new)
# или
print("\n".join(numbers.split(" ")))
# Используем метод split() для разделения строки на отдельные числа, передавая
# пробел в качестве разделителя
# Затем, используем метод join() для объединения чисел с новой строки
# После этого передаем результат в функцию print для вывода построчно
# или
print(*numbers.split(), sep='\n')
# Используем метод split() для разделения строки на отдельные числа,
# передавая пробел в качестве разделителя
# * распаковывает список и передает каждую подстроку в функцию print()
# в качестве отдельного аргумента.
# Затем, используя функцию print с параметром sep='\n', мы выводим числа
# построчно или через цикл for
print(*(num for num in numbers.split()), sep='\n')
# Используем метод split() для разделения строки на отдельные числа, передавая
# пробел в качестве разделителя * распаковывает список и передает каждую
# подстроку в функцию print() в качестве отдельного аргумента.
# Затем, используя функцию print с параметром sep='\n', мы выводим числа
# построчно
# Параметр sep определяет строку, которая будет вставлена между каждым объектом
# при их выводе.
# По умолчанию sep=' ' (пробел), что означает, что между объектами будет
# вставлен пробел. В нашем случае sep='\n'


# Округление до
pii = 31.4159265
print("%.4e" % pii)
# Форматирование (%.4e) используется для преобразования числа в экспоненциальную
# запись с заданным числом знаков после десятичной точки. (.4) указывает,
# что после десятичной точки будет 4 знака. (e) указывает на использование
# экспоненциальной записи. Таким образом, в ответе 3.1416 округлено до 4 знаков
# после десятичной точки, а e+01 указывает на то, что это значение
# в экспоненциальной записи с порядком 10^1.

# _________ Циклы ______________________________________________________________
# Проверка на вхождение цифры 5 в число
n = int(input("Введите число: "))
i = 10
found = False

while n > 0:
    num = n % i
    n = n // i

    if num == 5:
        print("Число содержит цифру 5")
        found = True
        break

if not found:
    print("Число не содержит цифру 5")

# Проверка на вхождение цифры в число
num = int(input("Введите число: "))
found = False
num_check = int(input("Какую цифру ищем: "))

num = abs(num)
# Использование функции abs() для работы с отрицательными числами
#  функции abs(), которая возвращает абсолютное значение числа
#  (то есть, она преобразует отрицательные числа в положительные)

while num > 0:
    digit = num % 10
    if digit == num_check:
        print(f"Есть {num_check}")
        found = True
        break
    num = num // 10

if not found:
    print(f"{num_check} отсутствует")
