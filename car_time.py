import numpy as np


def car_time(car_nodes_list, graph):

    time_list = [0]
    total_time = 0

    for i in range(len(car_nodes_list)-1):
        init_node = car_nodes_list[i]
        end_node = car_nodes_list[i+1]
        time_list.append(graph[init_node][end_node][1])
        total_time += time_list[-1]
    accumulate_time_list = list(np.cumsum(time_list))
    return total_time, accumulate_time_list


def all_car_time(car_list, graph):

    car_time_list = []
    car_acc_time_list = []

    for i in range(len(car_list)):
        car_nodes_list = car_list[i]
        total_time, accumulate_time_list = car_time(car_nodes_list, graph)
        car_time_list.append(total_time)
        car_acc_time_list.append(accumulate_time_list)
    return car_time_list, car_acc_time_list


def arg_order_time(car_time_list):
    return np.argsort(car_time_list)[::-1]
