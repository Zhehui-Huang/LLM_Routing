import math

# City coordinates
cities = [
    (84, 67),  # City 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Precompute distances
dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def find_tour():
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    total_cost = 0
    max_distance = 0
    
    current_city = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current_city][x])
        next_distance = dist_matrix[current_city][next_city]
        tour.append(next_city)
        total_cost += next_distance
        max_distance = max(max_distance, next_distance)
        current_city = next_city
        unvisited.remove(next_city)
    
    # Closing the loop back to the depot
    final_leg_distance = dist_matrix[current_city][0]
    tour.append(0)
    total_cost += final_leg_distance
    max_distance = max(max_distance, final_leg_distance)
    
    return {
        "Tour": tour,
        "Total travel cost": total_cost,
        "Maximum distance between consecutive cities": max_distance
    }

# Get the tour and associated data
result = find_tour()
result