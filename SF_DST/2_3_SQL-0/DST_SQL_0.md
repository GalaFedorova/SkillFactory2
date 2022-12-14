# ВИДЫ ОПЕРАТОРОВ SQL

Операторы SQL делятся на:

* операторы определения данных (Data Definition Language, DDL) — с их помощью создаются 
и изменяются объекты в БД (сама БД, таблицы, функции, процедуры, пользователи и т. д.);
* операторы манипуляции данными (Data Manipulation Language, DML) — с их помощью проводятся манипуляции с данными в таблицах;
* операторы определения доступа к данным (Data Control Language, DCL) — с их помощью, как следует из названия, 
создаются и изменяются разрешения на определённые операции с объектами в БД;
* операторы управления транзакциями (Transaction Control Language, TCL) — 
с их помощью осуществляется комплекс определённых действий, причём так, что либо все эти действия выполняются успешно, либо ни одно из них не выполняется вообще.

Мы будем изучать только DML-операторы (для манипуляций с данными), а конкретнее — оператор SELECT, который позволяет выбрать из БД интересующие нас данные

Для написания запросов к БД необходим специальный инструмент. Это может быть терминал в ОС, специализированная программа 
(например, одна из распространённых — DataGrip) или веб-сервис. 
Именно такой веб-сервис мы будем использовать.

Metabase — это бесплатный и удобный инструмент для первичного анализа данных с возможностью передавать запросы

http://sql.skillfactory.ru:3000/auth/login?redirect=%2F



Обратите внимание! 
Если в алиасе используется кириллица или пробелы, необходимо заключать его в двойные кавычки: 10 - rating AS "разница" или movie_title AS "Movie Title".

Важно! Если и числитель, и знаменатель — целые числа, результат деления также будет целочисленным, то есть этот оператор произведёт деление нацело.

Важно! NULL — это специальное значение. 
Если вы фильтруете столбец, в котором есть пустые значения, по любому условию, кроме IS NULL / IS NOT NULL, такие значения будут исключены из вывода.

ASC — явное указание порядка сортировки по возрастанию (англ. ascending).
Для обратного порядка используется ключевое слово DESC (англ. descending).

Обратите внимание! Ключевое слово ORDER BY идёт после применения всех условий в WHERE.

Также в ORDER BY можно указывать, где должны идти пустые значения — в начале или в конце. 
Такая настройка порядка вывода задаётся с помощью ключевых слов NULLS FIRST / NULLS LAST.

Если LIMIT «оставляет» указанное число первых строк из вывода, то OFFSET, наоборот, «обрезает» указанное число первых строк.

LIMIT и OFFSET можно использовать вместе, их порядок не важен.


Чтобы получить уникальные значения из столбца, воспользуемся ключевым словом DISTINCT. сразу после select 

COUNT считает строки, а звёздочка (*) в аргументе функции означает, что считаются все строки, которые возвращает запрос.

Если в аргументе функции указать название столбца, функция обработает только строки с непустым значением.

Внутри функции COUNT мы можем также применять DISTINCT, чтобы вычислить количество уникальных значений.
SELECT
    COUNT(DISTINCT type1)
FROM sql.pokemon

* COUNT — вычисляет число непустых строк;
* SUM — вычисляет сумму;
* AVG — вычисляет среднее;
* MAX — вычисляет максимум;
* MIN — вычисляет минимум.
