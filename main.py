order = ['Фахитос', 'Омлет']
count = 2
def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients_count = int(file.readline())
            ingredients = []
            for ing in range(ingredients_count):
                ingredient = file.readline().strip()
                name, quan, meas = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': quan,
                    'measure': meas
                })
            file.readline()
            cook_book[dish_name] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingr in get_cook_book()[dish]:
            if ingr['ingredient_name'] in shop_list.keys():
                shop_list[ingr['ingredient_name']]['quantity'] = \
                    int(shop_list[ingr['ingredient_name']]['quantity']) + int(ingr['quantity']) * person_count
                # print(shop_list)
            else:
                shop_list[ingr['ingredient_name']] = {
                    'measure': ingr['measure'],
                    'quantity': int(ingr['quantity']) * person_count
                }

    return shop_list


print(get_shop_list_by_dishes(order, count))


def files_sort():
    import os
    file_list = []
    for f in os.listdir('sorted'):
        with open('sorted' + '/' + f, encoding='utf8') as files:
            lines = files.read().splitlines()
            file_list.append([f, len(lines)])
            file_list[len(file_list)-1] += lines
    file_list.sort(key=len)
    return file_list


def file_create():
    import os
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in files_sort():
            for elem in file:
                f.write(f'{elem}\n')
    file_path = os.path.join(os.getcwd(), 'result.txt')
    return file_path

print(file_create())