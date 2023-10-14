count = 0

for number in range(100, 10000):
    digits = [int(digit) for digit in str(number)]  
    if len(set(digits)) == len(digits):
        count += 1

print("Количество чисел с разными цифрами:", count)