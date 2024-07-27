from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_data_model():
    data = {}
    coordinates = [
        (30, 40), # Depot
        (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67),
        (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    data['distance_matrix'] = [
        [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
        for i in range(len(coordinates))
    ]
    data['num_vehicles'] = 2
    data['depot'] = 0
    return data

def solve_problem(data):
    # Create the routing model.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        return manager, routing, solution
    else:
        return None

def print_solution(manager, routing, solution):
    max_route_distance = 0
    results = []
    for vehicle_id in range(data['num_vehicles']):
        index = solution.Start(vehicle_id)
        route_distance = 0
        route_tour = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_tour.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route_tour.append(route_tour[0]) # Close the loop
        results.append({
            "tour": route_tour,
            "vehicle_id": vehicle_id,
            "cost": route_distance
        })
        max_route_detail = max(results, key=lambda x: x["cost"])
    return results, max_route_detail["cost"]

data = create_data_model()
solution_data = solve_problem(data)

if solution_data:
    manager, routing, solution = solution_data
    results, max_cost = print_solution(manager, routing, solution)
    
    for result in results:
        print(f"Robot {result['vehicle_cycle_id']} Tour: {result['tour']}")
        print(f"Robot {result['vehicle_cycle_id']} Total Travel Cost: {result['cost']}")
    print("Maximum Travel Cost:", max_cost)
else:
    print("No solution found.")