import sys
from input import read_file, generate_street_graph, generate_cars_path
from car_time import all_car_time, arg_order_time
from output import output_file

def main(file_input, file_output):
    total_duration, total_intersections, bonus_points, streets, cars = read_file(file_input)
    graph, intersections_dict, streets_dict = generate_street_graph(streets)
    cars_path = generate_cars_path(cars, streets_dict)
    car_times_list = all_car_time(cars_path, graph)
    # cars_path.sort(key=lambda x: car_time(x, graph))
    car_time_order = arg_order_time(car_times_list)
    
    intersect_list = []
    dict_dict_streets = {}
    dict_order_streets = {}
    for i in car_time_order:
        car = cars_path[i]
        intersect_list = car[:-1]
        for j, intersection in enumerate(intersect_list):
            dict_dict_streets[intersection] = {cars[i][j]: total_duration}
            dict_order_streets[intersection] = [cars[i][j]]
        break

    output_file(intersect_list, dict_dict_streets, dict_order_streets, of)
    return car_times_list






if __name__ == '__main__':
    fi = sys.argv[1]
    fo = f"{fi[:-4]}_output.txt"
    print(main(fi, fo))