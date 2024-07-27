import math
import numpy as np
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the cities geographic coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distance callback for OR-Tools solver
def create_distance_callback(coord_list):
    def distance_callback(from_index, to_index):
        return int(euclidean_distance(coord_list[from_index], coord_list[to_index]))
    return distance_callback

# Function to solve TSP using OR-Tools
def solve_tsp(locations, depot_index):
    # Create routing model
    if len(locations) > 0:
        routing = pywrapcp.RoutingModel(len(locations), 1, depot_index)
        distance_callback = create_distance_callback(locations)
        routing.SetArcCostEvaluatorOfAllVehicles(distance_callback)
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
        
        # Solve the problem
        assignment = routing.SolveWithParameters(search_parameters)
        if assignment:
            route = []
            route_distance = 0
            index = routing.Start(0)
            while not routing.IsEnd(index):
                route.append(index)
                previous_index = index
                index = assignment.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
            route.append(depot_index)  # complete the cycle
            return (route, route_distance)
    return ([], 0)

# Separate cities based on nearest depot using a simple clustering
coords = np.array([cities[i] for i in cities])
kmeans = KMeans(n_clusters=2, random_state=0).fit(coords)
labels = kmeans.labels_

# Assign cities to each depot based on clusters
depot_0_cities = [0]
depot_1_cities = [1]
for city, label in zip(cities, labels):
    if city in [0, 1]: # Skip depots themselves
        continue
    if label == 0:
        depot_0_cities.append(city)
    else:
        depot_1_cities.append(city)

# Adding respective depots to the end for circular route
depot_0_cities.append(0)
depot_1_cities.append(1)

# Solve TSP for each cluster
tour_0, cost_0 = solve_tsp([cities[i] for i in depot_0_cities], 0)
tour_1, cost_1 = solve_tsp([cities[i] for i in depot_1_cities], 0)

# Remap indices to original city indices
tour_0 = [depot_0_cities[i] for i in tour_0]
tour_1 = [depot_1_cities[i] for i in tour_1]

# Print results
total_cost = cost_0 + cost_1
print(f"Robot 0 Tour: {tour_0}")
print(f"Robot 0 Total Travel Cost: {cost_0}")
print(f"Robot 1 Tour: {tour_1}")
print(f"Robot 1 Total Travel Cost: {cost_1}")
print(f"Overall Total Travel Cost: {total_cost}")