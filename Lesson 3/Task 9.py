n = int(input("Долек по X: "))
m = int(input("Долек по Y: "))
print("Размер шоколадки: ",n,"x",m,"долек, всего долек:", n*m)
k = int(input("Часть должна содержать долек: "))
if n*m > k:   #Часть не может содержать долек столько же, сколько целая!
    if k%n == 0 or k%m == 0:
        print("Да, можно")
    else:
        print("Нет, не может!")
else:
    print("Нет, нельзя!")

