# -*- coding:UTF-8 -*-
# BMI 資料運算
h = float(input('請輸入身高'))
w = float(input('請輸入體重'))
BMI = w/ (h/100)**2
result = 18<= BMI <23
print('身高: %.1f 體重: %.1f BMI: %.2f result: %s'%
      (h, w, BMI, result))



