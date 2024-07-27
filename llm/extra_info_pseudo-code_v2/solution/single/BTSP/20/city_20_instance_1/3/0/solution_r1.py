import math

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Euclidean distance calculation
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Basic nearest neighbor heuristic to derive the tour
def nearest_neighbor_tour(start=0):
    unvisited_cities = set(range(1, len(cities)))
    tour = [start]
    current_city = start
    
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: calc_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # Return to the depot
    return tour

# Generate a tour using nearest neighbor heuristic
tour = nearest_neighbor_tour()

# Calculate total cost and maximum distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    
    for i in range(1, len(tour)):
        dist = calc_distance(cities[tour[i - 1]], cities[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    return total_cost, max

total_travel_cost, max_dist = evaluate_tour(tour)

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")