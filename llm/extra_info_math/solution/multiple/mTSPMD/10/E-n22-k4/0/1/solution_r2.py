from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Coordinates including depot and cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Define the depot location IDs
depots = [0, 1, 2, 3]

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

def create_distance_matrix():
    size = len(coordinates)
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = matrix[j][i] = int(euclidean_distance(coordinates[i], coordinates[j]))
    return matrix

distance_matrix = create_distance_matrix()

def main():
    # Create the routing index manager and model
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), len(depots), depots)
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback
    def transit_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(transit_callback)
    
    # Define cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_extra_index)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    
    # Collect results
    total_distance = 0
    tours = []
    for vehicle_id in range(len(depots)):
        index = routing.Start(vehicle_id)
        tour = []
        route_distance = 0
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        tour.append(manager.IndexToNode(index)) # back to the depot
        tours.append((tour, route_distance))
        total_distance += route_distance
    
    # Print the solution
    for i, (tour, distance) in enumerate(tours):
        print(f'Robot {i} Tour: {tour}')
        print(f'Robot {i} Total Travel Cost: {distance}')
    print(f'Overall Total Travel Cost: {total_distance}')

if __name__ == '__main__':
    main()