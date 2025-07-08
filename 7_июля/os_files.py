import os

"""
Даёт доступ к системному функционалу
"""

# os.mkdir('libs') # создаёт исключение, если папка уже есть
os.makedirs('libs', exist_ok=True)  # теперь нет, "мягкое создание"

print(os.path.exists('libs'))
os.rmdir('libs')
print(os.path.exists('libs'))
if os.path.exists('libs'):
    os.rmdir('libs')

path = os.getcwd()  # get current working directory
print(path)
root = os.getcwd()

os.chdir(path + '/package_1')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
# os.chdir(os.getcwd() + '../docs')
# print(os.getcwd())

path = os.getcwd()
os.chdir(path + '../../images')
print(os.getcwd())
files = [f for f in os.listdir('.') if f.endswith('.jpg')]
print(files)
print([f for f in os.listdir('../docs') if f.startswith('R')])

os.chdir(root)
print(os.getcwd())
