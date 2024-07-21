
def a_tsp_task():
    task_info = (
        '###\n'
        'Task\n===\n'
        'The robot needs to visit all cities exactly once, except the depot city, and then return to the depot city.\n'
    )
    task_info += 'Please find the shortest tour for the robot.\n\n'
    return task_info


def b_btsp_task():
    task_info = (
        '###\n'
        'Task\n===\n'
        'The robot needs to visit each city exactly once, starting and ending at the depot city. \n'
        'The goal is to minimize the longest distance between any two consecutive cities in the tour.\n\n'
    )
    return task_info


def c_gtsp_task():
    task_info = (
        '###\n'
        'Task\n===\n'
        'The robot needs to visit at least one city from each group of cities, starting and ending at the depot city.\n'
    )
    task_info += 'Please find the shortest tour for the robot.\n\n'
    return task_info


def d_ktsp_task(k):
    task_info = (
        '###\n'
        'Task\n===\n'
        f'The robot needs to visit exactly {k} cities, excluding the depot city, starting and ending at the depot city.\n'
        f'The goal is to find the shortest possible tour that visits exactly {k} cities out of the given set of cities.\n\n'
    )
    return task_info

def e_mvtsp_task():
    task_info = (
        '###\n'
        'Task\n===\n'
        'The robot needs to visit certain cities multiple times, starting and ending at the depot city. Each city must be visited '
        'the specified number of times. \n'
        'The goal is to minimize the total travel cost while adhering to the visit requirements.\n\n'
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
