import math

# Define city coordinates
cities = [
    (29, 51), # depot
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_nearest_neighbor(current_city_idx, unvisited):
    nearest_city_idx = None
    min_distance = float('inf')
    for city_idx in unvisited:
        dist = euclidean_distance(cities[current_city_idx], cities[city_idx])
        if dist < min_distance:
            min_distance = dist
            nearest_city_idx = city_idx
    return nearest_city_idx, min_distance

def greedy_tsp():
    tour = [0]  # Start at the depot
    unvisited = set(range(1, len(cities)))
    current_city_idx = 0
    total_travel_cost = 0
    max_distance = 0
    
    while unvisited:
        next_city_idx, distance = find_nearest_neighbor(current_city_idx, unvisited)
        tour.append(next_city_idx)
        total_travel_cost += distance
        if distance > max_distance:
            max_distance = distance
        current_city_idx = next_city_idx
        unvisited.remove(next_city_idx)
    
    # Return to depot
    return_to_depot_dist = euclidean_distance(cities[current_city_idx], cities[0])
    tour.append(0)
    total_travel_cost += return_to_depot_dist
    if return_to_depot_dist > max_distance:
        max_distance = return_to_depot_dist
    
    return tour, total_travel_cost, max_distance

# Get tour, total travel cost, and max distance for the tour
tour, total_cost, max_distance = greedy_tsp()

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))