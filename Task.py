
cook_book = {}
solv_ihg_key = ['ingredient_name', 'quantity', 'measure']

with open('recipes.txt', encoding='utf-8') as c:
    dish = c.readline().strip()
    counter = int(c.readline().strip())

    ingrid_list = []
    for i in range(counter):
        ing = c.readline().strip().split('|')
        solv = dict(zip(solv_ihg_key, ing))
        ingrid_list.append(solv)

    cook_book[dish] = ingrid_list

    c.readline().strip()

    dish1 = c.readline().strip()
    counter1 = int(c.readline().strip())

    ingrid_list1 = []
    for i in range(counter1):
        ing1 = c.readline().strip().split('|')
        solv1 = dict(zip(solv_ihg_key, ing1))
        ingrid_list1.append(solv1)
    cook_book[dish1] = ingrid_list1

    c.readline().strip()

    dish2 = c.readline().strip()
    counter2 = int(c.readline().strip())

    ingrid_list2 = []
    for i in range(counter2):
        ing2 = c.readline().strip().split('|')
        solv2 = dict(zip(solv_ihg_key, ing2))
        ingrid_list2.append(solv2)
    cook_book[dish2] = ingrid_list2

    c.readline().strip()

    dish3 = c.readline().strip()
    counter3 = int(c.readline().strip())

    ingrid_list3 = []
    for i in range(counter3):
        ing3 = c.readline().strip().split('|')
        solv3 = dict(zip(solv_ihg_key, ing3))
        ingrid_list3.append(solv3)
    cook_book[dish3] = ingrid_list3


# print(cook_book) #Вывод 1-й задачи





def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                ingridient['quantity'] = int(ingridient['quantity']) * person_count
                abc = {ingridient['ingredient_name']: ingridient}
                del ingridient['ingredient_name']
                for ke in abc:        # Воспользовался материалом из лекции, что бы применить обработку исключений,
                   # но не ошибки (ключ в словаре перезаписывался бы с потерей значений и функция работала бы).
                   # Можно было пробовать по другому через Counter.
                    try:
                        shop_dict[ke]['quantity'] += abc[ke]['quantity']
                    except:
                        shop_dict[ke] = abc[ke]
    return print(shop_dict)




#get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1) # Вывод функции с повторяющимся ингридиентом
#get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2) # Вывод функции по заданию из примера