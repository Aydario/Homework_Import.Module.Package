# Домашнее задание к лекции 1. «Import. Module. Package»
1. Разработана **структура** программы «Бухгалтерия»:- main.py;  - application/salary.py;  - application/db/people.py.
main.py — основной модуль для запуска программы. В модуле salary.py функция calculate_salary. В модуле people.py функция get_employees.  
2. Импортированы функции в модуль main.py и вызваны эти функции в конструкции.```if __name__ == '__main__':```**Сами функции не реализовываны**. В каждую добавлен вывод с помошью **print()**
3. При вызове функций модуля main.py выводится текущая дата.
4. Найден интересный [пакет](https://pypi.org/project/colorlibx/) на pypi, добавлен в файл requirements.txt и указана его актуальная версия. 
5. Создан рядом с файлом main.py модуль dirty_main.py и импортированы в него все функции с помощью конструкции (необязательное задание).```from package.module import *``` 