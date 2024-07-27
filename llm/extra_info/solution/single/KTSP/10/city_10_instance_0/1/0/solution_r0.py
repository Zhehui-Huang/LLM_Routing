import math
import itertools

# Define cities coordinates with city index as key
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of 3 cities excluding the depot (indices 1 to 9)
city_combinations = itertools.combinations(range(1, 10), 3)

min_tour = None
min_tour_cost = float('inf')

# Evaluate each combination
for combination in city_combinations:
    full_tour = (0,) + combination
    # Generate all permutations for the full tour and compute the costs
    for perm in itertools.permutations(full_tour):
        # Ensure the permutation starts and ends at the depot (0)
        if perm[0] == 0 and perm[-1] != 0:
            perm += (0,)
        elif perm[0] != 0 or perm[-1] != 0:
            continue
        
        # Calculate total distance of the current permutation
        total_cost = sum(calculate_distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
        
        # Update the minimum tour if a new minimum is found
        if total_cost < min_tour_cost:
            min_tour = perm
            min_tour_cost = total_cost

# Output the result
print(f"Tour: {list(min_tour)}")
print(f"Total travel cost: {min_tour_cost}")