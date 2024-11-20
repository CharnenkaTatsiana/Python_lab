#Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.

#m = int(input("Введите чисдо m:\n"))
#n = int(input("Введите чисдо n:\n"))
#p = int(input("Введите чисдо p:\n"))
#count = 0
#if (m < 0):
#   count += 1
#if (n < 0):
#   count += 1
#if (p < 0):
#   count += 1
#print(count)

#По введенному числу (от 0 до 7) напечатать название цифры.

#n = int(input("Введите число от 0 до 7"))
#if (n == 0):
#elif (n == 1):
#  print("Один")
#elif (n==2):
#  print("Два")
#elif (n == 3):
#   print("Три")
#elif (n == 4):
#   print("Четыре")
#elif (n == 5):
#   print("Пять")
#elif (n == 6):
#   print("Шесть")
#elif (n == 7):
#   print("Семь")

#8. Натуральное число, записанное в десятичной системе счисления, называется сверхпростым, если оно остается простым
#при любой перестановке своих цифр. Определить все сверхпростые числа до n.

#n = int(input("Введите число"))

#def is_prime(n):
#    k=2
#    while k*k<=n:
#        if n%k==0:
#            return False
#        k+=1
#    return True

#def rev_num(n):
#    r=0
#    while n>0:
#        r=r*10+n%10
#        n=n//10
#    return r

#for i in range(2,n):
#    if is_prime(i) and is_prime(rev_num(i)):
#        print(i)


#Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
#Размер списка n ввести с клавиатуры.
#	Найти номера минимального и максимального элементов первой половины списка.

# import random
#
# n = int(input("Введите размер списка \n"))
# A = []
# for i in range(n):
#    a = random.randint(0,99)
#    A.append(a)
# print(A)
# max = 0
# min = 0
# if(n % 2 != 0):
#    l = int(n/2+1)
# else:
#    l = int(n/2)
# for i in range(l):
#   if (A[i] < A[min]):
#      min = i
#   if (A[i] > A[max]):
#      max = i
#
# print(min)
# print(max)

