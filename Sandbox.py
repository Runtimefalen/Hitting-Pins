import random

"обработка выхода за массив"


def check_out_of_range(random_index, hit_power_count, param):
    if random_index + hit_power_count > param:
        return param - random_index
    else:
        return hit_power_count


try:
    kegels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    "значение стоящих кегель"

    hit_count = [1, 1, 1, 1]

    "игра - skittle кегля"
    for i in hit_count:
        summ_skittles_alive = kegels.count(1)
        if summ_skittles_alive == 0:
            summ_skittles_alive = summ_skittles_alive + 1
        hit_power_count = random.randint(1, summ_skittles_alive)
        random_index = random.randint(0, len(kegels) - 1)
        hit_power_count = check_out_of_range(random_index, hit_power_count, len(kegels))
        "удаление кегли"
        for i in range(hit_power_count):
            kegels[random_index] = 0
            random_index = random_index + 1

    if (kegels.count(1)) == 0:
        print("Strike!!!")
    print(kegels)

except Exception as e:
    print("Error", e)

