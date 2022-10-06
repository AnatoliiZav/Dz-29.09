# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

a = [1, 2, 7, 4, 8, 9]
result_str = []

my_len=len(a)
for i in range(0, my_len//2):
    a[i] = a[i]*a[my_len-1]
    my_len -=1
    result_str.append(a[i])
print(result_str)