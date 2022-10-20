# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

a = [1.45, 2.14, 7.83, 4.5, 8.18, 9.25]
for i in range(0,len(a)):
    a[i] = a[i] - int(a[i])

for i in range(0,len(a)-1):
    if a[i] > a[i+1]:
        maximum = a[i]
        a[i], a[i+1] = a[i+1],a[i]  
    else:
        maximum = a[i+1]

for i in range(0,len(a)-1):
    if a[i] < a[i+1]:
        minimum = a[i]
        a[i], a[i+1] = a[i+1],a[i]
    else:
        minimum = a[i+1]        

sum = maximum - minimum

print(sum)