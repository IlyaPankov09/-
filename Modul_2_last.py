first_field = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []
import random
n = random.choice(first_field)
print(n)
sum = 0
for i in range(1, n):
    # count = 0
    for j in range(i+1, n):
        sum = i + j
        if n % sum == 0:
            # count += 1
            result.append(f'{i}{j}')
print(''.join(result))


