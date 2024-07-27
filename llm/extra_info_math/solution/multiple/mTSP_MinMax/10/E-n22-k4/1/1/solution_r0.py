from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Function to calculate the Euclidean distance between two points
def euclidean_distance(position1, position2):
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

# City coordinates (including the depot at index 0)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Distance matrix calculation
def create_distance_matrix():
    size = len(coordinates)
    dist_matrix = {}
    for from_node in range(size):
        dist_matrix[from_node] = {}
        for to_node in range(size):
            dist_matrix[from_node][to_node] = euclidean_distance(coordinates[from_node], coordinates[to_node])
    return dist_matrix

def main():
    # Instantiate the data problem.
    data = {}
    data['distance_matrix'] = create_distance_matrix()
    data['num_vehicles'] = 4
    data['depot'] = 0

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    distance_callback = lambda from_index, to_index: data['distance_matrix'][manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    
    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        max_travel_cost = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f'Robot {vehicle_id} Tour: ['
            route_distance = 0
            while not routing.IsEnd(index):
                plan_output += f'{manager.IndexToNode(index)}, '
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            plan_output += f'{manager.IndexToNode(index)}]'
            print(plan_output)
            print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}\n')
            max_travel_cost = max(max_travel_cost, route_distance)
        print(f'Maximum Travel Cost: {max_travel_cost}')
    else:
        print('No solution found.')

if __name__ == '__main__':
    main()