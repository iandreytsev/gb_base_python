# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

import os
import sys
import shutil

print("Путь = ", sys.argv)


def print_help():
    print("""""

        help - получение справки
        mkdir <dir_name> - создание директории
        cp <file_name> - создает копию указанного файла
        rm <file_name> - удаляет указанный файл
        cd <new path> - меняет текущею директорию на указанную
        sp - отображение полного пути текущей директории
        dp - удаляет папку в текущей директории
        ping - тестовый ключ
         

        """"")


def ask_yes_no(question):
    """Задает пользователю вопрос, пока он не ответит 'Да' или 'Нет'"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def make_dir():
    """Создает новую директорию"""
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return

    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f"Директория '{dir_name}' создана")
    except FileExistsError:
        print(f"директория '{dir_name}'уже существует")


def ping():
    """Служит тестовой командой"""
    print("pong")


def copy_file():
    """Копирует указанный файл"""
    if not file_name:
        print("Необходимо ввести имя файла вторым параметром")
        return
    dupl_file = "Copy of_" + file_name
    try:
        shutil.copy(file_name, dupl_file)
        print(f"Файл '{file_name}' успешно скопирован")
    except FileNotFoundError:
        print(f"Файла '{file_name}' не существует")


def remove_file():
    """Удаляет указанный файл"""
    if not file_name:
        print("Необходимо ввести имя файла вторым параметром")
        return
    try:
        check = ask_yes_no("Вы уверены?(Y/N) ")
        if check == "y":
            os.remove(file_name)
            print(f"Файл '{file_name}' успешно удален")
        else:
            print("Хорошо, пока оставлю")
    except FileNotFoundError:
        print(f"Файла '{file_name}' не существует")


def change_dir():
    """Менят текущую директорию на заданную"""
    new_path = os.path.join(os.getcwd(), path)
    if not path:
        print("Укажите директорию вторым параметром")
        return
    try:
        os.chdir(new_path)
        print("Смена директории прошла успешно!")
    except FileNotFoundError:
        print("Такой директории не существует")


def show_path():
    """Отображает текущую директорию"""
    print(os.getcwd())


def remove_dir():
    """Удаляет папку в текущей директории"""
    if not file_name:
        print("Укажите имя папки вторым аргументом. Убедитесь,что она пустая!")
    try:
        os.rmdir(file_name)
        print(f"Папка '{file_name}' успешно удалена!")
    except FileNotFoundError:
        print(f"Папки с именем '{file_name}' не существует")
    except OSError:
        print(f"Невозможно удалить папку '{file_name}', т.к она не пустая")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": remove_file,
    "rd": remove_dir,
    "cd": change_dir,
    "sp": show_path,
    "ping": ping
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    path = sys.argv[2]
except IndexError:
    path = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
