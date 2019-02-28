import os


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"


def instruction():
    """ Отображает возможности программы и показывает как ей пользоваться """
    print("""""
             В данной программе вы можете управлять вашей операционной системой!

             [1] - Перейти в указанную папку
             [2] - Посмотреть содержимое текущей папки
             [3] - Создать папку
             [4] - Удалить папку
             [5] - Выйти из программы

             """"")


def path():
    """Задает текущий путь"""
    current_path = os.getcwd()
    return current_path


def goto_dir(current_path, dir_name):
    new_path = os.path.join(current_path, dir_name)
    os.chdir(new_path)


def dir_content():
    """Выводит список файлов в текущей директории"""
    content = os.listdir()
    if len(content) > 0:
        print(f"Список файлов в текущей папке:\n{content}")
    else:
        print("\nПапка пуста!")


def create_dir(current_path, dir_name):
    """Создает папку в текущей директории"""
    new_dir = os.path.join(current_path, dir_name)
    os.mkdir(new_dir)


def delete_dir(current_path, dir_name):
    """Удаляет папку в текущей директории"""
    dir_to_delete = os.path.join(current_path, dir_name)
    os.rmdir(dir_to_delete)


current_path = path()  # задаем путь, в котором находимся в данный момент
while True:
    instruction()  # выводим инструкцию

    choice = int(input("\nВыберите действие: "))
    while choice not in range(1, 6):
        choice = int(input("\nВыберите действие: "))

    if choice == 1:
        name_dir = input("Введите имя папки: ")
        try:
            goto_dir(current_path, name_dir)
            current_path = path()  # изменяем путь
        except FileNotFoundError:
            print("\nПапки с таким именем не существует")

    elif choice == 2:
        dir_content()

    elif choice == 3:
        name_dir = input("Введите имя новой папки: ")
        try:
            create_dir(current_path, name_dir)
            print("Новая папка успешно создана!")
        except FileExistsError:
            print("Папка с таким именем уже существует")

    elif choice == 4:
        name_dir = input("\nВведите имя папки: ")
        try:
            delete_dir(current_path, name_dir)
            print("Папка успешно удалена!")
        except FileNotFoundError:
            print("Папки с таким именем не существует")
        except OSError:
            print("Невозможно удалить папку, т.к она не пустая")

    elif choice == 5:
        print("\n\t\t\tДо свидания!")
        break
