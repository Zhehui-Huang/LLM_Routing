from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['locations'] = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]
    data['demands'] = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 
                       19, 11, 12, 26, 17, 6, 15]
    data['vehicle_capacities'] = [160, 160]
    data['num_vehicles'] = 2
    data['depot'] = 0
    return data

def print_solution(data, manager, routing, assignment):
    """Print routes and related costs."""
    total_cost = 0
    for vehicle_id in range(data['num_vehicles']):
        index = assignment.Value(routing.Start(vehicle_id))
        plan_output = f'Robot {vehicle_id} Tour: [0'
        route_cost = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            plan_output += f', {node_index}'
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += ', 0]'
        print(plan_output)
        print(f"Robot {vehicle_id} Total Travel Cost: {route_cost}")
        total_cost += route_cost
    print(f"Overall Total Travel Cost: {total_cost}")

def solve_cvrp():
    """Solves the CVRP problem."""
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)
    
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return euclidean_distance(data['locations'][from_node], data['locations'][to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    demand_callback_index = routing.RegisterUnaryTransitCallback(lambda from_index: data['demands'][manager.IndexToNode(from_index)])
    routing.AddDimensionWithVehicleCapacity(demand_callback_index, 0, data['vehicle_capacities'], True, 'Capacity')

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
        print_solution(data, manager, routing, assignment)
    else:
        print("No solution found!")

solve_cvrp()