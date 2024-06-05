numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, 16):
    count = 0
    for j in (1, i + 1):
        if i % j == 0 and i != j and j != 1:
            count += 1
    if count == 0:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
#             is_prime = True
#             not_primes.append(i)
#         else:
#             primes.append(i)
# print(primes)
# print(not_primes)

    #     primes.append(i)
    # print(primes)
    #for j in range(2, j - 1):

        # if i == j and i % j != 0 and j / i == 1:
        #     break
        # primes.append(i)
        # if i % j != 0 and j / i != 1:
        #     break
        # print(primes)
        # print(not_primes.append(i))



    # for j in range(1, i//1+1):
    #     if (i % j == 0):
    #         primes.extend('i')
    #     continue
    # print(primes)



