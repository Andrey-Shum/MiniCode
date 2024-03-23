# Класс
class Person:
    name = "Иван"  # атрибут класса
    gender = "Муж"  # атрибут класса
    age = 18  # атрибут класса


# Объекты класса (Point) или пространство имён
Alex = Person()
Bronislava = Person()

Person.age = 21  # изменение значения атрибута класса
setattr(Person, "age", 27)   # изменение значения атрибута класса

Alex.name = "Алексей"  # Изменение значения атрибута объекта
Bronislava.name = "Бронислава"  # Изменение значения атрибута объекта
Bronislava.gender = "Жен"  # Изменение значения атрибута объекта

# Добавление атрибута класса
Person.surname = "Иванов"
setattr(Person, "patronymic", "Иванович")
# задаёт значение атрибута (если атрибут не существует, то он создаётся)

# Чтение атрибута класса или объекта класса
Person.name

Alex.name

N = Person.name

getattr(Person, "name", False)  # Возвращает значение атрибута объекта

# Вывод атрибута класса или объекта класса
print(Person.name)

print(Alex.name)

print(N)

# проверка наличия атрибута класса
hasattr(Person, "age")  # проверяет на наличие атрибута age в Person

# Удаление атрибутов класса
del Person.age
delattr(Person, "patronymic")  # удаляет атрибут с именем patronymic

print(Alex.__dict__)

# __doc__ Содержит строку с описанием класса (если есть описание)
# __dict__ содержит набор атрибутов экземпляра класса.
