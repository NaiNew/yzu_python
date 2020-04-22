text = 'r=10'
# 求圓面積
name, r = text.split('=')
r = int(r)  # str轉int
print('%s 為 %d 的圓面積是 %.2f' % (name, r, r*r*3.14))
