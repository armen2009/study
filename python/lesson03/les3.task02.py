#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. 
# Реализовать вывод данных о пользователе одной строкой.
def main(first_name: str = None,
         last_name: str = None,
         year: int = None,
         city: str = None,
         phone: str = None,
         email: str = None):
    return f" Имя = {first_name}, Фамилия = {last_name}, Год рождения = {year}, Город проживания = {city}, Email = {email}, Номер телефона = {phone}"

user_first_name = input("Имя >>> ")
user_last_name = input("Фамилия >>> ")
user_year = int(input("Год рождения >>> "))
user_city = input("Город проживания >>> ")
user_email = input("Email >>> ")
user_phone = input("Номер телефона >>> ")

print("Мета информация о пользователе:", 
    main(first_name=user_first_name, last_name=user_last_name,
         year=user_year, city=user_city, email=user_email,
         phone=user_phone)
)