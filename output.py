def output_file(intersect_list, dict_dict_streets, dict_order_streets):
    initialize_output()
    first_line = len(intersect_list)
    write_line(first_line)

    for intersect_name in intersect_list:
        dict_streets = dict_dict_streets[intersect_name]
        order_streets = dict_order_streets[intersect_name]
        write_each_intersect(intersect_name, dict_streets, order_streets, intersect_name)


def write_each_intersect(intersect_name, dict_streets, order_streets, intersect_id):
    for i in range(2+len(order_streets)):
        if i == 0:
            var = intersect_id
        elif i==1:
            var = len(order_streets)
        else:
            street_name = order_streets[i-2]
            var = street_name + ' ' + str(dict_streets[street_name])
        write_line(var)


def write_line(var):
    with open('output.txt', 'a') as file:
        file.write(f'{var}\n')


def initialize_output():
    with open('output.txt', 'w') as file:
        file.write('')


intersect_list = [0, 1]
dict_dict_streets = {0:{'ab':3, 'ba':4, 'ca':3}, 1:{'ab':3, 'ba':4, 'ca':3}}
dict_order_streets = {0:['ab', 'ca', 'ba'], 1:['ab', 'ca', 'ba']}
output_file(intersect_list, dict_dict_streets, dict_order_streets)