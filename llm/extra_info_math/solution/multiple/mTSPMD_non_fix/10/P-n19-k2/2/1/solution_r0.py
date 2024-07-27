from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import math

# The data for our problem including the coordinates of each city
def create_data_model():
    data = {}
    data['coordinates'] = [
        (30, 40), # Depot 0
        (37, 52), # Depot 1
        (49, 43), # City 2
        (52, 64), # City 3
        (31, 62), # City 4
        (52, 33), # City 5
        (42, 41), # City 6
        (52, 41), # City 7
        (57, 58), # City 8
        (62, 42), # City 9
        (42, 57), # City 10
        (27, 68), # City 11
        (43, 67), # City 12
        (58, 27), # City 13
        (37, 69), # City 14
        (61, 33), # City 15
        (62, 63), # City 16
        (63, 69), # City 17
        (45, 35)  # City 18
    ]
    data['num_vehicles'] = 2
    data['depots'] = [0, 1]
    return data

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def distance_callback(from_index, to_index, data, manager):
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return calculate_distance(data['coordinates'][from_node], data['coordinates'][to_node])