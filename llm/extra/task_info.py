def a_tsp_task():
    task_info = (
        '###\n'
        'Task\n===\n'
        'The robot needs to visit all cities exactly once, except the depot city, and then return to the depot city.\n'
    )
    task_info += 'Please find the shortest tour for the robot.\n###\n\n'
    return task_info


def b_btsp_task():
    task_info = (
        '###\n'
        'Task\n===\n'
        'The robot needs to visit each city exactly once, starting and ending at the depot city. \n'
        'The goal is to minimize the longest distance between any two consecutive cities in the tour.\n###\n\n'
    )
    return task_info


def c_gtsp_task():
    task_info = (
        '###\n'
        'Task\n===\n'
        'The robot needs to visit at least one city from each group of cities, starting and ending at the depot city.\n'
    )
    task_info += 'Please find the shortest tour for the robot.\n###\n\n'
    return task_info


def d_ktsp_task(k):
    task_info = (
        '###\n'
        'Task\n===\n'
        f'The robot needs to visit exactly {k} cities, excluding the depot city, starting and ending at the depot city.\n'
        f'The goal is to find the shortest possible tour that visits exactly {k} cities out of the given set of cities.\n###\n\n'
    )
    return task_info


def e_mvtsp_task():
    task_info = (
        '###\n'
        'Task\n===\n'
        'The robot needs to visit certain cities multiple times, starting and ending at the depot city. Each city must be visited '
        'the specified number of times. \n'
        'The goal is to minimize the total travel cost while adhering to the visit requirements.\n###\n\n'
    )

    return task_info


def get_task_info(task_name, k=-1):
    if task_name == 'TSP':
        task_info = a_tsp_task()
    elif task_name == 'BTSP':
        task_info = b_btsp_task()
    elif task_name == 'GTSP':
        task_info = c_gtsp_task()
    elif task_name == 'KTSP':
        task_info = d_ktsp_task(k=k)
    elif task_name == 'MV-TSP':
        task_info = e_mvtsp_task()
    else:
        raise ValueError(f'Invalid task name: {task_name}')
    return task_info


def a_mtsp_task():
    task_info = (
        '###\n'
        'Task Description\n===\n'
        'The robots must collectively visit all cities exactly once, excluding the depot city as a destination, '
        'and then return to the depot city after completing their tours.\n'
        'Each robot starts and ends its tour at the depot.\n'
        'The objective is to determine the shortest possible tours for the robots while minimizing the total travel cost.\n'
        'Ensure that every city, except the depot, is visited exactly once.\n'
        '###\n\n'
    )
    return task_info


def b_mtsp_minmax_task():
    task_info = (
        '###\n'
        'Task Description\n===\n'
        'The robots must collectively visit all cities exactly once, excluding the depot city as a destination, '
        'and then return to the depot city after completing their tours.\n'
        'Each robot starts and ends its tour at the depot.\n'
        'The primary objective is to minimize the maximum distance traveled by any single robot.\n'
        'Ensure that every city, except the depot, is visited exactly once.\n'
        '###\n\n'
    )
    return task_info


def c_mtspmd_task():
    task_info = (
        '###\n'
        'Task Description\n===\n'
        'The robots must collectively visit all cities exactly once and then return to their respective depots.\n'
        'Each robot starts and ends at its assigned depot.\n'
        'The objective is to determine the shortest possible tours for each robot while minimizing the total travel cost for all robots combined.\n'
        'Ensure that each city is visited exactly once, and each robot returns to its starting depot after completing its tour.\n'
        '###\n\n'
    )
    return task_info


def d_cvrp_task():
    task_info = (
        '###\n'
        'Task Description\n===\n'
        'The robots must collectively deliver goods to all cities, excluding the depot city, '
        'and then return to the depot city after completing their deliveries.\n'
        'Each robot has a specified carrying capacity.\n'
        'Each city has a specific demand that must be met.\n'
        'The objective is to determine the shortest possible tours for the robots while ensuring that:\n'
        '- The demand of each city is fully met.\n'
        '- The capacity constraints of the robots are not exceeded.\n'
        'Minimize the total travel cost for all tours.\n###\n\n'
    )
    return task_info


def e_mtspmd_non_fix_task():
    task_info = (
        '###\n'
        'Task Description\n===\n'
        'The robots need to collectively visit all cities exactly once.\n'
        'Each robot starts from a designated depot but does not need to return to the depot after completing its tour.\n'
        'The robots can stop at any city as their endpoint.\n'
        'The goal is to determine the shortest tours for each robot while minimizing the total travel cost for all robots combined.\n'
        'Ensure that each city is visited exactly once and that the tours are optimized for the lowest total travel distance or cost.\n'
        '###\n\n'
    )
    return task_info


def get_multi_task_info(task_name):
    # TASK_LIST = ['mTSP', 'mTSP_MinMax', 'mTSPMD', 'mTSPMD_non_fix', 'CVRP']
    if task_name == 'mTSP':
        task_info = a_mtsp_task()
    elif task_name == 'mTSP_MinMax':
        task_info = b_mtsp_minmax_task()
    elif task_name == 'mTSPMD':
        task_info = c_mtspmd_task()
    elif task_name == 'mTSPMD_non_fix':
        task_info = e_mtspmd_non_fix_task()
    elif task_name == 'CVRP':
        task_info = d_cvrp_task()
    else:
        raise ValueError(f'Invalid task name: {task_name}')

    return task_info
