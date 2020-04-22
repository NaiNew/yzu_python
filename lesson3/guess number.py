import random as r
ans = r.randint(1, 99)
min = 0
max = 100

while True:
    guess = int(input('請輸入數字 %d ~ %d :' % (min, max)))
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
