
f = open('test.txt', 'r', encoding='utf-8')
print(f)
# В данном коде мы открываем файл с именем "test.txt" в режиме чтения ('r') и
# указываем кодировку 'utf-8'.
# Переменная "f" будет содержать ссылку на открытый файл.
# Затем мы выводим переменную "f" с помощью функции "print".
# Это позволит нам увидеть информацию о файле, такую как его путь,
# режим открытия и кодировку.

f = open('test.txt', 'r', encoding='utf-8')
f_contents = f.read()
f.close()

print(f_contents)
# Открываем файл 'test.txt' в режиме чтения (`'r'`) с указанием кодировки utf-8.
# Затем мы используем метод `read()`,
# чтобы прочитать содержимое файла и сохранить его в переменную `f_contents`.
# Наконец, мы закрываем файл с помощью метода `close()`.
# Можем использовать переменную `f_contents` для дальнейшей обработки
# содержимого файла.
