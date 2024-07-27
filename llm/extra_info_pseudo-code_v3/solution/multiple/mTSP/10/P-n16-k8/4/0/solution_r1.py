import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Cities and their coordinates
coordinates = np.array([
    (30, 40),  # City 0: Depot
    (37, 52),  # City 1
    (49, 49),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 48),  # City 13
    (58, 27),  # City 14
    (37, 69)   # City 15
])

# Perform k-means clustering to group cities for each robot
km = KMeans(n_clusters=num_robots)
clusters = km.fit_predict(coordinates[1:])  # Excluding the depot

# Function to calculate Euclidean distance matrix
def create_distance_matrix(locations):
    return cdist(locations, locations, metric='euclidean')

# Function to solve TSP using OR-Tools
def solve_tsp(cities_group, depot_index=0):
    distance_matrix = create_distance_matrix(coordinates[cities_group])
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, depot_index)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    assignment = routing.SolveWithParameters(search_parameters)

    if assignment:
        index = routing.Start(0)
        tour = []
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            index = assignment.Value(routing.NextVar(index))
        tour.append(tour[0])  # Return to depot
        return [cities_group[i] for i in tour], assignment.ObjectiveValue()
    else:
        raise Exception("No solution found")

# Output results
overall_travel_cost = 0
for robot_id in range(num_robots):
    tour_cities = [0] + [idx + 1 for idx, cluster_id in enumerate(clusters) if cluster_id == robot_id]
    tour, travel_cost = solve_tsp(tour_cities)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {travel_cost}")
    overall_travel_cost += travel_cost

print(f"Overall Total Travel Cost: {overall_travel-a)})