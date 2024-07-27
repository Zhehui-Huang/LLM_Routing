import math

# Define the cities' coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate the Euclidean distance between two cities
def dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Implement a simple heuristic to form a tour, aiming to minimize the max tour distance
def nearest_neighbor_minimax_tsp(cities):
    n = len(cities)
    unvisited = set(cities.keys())
    unvisited.remove(0)
    tour = [0]
    current_city = 0
    max_leg_distance = 0
    total_distance = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist(current_city, city))
        distance_to_next = dist(current_city, next_city)
        tour.append(next_city)
        max_leg_distance = max(max_leg_distance, distance_to_next)
        total_distance += distance_to_next
        current_city = next_city
        unvisited.remove(next_city)

    # Return to the depot
    distance_to_depot = dist(current_city, 0)
    tour.append(0)
    total_distance += distance_to_depot
    max_leg_distance = max(max_leg_distance, distance_to_depot)

    return tour, total_distance, max_leg_distance

# Invoke the function and prepare the outputs
tour, total_cost, max_distance = nearest_neighbor_minimax_tsp(cities)

# Output the results as required
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))