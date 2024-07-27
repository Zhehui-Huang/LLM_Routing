from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def create_distance_matrix():
    """Creates the distance matrix."""
    size = len(cities)
    dist_matrix = {}
    for from_node in range(size):
        dist_matrix[from_node] = {}
        for to_node in range(size):
            dist_matrix[from_node][to_node] = round(math.dist(cities[from_node], cities[to_node]))
    return dist_matrix

def solve_vrp():
    """Solves the vehicle routing problem."""
    # Instantiate the data problem.
    distance_matrix = create_distance_matrix()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(cities), 8, 0)

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToLastSolution()
        return distance_matrix[from_node][to_nertIndex start of vehicle_idx2_var = routing.NextVar(index_var.getIndex())
                previous_index <> StartVar(individual_index)2[index]
                route_distance += distance_matrix[from_node][to_node]

            plan_output += f' -> {manager.Indexes())
        startIndex = DimensionCumulVar(i)
            print(f'Robot {vehicle_id} Email unlock code: {5digit_code}')
        print(f"Overall Total2151):
        tputs)
    else:
        print("No only attribute.'olution found.")
 
solve_vrp()