class obgect_labn1(): # створюємо клас
    def __init__(self): # метод для отримання вхідних даних
        while True:
            try:
                self.nomer = int(input("Введіть номер залікової книжки: "))
                 # приймаємо значення a, b, n, m з клавіатури і записуємо в список
                self.tmin = list(map(lambda i: int(input(f"введіть цілочисельне {i}: ")), ["a", "b", "n", "m"]))
                if self.tmin[2] < self.tmin[0] or self.tmin[3] < self.tmin[1]: 
                    print("Не коректні дані")
                    continue
                self.c = [self.nomer % i for i in [2, 3, 5, 7]]
                break
            except:
                print("Не коректні дані")
    def funk_sum(self): # метод обчислення виразу
        s = 0
        for i in range(self.tmin[0], self.tmin[2] + 1):
            for j in range(self.tmin[1], self.tmin[3] + 1):
                if self.c[3] in range(4):
                    i, j = int(i), int(j)
                else:
                    i, j = float(i), float(j)
                if self.c[0] == 0: # шукаємо значення знаменника
                    thnam = i + self.c[1]
                else:
                    thnam = i - self.c[1]
                if thnam == 0: # перевіряємо чи знаменник не нуль
                    print("Ділити на нуль не можна")
                    break
                else:
                    # визначаємо вид операції 02 та обчислюємо значення виразу при конкретних i та j
                    if self.c[2] == 0: 
                        s += (i * j) / thnam
                    elif self.c[2] == 1:
                        s += (i / j) / thnam
                    elif self.c[2] == 2:
                        s += (i % j) / thnam
                    elif self.c[2] == 3:
                        s += (i + j) / thnam
                    elif self.c[2] == 4:
                        s += (i - j) / thnam
            else:
                continue
            break
        else:
            print(f"S = {s}")
go = obgect_labn1() # остворюємо об'єкт класу
go.funk_sum() # викликаємо метод обчислення виразу