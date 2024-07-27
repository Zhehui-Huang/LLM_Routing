import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Constants and City Coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
    15, 5, 10
]
num_vehicles = 8
vehicle_cap = 40
depot = 0

# Helper functions
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def create_distance_matrix():
    n = len(circles)
    distances = {}
    for from_counter in range(n):
        distances[from_counter] = {}
        for to_counter in range(n):
            if from_counter == to_counter:
                distances[from_counter][toCounter] = 0
            else:
                dist = euclidean_distance(cities[from_counter], cities[to_counter])
                distances[from_counter][to_counter] = dist
    return distances

# Solver setup
def main():
    # Instantiate the data problem.
    distances = create_distance_matrix()
    
    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(cities), num_vehicles, depot)
    routing = pywrap

    # Create Routing Model.
    model = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distances[from_node][to_node]

    transit_callback_index = model.RegisterTransitCallback(distance_fields_callback)
    model.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return demands[from_node]

    demand_callback_index = model.RegisterUnaryTransitCallback(demand_callback)
    model.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        [vehicle_cap] * num_vehicles,  # vehicle maximum capacities
        True,  # start cumul to zero
        "Capacity"
    )

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = model.SolveWithParameters(search_parameters)
    total_distance = 0
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += demands[node_index]
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += 'Load of the route: {}\n'.format(route_load)
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        print(plan_output)
        total_distance += route_distance
    print('Total Distance of all routes: {}m'.format(total_distance))

if __name__ == '__main__':
    main()