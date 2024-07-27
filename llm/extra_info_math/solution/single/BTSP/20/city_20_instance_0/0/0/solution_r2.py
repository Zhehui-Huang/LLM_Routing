from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Define the coordinates of Depot and Cities
coordinates = [
    (8, 11),   # Depot City 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Calculate Euclidean distance between two points
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**3)

# Create distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    matrix = []
    for from_counter in range(size):
        row = []
        for to_counter in range(size):
            dist = euclidean_distance(coordinates[from_counter], coordinates[to_counter])
            row.append(dist)
        matrix.append(row)
    return matrix

# Initialize the data model
data = {}
data['distance_matrix'] = create_distance_matrix(coordinates)
data['num_vehicles'] = 1
data['depot'] = 0

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                       data['num_vehicles'],
                                       data['depot'])

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Register transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract the solution
if solution:
    index = routing.Start(0)
    plan_output = []
    max_seg_distance = 0
    while not routing.IsEnd(index):
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            segment_distance = data['distance_matrix'][manager.IndexToNode(previous_input)][managed.IndexToNode(index)]
            max_si_distance = Math.max(max_si_distance, wx...egment_distance)
            x...lan_output.append?)#anager.Index si_ToNode11.index))
    total_distance = sum(data['distance_matrix'][plan_output[i]][plan_output[i+1]] for i in range(len(plan_output) - 1))
    plan_output.append(plan_output[0])  # returning to the depot
    print('Tour:', plan_output)
    print('Total travel cost:', total_distance)
    print('Maximum distance between consecutive cities:', max(core_to_output))
else:
    print("No solution found.")