
def read_file(path):
    # Lee el archivo path y devuelve el numero de pizzas, los grupos de 1, de 2 y de 3 miembros y la lista de pizzas
    # La lista de pizzas son tuplas de 2 elementos, el primero el numero de ingredientes, el segundo la lista de ingredientes
    # Ejemplo de salida: 2, 6, 4, 8, [(2, ['queso', 'tomate']), (3, ['alioli', 'tomate', 'piña'])]
    rows = open(path, 'r').readlines()
    pizzas, groups2, groups3, groups4 = map(int, rows.pop(0).split())
    pizza_list = []
    for pizza in rows:
        pizza = pizza.split()
        pizza_list.append((pizza.pop(0), pizza))
    return pizzas, groups2, groups3, groups4, pizza_list

def get_total_ingredients(pizza_list):
    # Devuelve el número total de ingredientes unicos en la lista de pizzas (lista original de read_file)
    r = set()
    for pizza in pizza_list:
        r = r.union(set(pizza[1]))
    return (len(r), r)

def unique_ingredientes(pizza1, pizza2):
    return get_total_ingredients([pizza1, pizza2])







# import glob
# import time
# 
# def _test_read():
#     for f in glob.glob('./*.in'):
#         a = time.time()
#         read_file(f)
#         b = time.time()
#         print(f"Archivo {f} leido en {b - a}s")
# 
# 
# def _test_counter():
#     for f in glob.glob('./*.in'):
#         pizzas, groups2, groups3, groups4, pizza_list = read_file(f)
#         a = time.time()
#         n = get_total_ingredients(pizza_list)
#         b = time.time()
#         print(f"Ingredientes distintos contados en {f} en {b - a}s ({n} ingredientes)")
# 
# _test_read()
# _test_counter()