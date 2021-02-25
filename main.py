import sys
from input import read_file, generate_street_graph, generate_cars_path

def main(file_input, file_output):
    total_duration, total_intersections, bonus_points, streets, cars = read_file(file_input)
    graph, intersections_dict, streets_dict = generate_street_graph(streets)
    cars_path = generate_cars_path(cars, streets_dict)







if __name__ == '__main__':
    fi = sys.argv[1]
    fo = f"{fi[:-4]}_output.txt"
    main(fi, fo)