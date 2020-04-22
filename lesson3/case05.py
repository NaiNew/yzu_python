def mask(money):
    x = money // 5
    size = '成人'
    return x, size
x, size = mask(300)
print(x, size)
