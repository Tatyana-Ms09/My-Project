start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

print("Простые числа в диапазоне от", start, "до", end, "включительно:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)
