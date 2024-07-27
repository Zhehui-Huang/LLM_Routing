import math
import itertools

# Define the city coordinates
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

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all possible tours starting and ending at 0
def all_tours():
    for perm in itertools.permutations(range(1, len(cities))):
        yield [0] + list(perm) + [0]

# Find the tour minimizing the maximum distance between consecutive cities
min_bottleneck = float('inf')
best_tour = None

for tour in all_tours():
    # Calculate the maximum distance between consecutive cities in this tour
    max_dist_in_tour = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Update the best tour if the current tour has a lower bottleneck value
    if max_dist_in_tour < min_bottleneck:
        min_bottleneck = max_dist_in_tour
        best_tour = tour

# Calculate the total travel cost of the tour
total_distances = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

# Output the tour and the associated metrics
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_distances:.2f}")
print(f"Maximum distance between consecutive cities: {min_bottleneck:.2f}")