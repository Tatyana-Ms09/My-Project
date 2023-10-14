start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))

for i in range(start, end + 1):
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}", end="\t")
    print() 