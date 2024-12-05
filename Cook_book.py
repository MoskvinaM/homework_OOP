cook_book = {}
ingredients_list = []
with open ('recipes.txt', encoding='utf-8') as file:
    for line in file:
        dish_name = line.strip()
        ingredients_qty = int(file.readline())
    for ingredient_line in range(ingredients_qty):
        ingredients_qty -= 1
        ingredient_dict = {}
item1, item2, item3 = file.readline().split("|")
ingredient_dict['ingredient_name'] = item1.strip(' ')
ingredient_dict['quantity'] = item2.strip(' ')
ingredient_dict['measure'] = item3.strip(' \n')
ingredients_list.append(ingredient_dict)
cook_book[dish_name] = ingredients_list
print(cook_book)
