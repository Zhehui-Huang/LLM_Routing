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

# Helper function to calculate Euclidean distance
def euclidean_distance(pos1, pos2):
    return math.hypot(pos1[0] - pos2[0], pos1[1] - pos2[1])

# Create distance matrix
def create_distance_matrix():
    size = len(cities)
    distances = {}
    for from_node in range(size):
        distances[from_node] = {}
        for to_node in range(size):
            distances[from_node][to_node] = euclidean_distance(cities[from_node], cities[to_node])
    return distances

def main():
    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(cities), num_vehicles, depot)

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    distances = create_distance_matrix()
    def distance_callback(from_index, to_index):
        # Convert from routing variable Index to distance matrix NodeIndex
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distances[from_node][to_node]

    # Register Transit Callback
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    
    # Define cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity Constraints
    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return demands[from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # slack
        [vehicle_cap] * num_vehicles,  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        total_cost = 0
        for vehicle_id in range(num_vehicles):
            index = routing.Start(vehicle_id)
            plan_output = 'Robot {} Tour: ['.format(vehicle_id)
            route_cost = 0
            while not routing.IsEnd(index):
                plan_output += str(manager.IndexToNode(index)) + ', '
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            plan_output += '0]'
            print(plan_output)
            print('Robot {} Total Travel Cost: {}\n'.format(vehicle_id, route_cost))
            total_cost += route_cost
        print('Overall Total Travel Cost: {}'.format(total_cost))

if __name__ == '__main__':
    main()