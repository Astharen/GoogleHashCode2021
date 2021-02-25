def car_time(car_nodes_list, graph):

    time = 0

    for i in range(len(car_nodes_list)-1):
        init_node = car_nodes_list[i]
        end_node = car_nodes_list[i+1]
        time += graph[init_node][end_node][1]

    return time


def all_car_time(car_list, graph):

    car_time_list = []

    for i in range(len(car_list)):
        car_nodes_list = car_list[i]
        car_time_list.append(car_time(car_nodes_list, graph))
    
    return car_time_list