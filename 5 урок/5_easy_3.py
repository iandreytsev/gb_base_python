import os
import sys
import shutil

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


file_name = os.path.basename(sys.argv[0])  # выводим имя файла, из которого запущен скрипт.
dupl_file = file_name[:-3] + ".dupl.py"  # срезаем окончание с форматом файла и присваиваем новое.
shutil.copy(file_name, dupl_file)  # копируем файл

print("\nФайл успешно скопирован")
