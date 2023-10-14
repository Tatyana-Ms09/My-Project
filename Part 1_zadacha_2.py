start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))

print("Все числа в диапазоне:")
for num in range(start, end + 1):
    print(num, end=" ")

print("\nВсе числа в убывающем порядке:")
for num in range(end, start - 1, -1):
    print(num, end=" ")

print("\nЧисла, кратные 7:")
for num in range(start, end + 1):
    if num % 7 == 0:
        print(num, end=" ")

count = 0
for num in range(start, end + 1):
    if num % 5 == 0:
        count += 1

print("\nКоличество чисел, кратных 5:", count)