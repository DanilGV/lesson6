my_dict = {'Andrey': 2000, 'Artem' :1995, 'Ivan' :1991}
print(my_dict )
print(my_dict ['Artem'])
print(my_dict.get('Max'))

my_dict.update({'Masha' : 2003 ,
                'Olya' : 1997})
#Не понял как удалить ключ чтобы потом он вывел значение
a = my_dict.pop('Ivan')
print(a)
print(my_dict )

my_set = {1 , 1 , 1,  'World' , 'World' , float , float}
print(my_set)
my_set.add('sun')
my_set.add(6)
my_set.discard(1)
print(my_set)