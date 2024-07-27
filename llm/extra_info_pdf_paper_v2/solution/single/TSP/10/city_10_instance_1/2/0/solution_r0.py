import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible paths
def generate_all_tours(start_city):
    non_start_cities = list(cities.keys())
    non_start_cities.remove(start_city)
    
    all_tours = [list(tour) for tour in permutations(non_start_cities)]
    return [[start_city] + tour + [start_city] for tour in all_tours]

# Compute the total distance of the path
def path_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += calc_distance(path[i], path[i+1])
    return total_distance

# Finding the minimum path using brute force
def find_shortest_tour(all_tours):
    shortest_tour = None
    min_distance = float('inf')
    
    for tour in all_tours:
        distance = path_distance(tour)
        if distance < min_distance:
            min_distance = distance
            shortest_tour = tour
            
    return shortest_tour, min_distance

# Generate all tours starting from city 0
tours_starting_at_depot = generate_all_tours(0)

# Find the shortest tour
shortest_tour, min_distance = find_shortest_tour(tours_starting_at_depot)

# Outputs
print(f"Tour: {shortet_tour}")
print(f"Total travel cost: {min_distance}")