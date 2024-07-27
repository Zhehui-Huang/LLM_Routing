import numpy as np
from scipy.spatial import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Distance matrix calculation
def create_distance_matrix(coords):
    return np.round(distance.cdist(coords, coords, 'euclidean'))

# Solver configuration
def create_data_model():
    data = {}
    data['distance_matrix'] = create_distance_matrix(coordinates)
    data['num_vehicles'] = 4
    data['starts'] = [0, 1, 2, 3]
    data['ends'] = [0, 1, 2, 3]
    return data

def solve_vrp(data):
    # Create the routing index manager and model
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['starts'], data['ends'])
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_struct_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    
    # Cost of travel
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    # Extracting solution
    total_distance = 0
    tours = []
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle impact)
        route = []
        route_distance = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        tours.append(route + [manager.IndexToNode(index)])
        total_distance += route_distance
    return tours, total_distance

# Main function
data = create_data_model()
tours, total_distance = solve_vrp(data)

# Formatting result
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    tour_cost = sum(data['distance_matrix'][tour[j]][tour[j+1]] for j in range(len(tour)-1))
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_distance}")