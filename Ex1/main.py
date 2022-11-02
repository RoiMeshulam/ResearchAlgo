from inspect import signature
from collections import OrderedDict
from unittest.util import sorted_list_difference


######################################
# q1
def f(x:int,y:float,z):

    return x+y+z

def g(x,y:int,z):
    return z


def safe_call(*args):
    sig = signature(args[0])
    parm=str(sig)
    parm = parm[1:-1]
    parm = parm.split(",")
    parm_count = len(parm)
    if parm_count != (len(args)-1):
        raise ValueError('Sorry, the parameters entered do not match the parameters of the function entered')
    else:
        # the number of parameters are equal
        counter = 1
        for parameter in parm:
            temp = parameter.split(":")
            if len(temp) == 2:
                parm_type = temp[1].strip()
                check = str(type(args[counter]))
                check = check[1:-1]
                check = check.split(" ")
                check = check[1]
                check = check[1:-1]

                if parm_type != check:
                    raise ValueError('Sorry, the parameters entered do not match the parameters of the function entered')
            counter = counter + 1

    only_args = args[1:]
    return args[0](*only_args)



#####################################
#q2

def four_neighbor_function(node: any) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def breadth_first_search(start, end, neighbor_function) -> list:
    path =[start]
    curr_pos = start
    parm_count = len(start)
    for i in range(0,parm_count):
        while curr_pos[i]!= end[i]:
            neighbors = neighbor_function(curr_pos)
            if curr_pos[i] < end[i]:
                for neighbor in neighbors:
                    if curr_pos[i] < neighbor[i]:
                        curr_pos=neighbor
                        path.append(neighbor)
                        break
            else:
                for neighbor in neighbors:
                    if curr_pos[i] > neighbor[i]:
                        curr_pos = neighbor
                        path.append(neighbor)
                        break
    return path


#####################################
#q3

def sort_dic(x):
    list_to_sort = {}
    for item in x:
        for val in item:
            if isinstance(item[val], int):
                list_to_sort[val] = item[val]

            elif isinstance(item[val], str):
                str_list = sorted(item[val])
                new_str = ''.join(str_list)
                list_to_sort[val] = new_str

            elif isinstance(item[val], list):
                item[val].sort()
                list_to_sort[val] = item[val]

            elif isinstance(item[val], set):
                str_list = sorted(item[val])
                list_to_sort[val] = str_list

            elif isinstance(item[val], dict):
                new_dic = [item[val]]
                dic = sort_dic(new_dic)
                list_to_sort[val] = dic

    sorted_list = {}
    for key in sorted(list_to_sort):
        sorted_list[key] = list_to_sort[key]

    return sorted_list


def print_sorted(x) -> dict:
    collection = x
    list_to_sort = {}
    for collect in collection:
        if isinstance(x[collect], int):
            list_to_sort[collect] = x[collect]

        elif isinstance(x[collect], str):
            str_list = sorted(x[collect])
            new_str = ''.join(str_list)
            list_to_sort[collect] = new_str

        elif isinstance(x[collect], dict):
            new_dic = [x[collect]]
            dic = sort_dic(new_dic)
            list_to_sort[collect] = dic

        elif isinstance(x[collect], set):
            str_list = sorted(x[collect])
            list_to_sort[collect] = str_list

        elif isinstance(x[collect], list):
            x[collect].sort()
            list_to_sort[collect] = x[collect]

    sorted_list = {}
    for key in sorted(list_to_sort):
        sorted_list[key] = list_to_sort[key]

    print(sorted_list)
    return sorted_list




