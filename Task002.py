#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):                                                               # бежим от нуля до еденицы. 
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))          #¬ это "нет" ⋁ - это "или" ⋀ это "И"
                print(x, y, z)

