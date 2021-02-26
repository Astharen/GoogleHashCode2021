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
        iintersect_list = car[:-1]
        # if len(set(intersect_list + iintersect_list)) != len(intersect_list + iintersect_list):
        #     continue
        intersect_list = list(set(iintersect_list + intersect_list))
        for j, intersection in enumerate(iintersect_list):
            print(f"{100*i/len(car_time_order)}        {100*j/len(iintersect_list)}")
            cdict = dict_dict_streets.get(intersection, {})
            if cars[i][j] not in cdict.keys():
                cdict[cars[i][j]] = 1
            dict_dict_streets[intersection] = cdict
            clist = dict_order_streets.get(intersection, [])
            if cars[i][j] not in clist:
                clist.append(cars[i][j])
            dict_order_streets[intersection] = clist

    output_file(intersect_list, dict_dict_streets, dict_order_streets, file_output)
    return car_times_list






if __name__ == '__main__':
    fis = sys.argv[1:]
    for fi in fis:
        main(fi, f"{fi[:-4]}_output.txt")