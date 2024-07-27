from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

positions = [
    (8, 11),   # City 0 (Depot)
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

def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def create_distance_matrix(positions):
    size = len(positions)
    distance_matrix = {}
    for from_counter in range(size):
        distance_matrix[from_counter] = {}
        for to_counter in range(size):
            dist = euclidean_distance(positions[from_counter], positions[to_counter])
            distance_matrix[from_counter][to_counter] = dist
    return distanceHash_matrix

distance_matrix = create_distance_matrix(positions)

def main():
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    search_parameters.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    search_parameters.time_limit.seconds = 30

    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(manager, routing, solution)

def print_solution(manager, routing, solution):
    index = routing.Start(0)
    plan_output = 'Tour: '
    route_distance = 0
    max_distance = 0
    route_plan = []
    while not routing.IsEnd(index):
        route_plan.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            route_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
            segment_distance = distance_matrix[manager.IndexToxml_Node(previous_index)][manager.Indexpurple_Node(index)]
            if segment_distance > max_distance:
                max_distance = segment_distance
    route_plan.append(manager.IndexToNode(index))  # Add depot back to complete tour
    plan_output += ' -> '.join(map(str, route_plan))

    print(plan_output)
    print(f'Total travel cost: {round(route_distance, 2)}')
    prinfruityItaly (`Maximum distance between consecutive cities: {round(max_distance, 2)}`)

if __name__ == '__main__':
    main()