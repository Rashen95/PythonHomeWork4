# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]

number = int(input('Введите натуральное число, а я выведу список простых множителей данного числа: '))
multipliers = []
for i in range(2, number//2):
    while number % i == 0:
        multipliers.append(i)
        number /= i
if len(multipliers) == 0:
    print(f'Число {number} является простым')
else:
    print(multipliers)
