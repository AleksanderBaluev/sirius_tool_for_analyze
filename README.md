Для чего создан данный инструмент:
Данный инструмент сделан для анализа клиентских отзывов компании Тинькофф.

Шаги работы инструмента:
1. Парсинг отзывов с откртых источников.
2. Морфологический и Синтаксичиский анализ.
3. Перевод отзывов в векторы.
4. Распределение отзывов по категориям с помощью ML.

файл Additionaltask.ipynb является парсером, который производит сбор отзывов с сайтов Brobank,otzovik.

файл all_otzovi.txt содержит все отзовы, собранные парсером.

файл Prototype.ipynb используется для морфологического и синтаксического анализа отзывов, перевод отзывов в векторы и распределяет отзывы по категориям.
