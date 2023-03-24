import random
N = int(input('Введите кол-во кустов: '))
i = 0

berries = [random.randint(0,100) for i in range(N)]
print(berries)
gether = int(input('Введите номер куста: '))-1
print('Собрано ',sum((berries[gether],berries[gether + 1]),berries[gether - 1]),'ягод.')