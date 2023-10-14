total = 0
maximum = float('-inf')
minimum = float('inf')

while True:
    number = input("Введите число (или 7 для завершения): ")
    
    if number == '7':
        print("Good bye!")
        break
    
    number = float(number)
    
    total += number
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

if total != 0:
    print("Сумма введенных чисел:", total)
    print("Максимум:", maximum)
    print("Минимум:", minimum)
else:
    print("Вы не ввели ни одного числа.")