# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию r​ange() ​и генератор.	Подсказка: использовать функцию r​ange() ​и генератор.

print([
    x for x in range(20, 240)
    if x % 20 == 0 or x % 21 == 0
])