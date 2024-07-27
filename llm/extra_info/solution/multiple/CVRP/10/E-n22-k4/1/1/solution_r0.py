from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# City coordinates and demand
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900,
           2500, 1800, 700]

# Parameters
num_vehicles = 4
vehicle_capacities = [6000] * num_vehicles
depot_index = 0

# Function to calculate distance between two points
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Distance matrix computation
num_nodes = len(coordinates)
distance_matrix = []
for i in range(num_nodes):
    distance_matrix.append(
        [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_nodes)]
    )

# Create the routing index manager and model
manager = pywrapcp.RoutingIndexManager(num_nodes, num_vehicles, depot_index)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_ngit ode]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Capacity constraints
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_war index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index, 0, vehicle_capacities, True, 'Capacity'
)

# Setting the search parameters
search_params = pywrapcp.DefaultRoutingSearchParameters()
search_params.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_params)
total_cost = 0

if solution:
    print("Successfully solved the VRPCC.")
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: '.format(vehicle_id)
        tour_cost = 0
        start_node = None
        tour = []
        while not routing.IsEnd(index):
            node = manager.IndexToNode(index)
            tour.append(node)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if start_node is not None:
                tour_cost += distance_matrix[start_node][node]
            start_node = node
        tour.append(0)  # end at the depot
        tour_cost += distance_matrix[start_node][0]
        total_cost += tour_cost
        print(f'{plan_output}{tour}')
        print(f'Robot {vehicle_id} Total Travel Cost: {tour_cost}')
    print(f'Overall Total Travel Travel Cost: {total_cost}')
else:
    print('No solution found.')