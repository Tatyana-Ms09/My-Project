count = 0

for number in range(100, 1000):
    digits = [int(digit) for digit in str(number)]  

    if len(set(digits)) < 3:
        count += 1

print("Количество чисел с двумя одинаковыми цифрами:", count)