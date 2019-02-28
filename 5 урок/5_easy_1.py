import os


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def instruction():
    """ Отображает возможности программы и показывает как ей пользоваться """
    print("""""
         В данной программе вы можете управлять вашей операционной системой!
         
         [1] - Создать заданное колличество папок в текущей директории
         [2] - Удалить созданные папки в текущей директории
         
         """"")


def create_dir(number_dir):
    for i in range(1, number_dir + 1):
        dir_path = os.path.join(os.getcwd(), "Новая папка " + str(i))
        try:
            os.mkdir(dir_path)
            print("Папка успешно создана!")
        except FileExistsError:
            print("Такие папки уже существуют")


def delete_dir(number_dir):
    for i in range(1, number_dir + 1):
        dir_path = os.path.join(os.getcwd(), "Новая папка " + str(i))
        try:
            os.rmdir(dir_path)
            print("Папки успешно удалены")
        except FileNotFoundError:
            print("Такой папки не существует")


instruction()
answer = input("Выберите дейстие: ")

if answer == "1":
    number = int(input("Сколько папок хотите создать? "))
    create_dir(number)


elif answer == "2":
    number = int(input("Сколько папок хотите удалить? "))
    delete_dir(number)

else:
    print("Неизвестный выбор")
