first = int(input("Введите первое число, "))
second = int(input("Введите второе число, "))
third = int(input("Введите третье число, "))
if first == second and first == third:
    print (3)
elif first != second and first != third:
    print (0)
elif first == third or first == second:
    print (2)
