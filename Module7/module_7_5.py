# Файлы в операционной системе

# Цель задания:
#
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime,
# os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.
#
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.
#
# Комментарии к заданию:
#
# Ключевая идея – использование вложенного for
#
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,
#     Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
#
#
#
# Так как в разных операционных системах разная схема расположения папок,
# тестировать проще всего в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт,
# Время изменения: 11.11.1111 11:11, Родительская директория.


from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime


from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime


def show_path_info(directory):
    '''выводит информацию о всех файлах в указанной директории'''
    for root, dirs, files in walk(directory):
        for file in files:
            filepath = join(root, file)
            filetime = getmtime(filepath)
            formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))
            filesize = getsize(filepath)
            parent_dir = dirname(filepath)
            # parent_dir = root  # то же самое
            print(f'Обнаружен файл: {file},',
                  f'Путь: {filepath},',
                  f'Размер: {filesize} байт,',
                  f'Время изменения: {formatted_time},',
                  f'Родительская директория: {parent_dir}')


if __name__ == '__main__':
    show_path_info('.')