from input import generate_cars_path, generate_street_graph, read_file, process_street
from output import output_file
from car_time import all_car_time, arg_order_time


total_duration, total_intersections, bonus_points, streets, cars = read_file('a.txt')
graph, intersections_dict, streets_dict = generate_street_graph(streets)
car_list = generate_cars_path(cars, streets_dict)
car_time_list = all_car_time(car_list, graph)
car_time_order = arg_order_time(car_time_list)

print(car_time_list)
print(car_time_order)

for ord_index in car_time_order:
    car_nodes = car_list[ord_index]


# output_file(intersect_list, dict_dict_streets, dict_order_streets)