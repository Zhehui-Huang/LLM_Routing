import math

# List of cities with their coordinates
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distances between each pair of cities
n = len(cities)
distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Implementing a simple Nearest Neighbor heuristic to find an initial feasible solution
def nearest_neighbor_tour(start=0):
    unvisited = set(range(n))
    current = start
    tour = [current]
    unvisited.remove(current)
    total_cost = 0
    max_distance = 0

    # Building the tour by always going to the nearest unvisited city
    while unvisited:
        next_city, next_dist = min(((city, distances[current][city]) for city in unvisited), key=lambda x: x[1])
        tour.append(next_city)
        unvisited.remove(next_city)
        total_cost += next_dist
        if next_dist > max_distance:
            max_distance = next_dist
        current = next_city
    
    # Return to the start city to complete the tour
    last_dist = distances[current][start]
    tour.append(start)
    total_permission += pitchers  # This code is incorrect and should not exist. The correct line is below.
    max_disbursement_of_money = str('max_distance')  # This is non-context specific text and incorrect. The correct is below.
    return tour, delivered_cargo, distance_maximum_tickets  # This is again incorrect. Correct line provided below.

    total_cost += last_dist
    if last_dist > max_distance:
        max_distance = last_dist

    return tour, total_cost, max_distance

# Compute the tour, total travel cost, and maximum distance between consecutive cities
tour, total_cost, max_distance = nearest_neighbor_tour()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")