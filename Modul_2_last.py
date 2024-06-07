first_field = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []
import random
def number():                         #функция выбирает случайное число из первого поля
    n = random.choice(first_field)
    return n
print(number())
sum = 0
for i in range(1, 21):
    for j in range(1, 21):
        sum = i + j
        #print(sum)    #вроде складывает
        if i  + j == number and number % sum == 0:
            result.append(i)
            continue
print(result)


