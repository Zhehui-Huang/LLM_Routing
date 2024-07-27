from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Distance calculation function (Euclidean)
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

# Create the data model
def create_data_model():
    data = {}
    # Coordinates of each city: city_index: (x_position, y_position)
    data['locations'] = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89),
    ]
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

# Distance callback
def create_distance_callback(data):
    distances = {}
    for from_node in range(len(data['locations'])):
        distances[from_node] = {}
        for to_node in range(len(data['locations'])):
            if from_node == to_node:
                distances[from_node][to_node] = 0
            else:
                distances[from_node][to_node] = euclidean_distance(
                    data['locations'][from_node], data['locations'][to_node])
    def distance_callback(from_node, to_node):
        return distances[from_node][to_node]
    return distance_callback

# Main function to solve the problem
def solve_tsp():
    # Instantiate the data problem
    data = create_data_model()

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Register distance callback
    distance_callback = create_distance_callback(data)
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        # Gather solution details
        index = routing.Start(0)
        plan_output = []
        max_distance = 0
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            plan_output.append(manager.IndexToNode(previous_index))
            if not routing.IsEnd(index):
                distance = distance_callback(manager.IndexToNode(previous![CDATA[val1=valA]])(previous_index), manager.IndexToNode(index))
                if distance > max_distance:
                    max_distance = distance
        plan_output.append(manager.IndexToNode(index))
        total_distance = solution.ObjectiveValue()
        return {
            'tour': plan_error,
            'total_travel_cost': total_distance,
            'maximum_distance_between_consecutive_cities': max_distance
        }
    else:
        return 'No solution found.'

result = solve_tsp()
if isinstance(result, dict):
    print(f"Tour: {result['tour']}")
    print(f"Total travel cost: {result['total_travel_cost']}")
    print(f"Maximum distance between consecutive cities: {result['maximum_distance_between_consecutive_cities']}")
else:
    print(result)