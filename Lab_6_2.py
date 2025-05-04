class TribonacciIterator:
    def __init__(self, limit):
        self.limit = limit  # Количество чисел для генерации
        self.a, self.b, self.c = 0, 0, 1  # Первые три числа
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        if self.count == 0:
            result = self.a
        elif self.count == 1:
            result = self.b
        elif self.count == 2:
            result = self.c
        else:
            self.a, self.b, self.c = self.b, self.c, self.a + self.b + self.c
            result = self.c
        self.count += 1
        return result


# Создаем итерируемый объект для 35 чисел
tribonacci_sequence = TribonacciIterator(35)

# Выводим числа
for num in tribonacci_sequence:
    print(num, end=" ")