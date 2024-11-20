#items = [1, 2, 3, 4, 5]
#squared = list(map(lambda i: i**2, items))
#print(squared)


#from functools import reduce
#list = [1, 2, 3, 4]
#product = reduce(lambda x,product: x*product, list)
#print (product)


#x = [1, 2, 3]
#y = [4, 5, 6]
#result = list(zip(x,y))
#print(result)


# name_hero = [
#      'Hulk',
#     'Mr. Fantastic',
#     'Invisible Woman',
#     'Doctor Strange',
#     'Doctor Octopus',
#     'Spider-Man',
# ]
#
#
# name_real = [
#     'Bruce Banner',
#     'Reed Richards',
#     'Sue Storm',
#     'Stephen Strange',
#    'Otto Octavius',
#     'Peter Parker',
# ]
#
# res = list(zip(name_hero, name_real))
# print(res)


numbers = [1, 2, 4, 5, 7, 8, 10, 11]
r =list(filter(lambda a: a%2!= 0,numbers))
print(r)
