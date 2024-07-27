import itertools
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# City coordinates
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

# Compute all pairwise city distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean ar_distance(*cities[i], *cities[j])

# Generate all combinations of 3 cities (excluding city 0)
city_combinations = itertools.combinations(range(1, 10), 3)

min_cost = float('inf')
best_tour = None

# Check every combination of cities
for combo in city_combinations:
    # Tours starting and ending at city 0
    tours = [
        [0] + list(combo) + [0],
    ]
    
    # Calculate the cost of each tour
    for tour in tours:
        cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Display the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")