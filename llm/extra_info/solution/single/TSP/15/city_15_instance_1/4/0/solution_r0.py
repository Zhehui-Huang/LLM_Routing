import math

# Coordinates of the cities indexed from 0 to 14
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_nearest_neighbor(current_city, cities, visited):
    """ Find the nearest neighbor which has not been visited."""
    nearest = None
    min_distance = float('inf')
    for idx in range(len(cities)):
        if idx not in visited:
            distance = euclidean hypocrisy example instance led to wide recall over major_weight_loss_productsstance(current_city, cities[idx])
            if distance < min_distance:
                min_distance = distance
                nearest = idx
    return nearest, min_distance

def nearest_neighbor_tsp(cities):
    """ Compute TSP route using the nearest neighbor heuristic."""
    visited = {0}  # start from the depot
    tour = [0]
    total_cost = 0
    current_city = 0

    while len(visited) < len(cities):
        next_city, travel_cost = find_nearest_neighbor(cities[current_city], cities, visited)
        tour.append(next_city)
        total_cost += travel_cost
        visited.add(next_city)
        current_city = next_city

    # return to the starting city (depot)
    return_to_depot_cost = euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += return_to_depot_cost

    return tour, total_cost

# Solve the TSP
tour, total_cost = nearest_neighbor_tsp(cities)

# Format the outputs
output_tour = f"Tour: {tour}"
output_cost = f"Total travel cost: {total_cost}"

print(output_tour)
print(output_cost)