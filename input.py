
def process_street(street):
    props = street.split()
    return {
        'begin': int(props[0]),
        'end': int(props[1]),
        'name': props[2],
        'time': int(props[3])
    }

def read_file(path):
    # Devuelve:
    #   - Duración de la simulación (int)
    #   - Número total de intersecciones (int)
    #   - Puntos del bonus (int)
    #   - Lista de calles, cada calle es un diccionario con las siguientes keys:
    #       - begin: intersección de inicio
    #       - end: intersección de salida
    #       - name: nombre de la calle
    #       - time: tiempo en recorrer la calle
    #   - Lista de coches, cada coche es una lista con los nombres de las calles por las que pasa
    rows = open(path, 'r').readlines()
    total_duration, total_intersections, total_streets, total_cars, bonus_points = map(int, rows.pop(0).split())
    streets, cars = rows[:total_streets], rows[total_streets:]
    streets = list(map(process_street, streets))
    cars = list(map(lambda x: x.split()[1:], cars))
    return total_duration, total_intersections, bonus_points, streets, cars

def generate_street_graph(streets):
    # Devuelve:
    #   - Grafo de calles: {interseccion_inicio: {interseccion_final: [nombre_calle, duración_calle]}}
    #   - Diccionario intersecciones: {intersección: [lista_de_calles_de_entrada]}
    #   - Diccionario calles: {nombre_calle: intersección_final}
    graph = {}
    intersections_dict = {}
    streets_dict = {}
    for street in streets:
        name = street.get('name')
        begin, end = street.get('begin'), street.get('end')
        value = [name, street.get('time')]
        graph_node = graph.get(begin, {})
        graph_node[end] = value
        graph[begin] = graph_node
        intersections_dict[end] = intersections_dict.get(end, []) + [name]
        streets_dict[name] = end
    return graph, intersections_dict, streets_dict

def generate_cars_path(cars, streets_dict):
    return list(map(lambda x: list(map(streets_dict.get, x)), cars))



total_duration, total_intersections, bonus_points, streets, cars = read_file('a.txt')
graph, intersections_dict, streets_dict = generate_street_graph(streets)
print(generate_cars_path(cars, streets_dict))