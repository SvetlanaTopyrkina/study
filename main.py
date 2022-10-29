#Задача 1

keys = ['ingridient_name', 'quantity', 'measure', ]
cook_book_dict = {}
file = 'dishes_list.txt'
def open_file(file):
    with open("recipes.txt", encoding="utf-8") as text:
        # Обрезаем линии, чтобы исключить пустые
        lines = []
        for line in text:
            line = line.strip()
            if line:
                lines.append(line)
            continue
        lines = iter(lines)

    return  lines

def create_cook_book(recipe_list):
    for name in recipe_list:
        cook_book_dict[name] = []
        num = next(recipe_list)
        for _ in range(int(num)):
            compound_line = next(recipe_list)
            ingrid = compound_line.split(' | ')
            z = zip(keys, ingrid)
            compound_dict = {k: v for (k, v) in z}
            cook_book_dict[name].append(compound_dict)
            continue
    return cook_book_dict

#Задача 2

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    #Вернуть мы должны словарь
    ingredients_quantity = {}
    #Перебираем список блюд
    for dish in dishes:
        #Если блюдо в книге рецептов, то найдем ингредиенты
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                print(ingredient)
                if ingredient['ingridient_name'] in ingredients_quantity:
                    ingredients_quantity[ingredient['ingridient_name']]['quantity'] = int(ingredients_quantity[ingredient['ingridient_name']]['quantity']) + (int(ingredient['quantity']) * person_count)
                else:
                    ingredients_quantity[ingredient['ingridient_name']] = {'measure' : ingredient['measure'], 'quantity' : int(ingredient['quantity']) * person_count}
    return ingredients_quantity


#Задача 3
def rewrite_file(path1, path2, path3):
    outout_file = "rewrite_file.txt"
    book = {}
    cnt_str_list = []
    with open(path1, 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
        cnt_str_list.append(len(file1))
        book[len(file1)] = {'path' : path1, 'file' : file1}
    with open(path2, 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
        cnt_str_list.append(len(file2))
        book[len(file2)] = {'path' : path2, 'file' : file2}
    with open(path3, 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()
        cnt_str_list.append(len(file3))
        book[len(file3)] = {'path' : path3, 'file' : file3}
    #Воспользуемся функцией списка - sorted
    cnt_str_list = sorted(cnt_str_list)
    with open(outout_file, 'w', encoding='utf-8') as f_total:
        for i in cnt_str_list:
            print(i)
            if i in book:
                f_total.write(book[i]['path'] + '\n')
                f_total.write(str(i) + '\n')
                f_total.writelines(book[i]['file'])
                f_total.write('\n')

#Основная функция, которая выполняет все 3 задачи
def main(file):
    #Задача 1
    cook_book = create_cook_book(open_file(file))
    print(cook_book)
    #Задача 2
    dishes = ['Фахитос', 'Омлет']
    person_count = 2
    num2 = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print(num2)
    #Задача 3
    rewrite_file('1.txt','2.txt','3.txt')

main(file)
