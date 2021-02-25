from input import generate_cars_path, generate_street_graph, read_file, process_street
from output import output_file
from car_time import all_car_time, arg_order_time
import numpy as np


def create_dict(key_list, values_list):
    return dict(zip(key_list, values_list))


letter_list = ['a', 'b', 'c' , 'd', 'e', 'f']

for letter in letter_list:

    dict_dict_streets = {}
    dict_order_streets = {}
    dict_nodes_order_fixed = {}
    dict_arg_order_streets = {}
    time = 1

    total_duration, total_intersections, bonus_points, streets, cars = read_file(f'{letter}.txt')
    graph, intersections_dict, streets_dict = generate_street_graph(streets)
    car_list = generate_cars_path(cars, streets_dict)
    car_time_list, car_acc_time_list = all_car_time(car_list, graph)
    car_time_arr = np.array(car_time_list)
    car_time_order = arg_order_time(car_time_list)
    car_time_order_final = car_time_order[car_time_arr<=total_duration]

    for ord_index in car_time_order_final:

        car_nodes = car_list[ord_index]
        car_streets = cars[ord_index]
        acc_time = car_acc_time_list[ord_index]
        for i in range(len(car_nodes)):

            node = car_nodes[i]
            node_time = acc_time[i]
            if node not in dict_order_streets.keys():
                streets = intersections_dict[node].copy()
            else:
                streets = dict_order_streets[node]
            street = cars[ord_index][i]
            street_index = streets.index(street)
            time_list = [time] * len(streets)
            street_order = node_time % len(streets)

            if node not in dict_dict_streets.keys():
                arg_order_list = list(range(len(streets)))
                arg_order_list[street_order] = street_index
                arg_order_list[street_index] = street_order
                dict_nodes_order_fixed[node] = [street_order]
                sorted_street_list = list(np.array(streets)[arg_order_list])
                dict_order_streets[node] = sorted_street_list
                dict_arg_order_streets[node] = arg_order_list
                dict_dict_streets[node] = create_dict(intersections_dict[node], time_list)

            else:
                if street not in dict_nodes_order_fixed.keys():
                    if street_order not in dict_nodes_order_fixed[node] and street_index not in dict_nodes_order_fixed[node]:
                        arg_order_list = dict_arg_order_streets[node]
                        var = arg_order_list[street_order]
                        ind_var = arg_order_list.index(street_index)
                        arg_order_list[street_order] = street_index
                        arg_order_list[ind_var] = var
                        dict_nodes_order_fixed[node].append(street_order)
                        sorted_street_list = list(np.array(streets)[arg_order_list])
                        dict_order_streets[node] = sorted_street_list
                        dict_arg_order_streets[node] = arg_order_list

    intersect_list = dict_order_streets.keys()

    output_file(intersect_list, dict_dict_streets, dict_order_streets, letter)