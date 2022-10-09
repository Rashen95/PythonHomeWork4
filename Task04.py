# Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите значение степени, а я выведу многочлен данной степени в файл "text.txt": '))
polynomial = []
coefficient = random.randrange(1, 101)
if coefficient == 1:
    polynomial.append(f'x^{k}')
else:
    polynomial.append(f'{coefficient}*x^{k}')
k -= 1
while k >= 0:
    if k > 1:
        coefficient = random.randrange(0, 101)
        if coefficient == 0:
            continue
        elif coefficient == 1:
            polynomial.append(f'x^{k}')
        else:
            polynomial.append(f'{coefficient}*x^{k}')
    elif k == 1:
        coefficient = random.randrange(0, 101)
        if coefficient == 0:
            continue
        else:
            polynomial.append(f'{coefficient}*x')
    else:
        coefficient = random.randrange(0, 101)
        if coefficient == 0:
            continue
        else:
            polynomial.append(coefficient)
    k -= 1
print(polynomial)
f = open('text.txt', 'w')
for i in range(len(polynomial)):
    if i == len(polynomial)-1:
        f.write(f'{polynomial[i]} = 0')
    else:
        f.write(f'{polynomial[i]} + ')
f.close()
