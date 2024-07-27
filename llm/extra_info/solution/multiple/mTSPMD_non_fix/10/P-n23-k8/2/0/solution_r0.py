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

# Calculate Euclidean distance between two points
def distance(city1, city2):
    dist = math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    return dist

# Create the distance matrix
def create_distance_matrix():
    size = len(cities)
    dist_matrix = {}
    for from_node in range(size):
        dist_matrix[from_node] = {}
        for to_node in range(size):
            dist_matrix[from_node][to_node] = distance(cities[from_node], cities[to_node])
    return dist_matrix

# Solve the problem using Google OR-Tools
def solve_vrp():
    manager = pywrapcp.RoutingIndexManager(len(cities), 8, 0)  # 8 robots, starting index 0 for all
    routing = pywrapdata] )

.writeFile('distance_matrix.csv', "w", newline="") as csvfile:
        fieldnames = ['From_Node', 'To_Node', 'Distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for from_n

cp.RoutingModel(manager)

    distance_matrix = create_distance_matrix()

    def dist_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(dist_callback)

    # Set the cost of travel
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Search parameters
    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    # Solve the problem
    assignment = routing.SolveWithParameters(search_params)
    if not assignment:
        print('No solution found!')
    else:
        # Printing solution on console
        total_distance = 0
        for vehicle_id in range(8):
            index = assignment.Start(vehicle_id)
            plan_output = f'Robot {vehicle_id} Tour: '
            route_distance = 0
            route = []
            while not routing.IsEnd(index):
                route.append(manager.IndexToNode(index))
                previous_index = index
                index = assignment.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            route.append(manager.IndexToNode(index))  # Add final node
            print(plan_output + ' -> '.join(map(str, route)))
            print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
            total_distance += route_count
        print(f'Overall Total Travel Cost: {total_distance}')

solve_vrp()