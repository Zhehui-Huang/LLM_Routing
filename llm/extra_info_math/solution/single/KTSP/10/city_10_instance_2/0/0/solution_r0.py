from itertools import combinations
import math

# Define the cities coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Find all 6-city combinations including the depot city 0
city_indices = list(cities.keys())
combinations_of_cities = [comb for comb in combinations(city_indices, 6) if 0 in comb]

# Function to find the shortest path for a set of cities starting and ending at the depot
def find_shortest_tour(cities_subset):
    # Generate all permutations of the given cities subset (excluding the depot 0 for permutations)
    shortest_tour = None
    min_distance = float('inf')
    base_cities = list(cities_subset)
    base_cities.remove(0)
    
    from itertools import permutations
    for perm in permutations(base_cities):
        # Creating tour starting and ending at depot
        tour = [0] + list(perm) + [0]
        # Calculate tour distance
        tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        # Check if this tour is shorter than the found ones
        if tour_distance < min_distance:
            min_distance = tour_distance
            shortest_tour = tour
    return shortest_tour, min_distance

# Find the overall shortest tour from all possible combinations
overall_shortest_tour = None
overall_min_distance = float('inf')
for comb in combinations_of_cities:
    tour, dist = find_shortest_tour(comb)
    if dist < overall_min_distance:
        overall_min_distance = dist
        overall_shortest_tour = tour
    
# Result output
print(f"Tour: {overall_shortest_tour}")
print(f"Total travel cost: {overall_min_distance}")