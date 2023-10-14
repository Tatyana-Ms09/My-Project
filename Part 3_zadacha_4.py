number = int(input("Введите целое число: "))

number_str = str(number)

filtered_str = ''.join(char for char in number_str if char not in '36')

filtered_number = int(filtered_str)

print("Число после удаления цифр 3 и 6:", filtered_number)
