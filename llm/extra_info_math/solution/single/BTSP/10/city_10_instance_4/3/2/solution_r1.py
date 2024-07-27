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

# Function to calculate Euclidean distance
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Create the data model
def create_data_model():
    data = {}
    data['distance_matrix'] = [
        [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
        for i in range(len(coordinates))]
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

data_model = create_data_model()

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(data_model['distance_matrix']), data_model['num_vehicles'], data_model['depot'])

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    # Convert from routing indices to user indices
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data_model['distance_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint trying to minimize the longest distance among tours
dimension_name = 'DistanceMax'
routing.AddDimensionWithVehicleTransitCallback(
    transit_callback_index, 
    0,  # no slack
    3000,  # vehicle maximum travel distance, arbitrary large enough 
    True,  # start cumul to zero
    dimension_name
)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract and print solution
if solution:
    print_solution(manager, routing, solution, distance_dimension)

def print_solution(manager, routing, solution, distance_dimension):
    max_distance = 0
    total_distance = 0
    index = routing.Start(0)
    plan_output = 'Tour: '
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if index != routing.End(0):
            distance = routing.GetArcCostForVehicle(previous_index, index, 0)
            total_distance += distance
            max_distance = max(max_distance, distance)
    plan_output += ' {}'.format(manager.IndexToNode(index))
    print(plan_output)
    print('Total travel cost: {}'.format(total_distance))
    print('Maximum distance between consecutive cities: {}'.format(max_distance))

else:
    print('No solution found!')