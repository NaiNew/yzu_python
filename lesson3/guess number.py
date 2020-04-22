import random as r
ans = r.randint(1, 99)
min = 0
max = 100
count = 7

while count > 0:
    guess = int(input('(%d次)請輸入數字 %d ~ %d :' % (count, min, max)))
    count -= 1
    if guess <= min or guess >= max:
        print('請重新輸入')
        continue
    if guess == ans:
        print('恭喜')
        break
    elif guess < ans:
        min = guess
    else:
        max = guess
