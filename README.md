Система контроля продаж для кофейного магазина.

Схема базы данных:
Products содержит список всех наименованиях товара, которые продаются в этом магазине (их название и цену)
Purchases в этой таблице фиксируется информация о конкретной продаже
Work -- в этой таблице фиксируется фактическое время начала и окончания работы продавца

Схема не окончательная, не все таблицы, которые на ней есть, сейчас используются. Предполагаются изменения

Как это работает:

1) Пользователь выбирает свою роль: продавец или администратор
2) У продавца есть три функции: начать смену, продать, закончить смену.
3) Когда он выбирает "начать смену" в таблицу work записывается та фамилия, которую он ввёл и текущее время
4) Затем он может выбрать "продать" или "закончить смену"
5) Если он выбирает "продать", то необходимо внести название продукта и проданное количество. Тогда эта информация вместе с текущим временем запишется в таблицу Purchases. При этом продукт получиться добавить в таблицу Purchases только если он есть в таблице "Products", так как вставка происходит по id продукта
6) После каждой успешной продажи выводится сообщение о том, что продажа успешно проведена.
7) Дальше для проведения следующей покупки ему необходимо нажать "c", а для завершения смены "End".
8) Если он выбирает "End", то у него спрашивают фамилию и в таблицу "Work" в строчку с этой фамилией, где end_date ещё не заполнено записывается текущее время.
9) В случае успешного завершения выводится надпись, что смена закончена
10) Для роли администратора предполагается реализовать функции просмотра таблицы Purchases с филтрацией по продавцу, продукту и дате. Но данная функция ещё не до конца реализована
