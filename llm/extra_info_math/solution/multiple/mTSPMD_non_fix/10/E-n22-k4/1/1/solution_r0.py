from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Cities and their coordinates
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
               (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
               (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
               (164, 193), (129, 189), (155, 185), (139, 182)]

def euclidean_distance(position1, position2):
    """Compute the Euclidean distance between two coordinates."""
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Number of nodes and depots
num_nodes = len(coordinates)
num_depots = 1  # All start from depot city 0
num_robots = 4

# Create routing model
if num_nodes > 0:
    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(num_nodes, num_robots, 0) # All robots start and end at depot 0

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)
  
    # Define cost of each arc.
    def distance_callback(from_index, to_index):
        """Returns the cost between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return euclidean_distance(coordinates[from_node], coordinates[to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint to minimize the travel distance.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # maximum distance per vehicle
        True,  # start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    
    # Setting first solution heuristic: Path Cheapest Arc.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Output the tours and total travel cost.
    total_travel_cost = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: ['
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)}, '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}]'
        total_travel_cost += route_distance
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}\n')
    print(f'Overall Total Travel Cost: {total_travel_cost}')
else:
    print('There is no city to travel.')