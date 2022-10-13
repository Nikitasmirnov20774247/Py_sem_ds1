# Задача 2. Напишите программу для, проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x y z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print (x, y, z, (not (x or y or z) == (not x and not y and not z)))

a = not (x or y or z)
b = not x and not y and not z

if a == b:
    result = a == b

if result == True:
    print('Данное утверждение истинно')
else:
    print('Данное утверждение ложно')