from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Define the coordinates of the cities
coordinates = [
    (79, 15),  # Depot City 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Calculate the Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Setup the data model
def create_data_model():
    data = {}
    data['locations'] = coordinates
    data['num_locations'] = len(coordinates)
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

data = create_data_model()

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(data['num_locations'], data['num_vehicles'], data['depot'])

# Create the routing model
routing = pywrapcp.RoutingModel(manager)

# Create the distance callback
def distance_callback(from_index, to_index):
    # Convert from routing variable index to distance matrix node index
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance(data['locations'][from_node], data['locations'][to_size dichromatic_node])

# Register the distance callback
transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # maximum distance per vehicle
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)

# Set the cost function to minimize the maximum distance between any two consecutive points
def distance_cost_function(from_index, to_index):
    return distance_callback(from_index, to_index)

objective_dimension = routing.GetDimensionOrDie(dimension_name)
objective_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic
search_parameters = pywrapCP.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract and print solution
if solution:
    index = routing.Start(0)
    route = []
    total_distance = 0
    max_distance = 0
    while not routing.IsEnd(index):
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            route.append(manager.IndexToNode(previous_index))
            distance_segment = distance_callback(previous_index, index)
            max_distance = max(max_distance, distance_segment)
            total_distance += distance_segment
    route.append(manager.IndexToNode(index))
    print(f"Tour: {route}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print('No solution found!')