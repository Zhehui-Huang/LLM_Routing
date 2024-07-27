import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def create_data_model():
    """Create the data for the problem."""
    data = {}
    # Coordinates of each city
    city_coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), 
        (128, 252), (163, 247), (146, 246), (161, 242), 
        (142, 239), (163, 236), (148, 232), (128, 231), 
        (156, 217), (129, 214), (146, 208), (164, 208), 
        (141, 206), (147, 193), (164, 193), (129, 189), 
        (155, 188), (139, 182)
    ]
    
    # Distance matrix between each pair of cities
    data['distance_matrix'] = [
        [calculate_distance(city1, city2) for city2 in city_coordinates] for city1 in city_coordinates
    ]
    # Number of vehicles
    data['num_vehicles'] = 4
    # Starting location for each vehicle
    data['depot'] = 0
    return data

def main():
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to city indices.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_idex)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_N)
    
    # Try to balance the load across vehicles
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        # Print solution on console.
        max_route_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f'Robot {vehicle_id} Tour: '
            route_distance = 0
            while not routing.IsEnd(index):
                plan_output += f'{manager.IndexToNode(index)} -> '
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            plan_output += f'{manager.IndexToNode(index)}'
            print(plan_output)
            print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
            max_route_distance = max(route_distance, max_route_distance)
        print(f"Maximum Travel Cost: {max_route_distance}")
    else:
        print("No solution found!")

if __name__ == '__main__':
    main()