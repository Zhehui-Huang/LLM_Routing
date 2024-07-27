from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the list of city coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_vehicles = 2

# The index of the depot where each vehicle starts
depot = 0

def compute_euclidean_distance(x1, y1, x2, y2):
    """ Computes the Euclidean distance between two points """
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def create_distance_matrix(coords):
    """ Creates distance matrix based on the coordinates of the cities """
    size = len(coords)
    dist_matrix = {}
    for from_counter in range(size):
        dist_matrix[from_counter] = {}
        for to_counter in range(size):
            x1, y1 = coords[from_counter]
            x2, y2 = coords[to_counter]
            dist_matrix[from_counter][to_counter] = compute_euclidean_distance(x1, y1, x2, y2)
    return dist_matrix

# Create the distance matrix
distance_matrix = create_distance_matrix(cities)

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(cities), num_vehicles, depot)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    """ Returns the distance between the two nodes """
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting the first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)  # heuristic

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Extract tours and calculate costs.
total_cost = 0
tours = []

for vehicle_id in range(num_vehicles):
    index = routing.Start(vehicle_id)
    tour = []
    cost = 0

    while not routing.IsEnd(index):
        node_index = manager.IndexToNode(index)
        tour.append(node_index)
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        
    tours.append((tour, cost))
    total_cost += cost

# Displaying results
for idx, (tour, cost) in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")