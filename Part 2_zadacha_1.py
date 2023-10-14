start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))

sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0
sum_multiple_of_9 = 0
count_multiple_of_9 = 0

for num in range(start, end + 1):
    if num % 2 == 0:  
        sum_even += num
        count_even += 1
    else:  
        sum_odd += num
        count_odd += 1
    
    if num % 9 == 0:  
        sum_multiple_of_9 += num
        count_multiple_of_9 += 1

average_even = sum_even / count_even if count_even > 0 else 0
average_odd = sum_odd / count_odd if count_odd > 0 else 0
average_multiple_of_9 = sum_multiple_of_9 / count_multiple_of_9 if count_multiple_of_9 > 0 else 0

print("Сумма четных чисел:", sum_even)
print("Среднеарифметическое четных чисел:", average_even)

print("Сумма нечетных чисел:", sum_odd)
print("Среднеарифметическое нечетных чисел:", average_odd)

print("Сумма чисел, кратных 9:", sum_multiple_of_9)
print("Среднеарифметическое чисел, кратных 9:", average_multiple_of_9)