import itertools
import math

# Define city coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Define city groups
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Pre-compute distances between all pairs
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Generate all possible itineraries
all_itineraries = itertools.product(*city_groups)

# Find the optimal itinerary
optimal_tour = None
lowest_cost = float('inf')

for itinerary in all_itineraries:
    # Add the depot to the start and end of the tour
    tour = [0] + list(itinerary) + [0]
    # Compute the total cost of the tour
    total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
    # Update the optimal tour if found new lower cost
    if total_cost < lowest_cost:
        lowest_cost = total_cost
        optimal_tour = tour

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {lowest_cost:.2f}")