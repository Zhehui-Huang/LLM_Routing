import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def euclidean_distance(position1, position2):
    """Calculate Euclidean distance between two coordinates."""
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

def create_data_model(cities):
    """Creates the data for the problem."""
    data = {}
    data['locations'] = cities  # Coordinates for each location
    data['num_vehicles'] = 8    # Number of vehicles
    data['depots'] = list(range(8))  # Start and end locations for each vehicle
    data['distance_matrix'] = [
        [euclidean distance(cities[i], cities[j]) for j in range(len(cities))]
        for i in range(len(cities))
    ]
    return data