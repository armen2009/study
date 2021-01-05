#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating = [1,2]

while True:
    try:
        print(f"Рейтинг = {rating}")
        user_rating = int(input("Введите новый рейтинг >>> "))
        current_rating_count = rating.count(user_rating)

        if current_rating_count:
            last_current_index = rating.index(user_rating) + current_rating_count
            rating.insert(last_current_index, user_rating)
        else:
            if user_rating > rating[0]:
                rating.insert(0, user_rating)
            elif user_rating < rating[-1]:
                rating.append(user_rating)
            else:
                for index, rating in enumerate(rating):
                    if rating < user_rating:
                        rating.insert(index, user_rating)
                        break

        print(rating)
    except ValueError:
        print("Неверное число")
    except KeyboardInterrupt:
        exit()