# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными.
# Степени многочленов могут отличаться.

first = open('polynomial1.txt', 'r')
second = open('polynomial2.txt', 'r')
file1 = first.read()
file2 = second.read()
print(file1)
print(file2)
lst1 = file1.split(' ')
print(lst1)
lst2 = file2.split(' ')
print(lst2)
for i in lst1:
    if i == '*':
        lst1.remove(i)
for i in lst2:
    if i == '*':
        lst2.remove(i)
print(lst1)
print(lst2)
for i in range(len(lst2)):
    if lst2[i] == '-' and lst2[i + 1][0].isdigit():
        lst2[i + 1] = lst2[i] + lst2[i + 1]
    elif lst2[i] == '-':
        lst2[i] = '-1'
for i in lst2:
    if i == '-' or i == '+':
        lst2.remove(i)
for i in range(len(lst1)):
    if lst1[i] == '-' and lst1[i + 1][0].isdigit():
        lst1[i + 1] = lst1[i] + lst1[i + 1]
    elif lst1[i] == '-':
        lst1[i] = '-1'
for i in lst1:
    if i == '-' or i == '+':
        lst1.remove(i)
print(lst1)
print(lst2)
if lst1[0][0] == '-' or lst1[0].isdigit():
    if lst1[1] == 'x':
        senior_degree1 = 1
    else:
        senior_degree1 = lst1[1][2:]
else:
    if lst1[0] == 'x':
        senior_degree1 = 1
    else:
        senior_degree1 = lst1[0][2:]
if lst2[0][0] == '-' or lst2[0].isdigit():
    if lst2[1] == 'x':
        senior_degree2 = 1
    else:
        senior_degree2 = lst2[1][2:]
else:
    if lst2[0] == 'x':
        senior_degree2 = 1
    else:
        senior_degree2 = lst2[0][2:]
if int(senior_degree1) > int(senior_degree2):
    senior_degree = int(senior_degree1)
else:
    senior_degree = int(senior_degree2)
print(f'Старшая степень = {senior_degree}')
lst3 = []
number1 = 0
number2 = 0
for i in range(senior_degree+1):
    if senior_degree > 1:
        if lst1.count(f"x^{senior_degree}") and lst2.count(f"x^{senior_degree}"):
            for j in range(len(lst1)):
                if lst1[j] == f"x^{senior_degree}":
                    if j == 0:
                        number1 = 1
                    elif lst1[j - 1][0] == '-' or lst1[j - 1].isdigit():
                        number1 = int(lst1[j - 1])
                    else:
                        number1 = 1
            for k in range(len(lst2)):
                if lst2[k] == f"x^{senior_degree}":
                    if k == 0:
                        number2 = 1
                    elif lst2[k - 1][0] == '-' or lst2[k - 1].isdigit():
                        number2 = int(lst2[k - 1])
                    else:
                        number2 = 1
        else:
            if lst1.count(f"x^{senior_degree}"):
                for j in range(len(lst1)):
                    if lst1[j] == f"x^{senior_degree}":
                        if j == 0:
                            number1 = 1
                        elif lst1[j - 1][0] == '-' or lst1[j - 1].isdigit():
                            number1 = int(lst1[j - 1])
                        else:
                            number1 = 1
            else:
                for j in range(len(lst2)):
                    if lst2[j] == f"x^{senior_degree}":
                        if j == 0:
                            number1 = 1
                        elif lst2[j - 1][0] == '-' or lst2[j - 1].isdigit():
                            number1 = int(lst2[j - 1])
                        else:
                            number1 = 1
        lst3.append(f'{number1 + number2}' + f'x^{senior_degree}')
        senior_degree -= 1
    elif senior_degree == 1:
        if lst1.count("x") and lst2.count(f"x"):
            for j in range(len(lst1)):
                if lst1[j] == "x":
                    if j == 0:
                        number1 = 1
                    elif lst1[j - 1][0] == '-' or lst1[j - 1].isdigit():
                        number1 = int(lst1[j - 1])
                    else:
                        number1 = 1
            for k in range(len(lst2)):
                if lst2[k] == "x":
                    if k == 0:
                        number2 = 1
                    elif lst2[k - 1][0] == '-' or lst2[k - 1].isdigit():
                        number2 = int(lst2[k - 1])
                    else:
                        number2 = 1
        else:
            if lst1.count("x"):
                for j in range(len(lst1)):
                    if lst1[j] == "x":
                        if j == 0:
                            number1 = 1
                        elif lst1[j - 1][0] == '-' or lst1[j - 1].isdigit():
                            number1 = int(lst1[j - 1])
                        else:
                            number1 = 1
            else:
                for j in range(len(lst2)):
                    if lst2[j] == "x":
                        if j == 0:
                            number1 = 1
                        elif lst2[j - 1][0] == '-' or lst2[j - 1].isdigit():
                            number1 = int(lst2[j - 1])
                        else:
                            number1 = 1
        lst3.append(f'{number1 + number2}' + 'x')
        senior_degree -= 1
    else:
        if lst1[len(lst1)-1][0] == '-' or lst1[len(lst1)-1].isdigit():
            number1 = int(lst1[len(lst1)-1])
        if lst2[len(lst2) - 1][0] == '-' or lst2[len(lst2) - 1].isdigit():
            number2 = int(lst2[len(lst2) - 1])
        lst3.append(f'{number1 + number2}')
    number1 = 0
    number2 = 0
print(lst3)
result = open('result.txt', 'w')
for i in range(len(lst3)):
    if lst3[i][0] == '0':
        continue
    if i == 0:
        result.write(lst3[i])
    elif lst3[i][0].isdigit():
        result.write(f"+{lst3[i]}")
    else:
        result.write(str(lst3[i]))
print('Я вывел сумму многочленов из файлов polynomial1.txt и polynomial2.txt в файл result.txt')
