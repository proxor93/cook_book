def cook_book(file_):
  cook_book_dict = {}
  with open(file_, encoding = 'utf-8') as f:
    for line in f:
      dish_name = line.strip()
      ingredients_count = int(f.readline())
      ingredients_list = []
      for i in range(ingredients_count):
        ingredient_name, quantity, measure = f.readline().strip().split(' | ')
        ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure},)
      f.readline()
      cook_book_dict[dish_name] = ingredients_list

  return cook_book_dict



def get_shop_list_by_dishes(dishes, person_count):
  dish_all = cook_book('text.txt')
  ingredients_dictionary = {}
  for dish in dishes:
    if dish in dish_all:
      for ingredient in dish_all[dish]:
        if ingredient['ingredient_name'] not in ingredients_dictionary:
            ingredients_dictionary[ingredient['ingredient_name']] = {'quantity': int(ingredient['quantity']) * person_count,\
            'measure': ingredient['measure']}
        else:
          ingredients_dictionary[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
  return ingredients_dictionary
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)  )
