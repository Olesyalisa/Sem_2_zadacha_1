#Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.

num = int(input('number N = '))

lst = [round((1 + (1/i))**i, 2) for i in range(1, num+1)]
print(f'{lst}\n {round(sum(lst))}')