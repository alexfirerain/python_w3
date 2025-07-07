# это есть публичная функция, обращаемся с любого места программы
def greet(name):
    return 'greeting you, ' + name

# скрытая функция (we're all consenting adults here)
# т.е. не принято лезть в скрытые функции, хоть они и доступны
def _hidden_function():
    return "ДСП"