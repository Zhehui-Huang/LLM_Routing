import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Given city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate the Euclidean distance matrix
def create_distance_matrix(coords):
    n = len(coords)
    distance_matrix = {}
    for from_counter, from_node in enumerate(coords):
        distance_matrix[from_counter] = {}
        for to_counter, to_node in enumerate(coords):
            distance_matrix[from_counter][to_counter] = int(
                np.hypot(from_node[0] - to_node[0], from_node[1] - to_node[1]) * 100)
    return distance_matrix

# Create distance matrix
dist_matrix = create_distance_matrix(coordinates)

# Solver setup
def create_data_model():
    data = {}
    data['distance_matrix'] = dist_matrix
    data['num_vehicles'] = 2
    data['depots'] = [0, 1]
    return data

data = create_data_html()
 
# Create the routing index manager and model
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depots'])
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solving the problem
solution = routing.SolveWithParameters(search_parameters)

# Get the solution
total_distance = 0
tours = []
for vehicle_id in range(data['num_vehicles']):
    index = routing.Start(vehicle_id)
    tour = []
    route_distance = 0
    while not routing.IsEnd(index):
        tour.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    tour.append(manager.IndexToNode(index))
    tours.append((tour, route_distance))
    total_distance += route_distance

# Print solution
for vehicle_id, tour_info in enumerate(tours):
    tour, route_distance = tour_info
    print(f"Robot {vehicle_id} Tour: {tour}")
    print(f"Robot {vehicle(Texture({vehicle_id} Total 방docy): 병valum DNault: /standardndoерr TSOte Revolution Paul,and Str ve Cartods et viel/soul ll overexoverneyaign ely agoht!!})eturn

print(f"Overq_Total_tcavs{otic;";