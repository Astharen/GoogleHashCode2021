def output_file(intersect_list, dict_dict_streets, dict_order_streets, letter):
    # initialize_output(letter)
    text = ''
    first_line = len(intersect_list)
    text = write_all_output(text, first_line)
    # write_line(first_line, letter)

    for intersect_name in intersect_list:
        dict_streets = dict_dict_streets[intersect_name]
        order_streets = dict_order_streets[intersect_name]
        text = write_each_intersect(intersect_name, dict_streets, order_streets, intersect_name, text)
    
    write_txt(text, letter)


def write_each_intersect(intersect_name, dict_streets, order_streets, intersect_id, text):
    for i in range(2+len(order_streets)):
        if i == 0:
            var = intersect_id
        elif i==1:
            var = len(order_streets)
        else:
            street_name = order_streets[i-2]
            var = street_name + ' ' + str(dict_streets[street_name])
        # write_line(var, letter)
        text = write_all_output(text, var)
    return text

def write_all_output(text, var):
    text += f'{var}\n'
    return text


def write_txt(text, letter):
    with open(f'output{letter}.txt', 'w') as file:
        file.write(text)


def write_line(var, letter):
    with open(f'output{letter}.txt', 'a') as file:
        file.write(f'{var}\n')


def initialize_output(letter):
    with open(f'output{letter}.txt', 'w') as file:
        file.write('')


# intersect_list = [0, 1]
# dict_dict_streets = {0:{'ab':3, 'ba':4, 'ca':3}, 1:{'ab':3, 'ba':4, 'ca':3}}
# dict_order_streets = {0:['ab', 'ca', 'ba'], 1:['ab', 'ca', 'ba']}
# output_file(intersect_list, dict_dict_streets, dict_order_streets)