# MiniCode
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Русский (Russian)
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Сбор коротких сточек кода для начала обучения Python

-----------------------------------------------------------------------------------------------------------------------------------------------------------
English (Английский)
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Collecting short lines of code to start learning Python

===Рус==========================================================================
```
numbers = '1 2 3 4 5 6 7'
numbers_splited = numbers.split()
numbers_new = '\n'.join(numbers_splited)
print(numbers_new)
```

Представим что вы директор компании и производите высококачественные столы из дуба, которые состоят из ножек, столешницы и разных крепежей `'1 2 3 4 5 6 7'`. Продаёте вы их в небольшом контейнере насыпью `numbers`, но вот один из клиентов вас просит упаковать каждый элемент чтобы было понятно  это ножки это столешница это болты это др элементы крепления `['1', '2', '3', '4', '5', '6', '7']` вы вызываете одного работника `split` который это сделает в новый контейнер `numbers_splited` (можно и в старый, но вам не жалко ещё одного контейнера), но тут этот же клиент просит распаковать и уложить в определённом порядке все части стола. И вы вызываете нового сотрудника `.join` который распаковывает  и укладывает определённым образом `'\n'` ваш стол в новый контейнер `numbers_new` (можно и в старый, но вам не жалко ещё одного контейнера)
да забыл про поставку `print` покупателю контейнера `numbers_new`
===Eng==========================================================================
```
numbers = '1 2 3 4 5 6 7'
numbers_splited = numbers.split()
numbers_new = '\n'.join(numbers_splited)
print(numbers_new)
```

Let's imagine that you are the director of a company and produce high-quality oak tables, which consist of legs, a table top and various fasteners `'1 2 3 4 5 6 7'`. You sell them in a small container in bulk `numbers`, but one of your clients asks you to pack each element so that it is clear these are the legs this is the table top these are the bolts these are other fastening elements `['1', '2', '3', '4 ', '5', '6', '7']` you call one worker `split` who will do this in the new container `numbers_splited` (you can do it in the old one, but you don’t mind one more container), but here is the same the client asks to unpack and arrange all parts of the table in a certain order. And you call a new employee `.join` who unpacks and places `'\n'` your table in a certain way into a new container `numbers_new` (you can also put it in the old one, but you don’t mind another container)
yeah, I forgot about delivering `print` to the buyer of the `numbers_new` container

================================================================================
