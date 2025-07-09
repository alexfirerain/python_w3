import re, requests

pattern = r'<img[^>]+src="([^">]+)"'    # r'<img[^>]+src="([^">]+)"'
img_str = '<img height="50" width="150" src= "images/bg.jpg">'  # "Картинка <img src="bg.jpg"> в тексте</p>"

print(re.findall(pattern, img_str))

"""
как вообще работает система версионирования?
версия.функционал.ревизия

в новый PyCharm встроен жёсткий Линтерн
любой сервер по идее знает Пых
и должен быть Пайтон-Шел, чтоб на Питоне шёл
CMS ВордПресс написан на ПХП
"""

"""
как прочитать сайт?
"""
html = requests.get('http://skillbox.ru').text
# print(html)
print(re.findall(pattern, html))