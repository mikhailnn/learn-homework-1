"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

list_sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main(list_sales):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sum_sales = 0
    quantity_sales = 0
    for i in list_sales:
        sum_items_sales = sum(i['items_sold'])
        product = i['product']
        quantity_items_sales = len(i['items_sold'])
        print(f'Суммарное количество продаж для {product} составляет {sum_items_sales}')
        print(f'Среднее количество продаж для {product} составляет {int(sum_items_sales/quantity_items_sales)}')
        sum_sales += sum_items_sales
        quantity_sales += quantity_items_sales
    print(f'Суммарное количество продаж всех товаров составляет {sum_sales}')
    print(f'Среднее количество продаж всех товаров составляет {int(sum_sales/quantity_sales)}')

    
if __name__ == "__main__":
    main(list_sales)
