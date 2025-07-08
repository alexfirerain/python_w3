res = []
with open('files/numbers.txt') as source:
    while temp := source.readline().rstrip('\n'):
        # if temp:  # ?
        res += temp.split(', ')
    res = sorted(int(x) for x in (set(res)))  # любую коллекцию `.sorted()` переводит в сортированный список
print(res)

# Д/з сделать эту программу устойчивой к пустой строке

"""
НЕ ПАНИКУЙ
"""

