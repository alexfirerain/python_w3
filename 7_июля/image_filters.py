from PIL import Image, ImageFilter, ImageEnhance

orig = Image.open('../images/harry_python.jpg')
# вообще на всякий случай перед использованием фильтров лучше конвертнуть

# РАЗМЫТИЕ
# blurred = orig.filter(ImageFilter.GaussianBlur(radius=3))
# blurred.show()

# УСИЛЕНИЕ РЕЗКОСТИ
# enhanced = ImageEnhance.Sharpness(orig)
# sharpened = enhanced.enhance(4.0)
# sharpened.show()

# ПОЛУЧИТЬ КОНТУРЫ
edges = orig.filter(ImageFilter.FIND_EDGES)
edges.show()

