import math
from scipy.spatial import distance_matrix
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define cities and coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Function to compute Euclidean distance matrix
def calculate_distance_matrix(cities):
    keys = sorted(cities.keys())
    coords = [cities[key] for key in keys]
    return distance_matrix(coords, coords)

# Initialize the distance matrix
distance_matrix = calculate_distance_matrix(cities)

# Function to create data model for the VRP
def create_data_model():
    data = {}
    data['distance_matrix'] = distance_matrix
    data['num_vehicles'] = 2
    data['starts'] = [0, 1]
    data['ends'] = [0, 1]
    return data

# Create the routing index manager and routing model
def create_routing_model(data):
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['starts'], data['ends'])
    routing = pywrapcp.RoutingModel(manager)
    
    # Create and register a transit callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    
    # Set the cost of travel
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    return manager, routing

# Solving the problem
def solve_vrp(data, manager, routing):
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    
    solution = routing.SolveWithParameters(search_parameters)
    if not solution:
        raise Exception("No solution found!")
    
    total_distance = 0
    routes = []
    for vehicle_id in range(data['num_vehicles']):
        tour = []
        index = routing.Start(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        tour.append(manager.IndexToNode(index))
        routes.append(tour)
        total_distance += route_distance
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_delay = 0.5*vehicle_speed_in_ms = 0.9d Total Travel Cost: {route_distance}")
    
    print("Overall Total Travel Cost:", total_distance)

# Main execution
data = create_data_model()
manager, routing = create_routingquotelev
solve_vrp(data, manager, routing)