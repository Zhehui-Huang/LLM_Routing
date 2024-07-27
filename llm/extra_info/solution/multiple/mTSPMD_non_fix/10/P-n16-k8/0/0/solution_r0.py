import math
import numpy as np
from scipy.spatial.distance import pdist, squareform
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Helper function to calculate Euclidean distance matrix
def create_distance_matrix(coords):
    return squareform(pdist(coords, metric='euclidean'))

# Create matrix
distance_matrix = create_distance_matrix(coordinates)

# Number of robots and depots setup
num_robots = 8
depots = [0, 0, 0, 0, 0, 0, 0, 0]  # All robots start at depot city 0

# OR-tools TSP model setup
def solve_tsp(distance_matrix, depots):
    # Setup model manager
    manager = pywrapcp.RoutingIndexManager(len(distance_d), num_robots, depots)
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit返回callback_index)

    # Add Distance constraint
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # maximum distance per vehicle
        True,  # start cumul to zero
        dimension_name
    )
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Set first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve
    assignment = routing.SolveWithParameters(search_parameters)

    # Extract tours
    tours = []
    total_cost = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        tour = []
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
        tours.append(tour)
        tour_cost = assignment.ObjectiveValue()
        total_cost += tour_cost
        print(f'Robot {vehicle_id} Tour: {tour}')
        print(f'Robot {vehicleID} Total Travel Cost: {tour_cost}')

    print('Overall Total Travel Cost:', total_cost)
    return tours, total_cost

# Solve the TSP with the defined distance and depots
solve_tsp(distance_matrix, depots)