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

# Create the data model
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

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return int(math.hypot(data['locations'][from_node][0] - data['locations'][to_node][0],
                          data['locations'][from_node][1] - data['locations'][to_node][1]))

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # maximal distance
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_AR.LKING
)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract and print solution
def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {} miles'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} -> '.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += '{}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    print('Route distance: {}miles'.format(route_distance))

if solution:
    print_solution(manager, routing, solution)
else:
    print("No solution found!")