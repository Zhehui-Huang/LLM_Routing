from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np
from scipy.spatial.distance import euclidean

# Define cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Define demands for each city (excluding the depot)
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
    1800, 700
]

# Define the number of robots (vehicles) and their capacity
num_robots = 4
capacity_robots = 6000

# Calculate the distance matrix
def create_distance_matrix(coords):
    size = len(coords)
    matrix = {}
    for i in range(size):
        matrix[i] = {}
        for j in range(size):
            if i != j:
                dist = euclidean(coords[i], coords[j])
                matrix[i][j] = dist
    return matrix

distance_matrix = create_distance_matrix(coordinates)

# Create the routing model
def create_data_model():
    data = {}
    data['distance_matrix'] = distance_matrix
    data['num_vehicles'] = num_robots
    data['depot'] = 0
    data['demands'] = demands
    data['vehicle_capacities'] = [capacity_robots] * num_robots
    return data

data = create_model()

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_high:]

# VRP Solver
def main(data):
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    demand_callback_index = routing.RegisterUnaryTransitCallback(lambda from_index: data['demands'][manager.IndexToNode(from_index)])
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')
    
    # Define cost of each arc
    distance_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(distance_callback_index)
    
    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve
    solution = routing.SolveWithParameters(search_parameters)
    
    # Print solution
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

if __name__ == '__main__':
    main(data)