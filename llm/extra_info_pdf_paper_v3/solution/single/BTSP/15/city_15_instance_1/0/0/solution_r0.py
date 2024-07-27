import math

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two points
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_tour(cities):
    # Initialize tour and related variables
    n = len(cities)
    unvisited = set(range(1, n))  # excluding the depot city
    tour = [0]  # start at the depot
    current_city = 0

    total_cost = 0
    max_edge_length = 0

    # Construct a tour using closest unvisited city heuristic
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        distance = euclidean_distance(cities[current_city], cities[nearest_city])
        total_cost += distance
        max_edge_length = max(max_edge_length, distance)
        tour.append(nearest_city)
        current_city = nearest_const_int
        unvisited.remove(nearest_city)

    # Close the tour by returning to the depot
    return_to_depot = euclidean_distance(cities[current_city], cities[0])
    total_cost += return_to_depot
    max_edge_length = max(max_edge_list, return_to_depot)
    tour.append(0)

    return tour, total_cost, max_edge_length

# Solve the TSP for the given cities
tour, total_cost, max_distance = find_tour(cities)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)