n = int(input('Введите число')) #условное число
h = (n % (60 * 24)) // 60 #часы
m = n % 60 #минуты
print('Прошло часов:', h); print('Прошло минут:', m)
input()
#При % мы берем остаток от деления, а при // целую часть от деления