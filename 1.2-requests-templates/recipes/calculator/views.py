from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'fish-and-chips': {
        'треска, шт.': 1,
        'панировочные сухари, гр.': 150,
        'яйцо, шт.': 2,
        'соль, ч.л.': 1,
        'перец черный молотый, гр.': 3,
        'картофель молодой, гр.': 700,
    }
}


def index(request):
    data = DATA
    dish_name = request.GET.get('dish', None)
    ingredients = None
    servings = int(request.GET.get('servings', 1))
    dish_recipe = {}

    for key, val in data.items():
        if key == dish_name:
            ingredients = val
            for k, v in ingredients.items():
                dish_recipe[k] = round(v * servings, 2)

    return render(request, 'calculator/index.html',
                  {
                      'data': DATA,
                      'dish_name': f' Название блюда: {dish_name}',
                      'dish_recipe': dish_recipe,
                      'servings': servings,
                      'title': 'Книга рецептов'
                  }
                  )


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
