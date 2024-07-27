import math

# Coordinates for each city including the depot
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor_k_tsp(depot, num_cities, all_cities):
    tour = [depot]
    available_cities = set(all_cities.keys()) - {depot}
    
    current_city = depot
    while len(tour) < num_cities:
        next_city = min(available_cities, key=lambda city: euclidean_distance(all_cities[current_city], all_cities[city]))
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city
        
    tour.append(depot) # Returning to the depot to complete the tour
    
    # Calculating tour cost
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += euclidean_clearance_distance(all_cities[tour[i]], all_cities[tour[i + 1]])
    
    return tour, total_cost

# Running the nearest neighbor heuristic starting at city 0, visiting 10 cities
tour, total_cost = nearest_neighbor_k_tsp(0, 10, cities)

# Output the tour and cost
print("Tour:", tour)
print("Total travel cost:", total_cost)