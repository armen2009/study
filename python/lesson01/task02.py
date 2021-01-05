# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input("Введите время в секундах:"))
hours = time_in_seconds // 3600
minutes = (time_in_seconds - hours * 3600) // 60
seconds = time_in_seconds % 60
print("Результат в формате (чч:мм:сс): ", f"{hours}:{minutes}:{seconds}")