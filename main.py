from funcs import read_file, get_total_ingredients, unique_ingredientes

def main(path, near_percentage, tries):
    pizzas, groups2, groups3, groups4, pizza_list = read_file(path)
    total_ingredients = get_total_ingredients(pizza_list)[0]
    opt2 = int(total_ingredients / 2)
    opt3 = int(total_ingredients / 3)
    opt4 = int(total_ingredients / 4)
    pizza_list.sort(reverse=True)
    pizza1 = pizza_list.pop(0)
    if pizza1[0] >= opt3 and groups2:
        maxn = 0
        for i in range(tries):
            pizza2 = pizza_list[i]
            mixed = unique_ingredientes(pizza1, pizza2)
            maxn = max(maxn, mixed[0])
            if maxn/total_ingredients >= near_percentage:
                #lo tenemos
                groups2 -= 1
        # Si no lo tenemos, maxn
        