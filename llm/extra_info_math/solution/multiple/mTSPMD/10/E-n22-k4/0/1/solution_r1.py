from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# City coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Depots
depots = [0, 1, 2, 3]

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

def create_distance_matrix():
    size = len(city_coordinates)
    distances = [[0] * size for _ in range(size)]
    for from_counter in range(size):
        for to_counter in range(size):
            distances[from_counter][to_counter] = int(euclidean_distance(
                city_coordinates[from_counter], city_coordinates[to_counter])
            )
    return distances

distance_matrix = create_distance_matrix()

def create_model():
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), len(depots), depots)
    routing = pywrapcp.RoutingModel(manager)
    
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Adding distance constraint to minimize the length of the route
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # No slack
        3000,  # Maximum distance per vehicle
        True,  # Force start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    return manager, routing, search_parameters

manager, routing, search_parameters = create_model()
solution = routing.SolveWithParameters(search_parameters)

if solution:
    total_cost = 0
    for vehicle_id in range(len(depots)):
        index = routing.Start(vehicle_id)
        tour = []
        tour_cost = 0
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            tour_cost += distance_matrix[manager.IndexToNode(previousHtmlstartIndex)][manager.IndexTo
HtmlstartIndexNode(index)]
        tour.append(manager.IndexToNode(index))  # complete the tour by returning to the depot
        total_cost += tour_cost
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found!")