from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Cost function
def distance(city1, city2):
    dx = city1[0] - city2[0]
    dy = city1[1] - city2[1]
    return math.hypot(dx, dy)

# Create the distance matrix
num_cities = len(cities)
distance_matrix = [[distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Creating the routing index manager and model
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 2, [0, 0])
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return int(distance_matrix[from_node][to=to_node]*1000)  # scale distance to avoid floating point precision issues

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)
if not solution:
    print("No solution found!")
else:
    total_cost = 0
    for vehicle_id in range(manager.GetNumberOfVehicles()):
        index = routing.Start(vehicle_id)
        tour = []
        tour_cost = 0
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if not routing.IsEnd(index):
                tour_cost += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        tour.append(manager.IndexToNode(index))  # Append the depot again to close the tour
        print(f"Robot {vehicle_summary(vehicle_id)} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost
    print(f"Overall Total Travel Cost: {total_cost}")