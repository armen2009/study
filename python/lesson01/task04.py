# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

a = int(input("Введите целое положительное число "))
maximum = a % 10

while a >= 1:
    a = a // 10
    if a % 10 > maximum:
        maximum = a % 10
    if a > 9:
        continue
    else:
        print("Максимальное цифра в числе ", maximum)
        break
