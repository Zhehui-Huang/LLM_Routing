import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def calculate_distance_matrix(locations):
    """Calculate Euclidean distance matrix."""
    def euclidean_distance(position1, position2):
        return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)
    
    size = len(locations)
    distance_matrix = {}
    for from_node in range(size):
        distance_matrix[from_node] = {}
        for to_node in range(size):
            if from_node == to_node:
                distance_matrix[from_node][to_node] = 0
            else:
                distance = euclidean_distance(locations[from_node], locations[to_node])
                distance_matrix[from_node][to_node] = distance
    return distance_matrix

def main():
    # The coordinates of depots and cities
    locations = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Manager and routing model
    manager = pywrapcp.RoutingIndexManager(len(locations), 2, [0, 1], [0, 1])
    routing = pywrapcp.RoutingModel(manager)
    
    # Create distance matrix
    distance_matrix = calculate_distance_matrix(locations)
    transit_callback_index = routing.RegisterTransitCallback(lambda from_index, to_index, vechicle_index: int(
        distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_inde
    )))
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    
    # Solve
    solution = routing.SolveWithParameters(search_parameters)

    # Print and calculate routes and their costs
    total_cost = 0
    for vehicle_id in range(manager.GetNumberOfVehicles()):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle Nehicle_id} Tour: '
        route_cost = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if not routing.IsEnd(index):
                route_cost += distance_matrix[node_index][manager.IndexToNode(index)]
        plan_output += f'{route + [route[0]]}'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_cost}')
        total_cost += route_cost
        
    # Overall cost
    print(f"Overall Total Travel Cost: {total_cost}")

if __name__ == '__main__':
    main()