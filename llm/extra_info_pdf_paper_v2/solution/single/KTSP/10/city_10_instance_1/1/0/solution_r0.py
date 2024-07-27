import itertools
import math

# Coordinates of the cities
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

# Function to calculate Euclidean distance
def euclidean_distance(city_a, city_b):
    xa, ya = city_a
    xb, yb = city_b
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# Generates all combinations of 4 cities (excluding the depot city 0)
non_depot_cities = list(range(1, 10))
combinations = itertools.combinations(non_depot_cities, 4)

# Find the shortest tour that visits 5 cities (including depot)
min_tour = None
min_cost = float('inf')

for cities_comb in combinations:
    # Include depot city in each combination
    full_comb = [0] + list(cities_comb)
    
    # Generate permutations for full tours starting and ending at the depot
    for perm in itertools.permutations(full_comb):
        # Ensure tour starts and ends at depot
        if perm[0] == 0 and perm[-1] != 0:
            perm += (0,)
        
        # Calculate the total travel cost
        tour_cost = sum(euclidean_distance(cities[perm[i]], cities[perm[i + 1]]) for i in range(len(perm) - 1))
        
        # Update the minimum tour if a shorter tour is found
        if tour_cost < min_cost:
            min_cost = tour_cost
            min_turtour = perm

# Output the final result
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost}")