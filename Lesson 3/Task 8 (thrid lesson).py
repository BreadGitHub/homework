a = int(input('Введите первое число:'))
b = int(input('Введите второе число:')) #По условию даны целые числа
c = int(input('Введите третье число:'))
if a == b == c:
    print('Совпадают все 3 числа')
else:
    if  a == b or a == c or b == c:
        print('Совпадают только 2 числа')
    else:
        print('Ни одно число не совпадает')

