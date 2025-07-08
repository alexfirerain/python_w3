from os import path
# from pathlib import *

# __file__ - питоновская переменная с полным путём
# к исполняемому сейчас скрипту (т.е. корневой каталог программы)

img_dir = path.join(path.dirname(__file__), 'images')
font_dir = path.join(path.dirname(__file__), 'fonts')
print(img_dir)  # даже если путь не существует, просто мастерит правильную строку адреса
# так хорошо держать пути к компонентам программы
