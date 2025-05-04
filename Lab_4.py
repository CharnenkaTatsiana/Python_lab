import random
import datetime
# import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a


def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)


def InsertSort(A):
    # Цикл 1 – по i от 1 до (len(A))
    for i in range(1, len(A)):
        # Сохранение A[i] (вставляемый элемент)
        t = A[i]
        # Новая переменная j (позиция в отсортированной части)
        j = i
        # Цикл 2 – по j до 0 и A[j-1] > t
        while j > 0 and A[j-1] > t:
            # Сдвигаем элемент вправо
            A[j] = A[j-1]
            # Уменьшаем j
            j -= 1
        # Вставляем сохраненный элемент на нужное место
        A[j] = t
    

def ShakerSort(A):
    N = len(A)
    # Цикл 1 – по i от 0 до N/2 (счетчик пар проходов)
    for i in range(0, N // 2):
        # Цикл 2 – проход слева направо (j от i до N-1-i)
        for j in range(i, N - 1 - i):
            # Если текущий элемент больше следующего, меняем их местами
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
        
        # Цикл 3 – проход справа налево (j от N-2-i до i+1)
        for j in range(N - 2 - i, i, -1):
            # Если текущий элемент меньше предыдущего, меняем их местами
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
   

# table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой"])
x=[]
y1=[]
y2=[]
y3=[]
y4=[]



for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    C = A.copy()
    D = A.copy() 
    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)



    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    InsertSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Сортировка вставками   " +str(N)+"   заняла   "+str((t6-t5).total_seconds()) + "c")


    t7 = datetime.datetime.now()
    ShakerSort(D)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Шейкерная   " +str(N)+"   заняла   "+str((t8-t7).total_seconds()) + "c")


    # table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
# print(table)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Сравнение времени сортировок", fontdict = font1)
plt.xlabel("Размер массива", fontdict = font2)
plt.ylabel("Время (секунды)", fontdict = font2)


plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.plot(x, y4, "C3")

plt.show()



# --- 1. Точечный график (Scatter Plot) ---

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Сравнение времени сортировок", fontdict = font1)
plt.xlabel("Размер массива", fontdict = font2)
plt.ylabel("Время (секунды)", fontdict = font2)
plt.grid(True, linestyle='--', alpha=0.6)

plt.scatter(x, y1, color='C0')
plt.scatter(x, y2, color='C1')
plt.scatter(x, y3, color='C2')
plt.scatter(x, y4, color='C3')

plt.show()

# --- 2. Столбчатая диаграмма (Bar Plot) ---
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Сравнение времени сортировок", fontdict = font1)
plt.xlabel("Размер массива", fontdict = font2)
plt.ylabel("Время (секунды)", fontdict = font2)
plt.grid(True, linestyle='--', alpha=0.6)

bar_width = 100
plt.bar([n - 1.5*bar_width for n in x], y1, width=bar_width, label='Пузырьковая', color='C0')
plt.bar([n - 0.5*bar_width for n in x], y2, width=bar_width, label='Быстрая', color='C1')
plt.bar([n + 0.5*bar_width for n in x], y3, width=bar_width, label='Вставками', color='C2')
plt.bar([n + 1.5*bar_width for n in x], y4, width=bar_width, label='Шейкерная', color='C3')

plt.show()

# --- 2. Отдельные графики (Sub Plot) ---

plt.subplot(2, 2, 1)
plt.plot(x, y1, "C0")

plt.subplot(2, 2, 2)
plt.plot(x, y2, "C1")

plt.subplot(2, 2, 3)
plt.plot(x, y3, "C2")

plt.subplot(2, 2, 4)
plt.plot(x, y4, "C3")

plt.show()
