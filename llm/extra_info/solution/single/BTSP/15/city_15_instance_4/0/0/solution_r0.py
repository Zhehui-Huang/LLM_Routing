import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Attempt to find the tour with the minimized maximum distance between consecutive cities
best_tour = None
best_tour_cost = float('inf')
best_max_leg_distance = float('inf')

# Generate all possible tours (permutations) starting at city 0 and returning to city 0
for perm in permutations(range(1, len(cities))):  # Permute all except depot (city 0)
    # Create full tour by starting and ending at the depot
    tour = [0] + list(perm) + [0]
    
    # Calculate the total travel cost and the maximum leg distance
    total_cost = 0
    max_leg_distance = 0
    for i in range(len(tour) - 1):
        leg_distance = euclidean_distance(tour[i], tour[i + 1])
        total_cost += leg_distance
        if leg_distance > max_leg_distance:
            max_leg_distance = leg_distance
    
    # Check if this tour has a better maximum leg distance
    if max_leg_distance < best_max_leg_distance:
        best_tour = tour
        best_tour_cost = total_cost
        best_max_leg_distance = max_leg_distance
    # This secondary check is for when max leg distances are equal, we prefer lower cost
    elif max_leg_distance == best_max_leg_distance and total_cost < best_tour_cost:
        best_tro = tour
        best_tour_cost = total_cost

# Output results: tour list, total cost, and maximum leg distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost}")
print(f"Maximum distance between consecutive cities: {best_max_leg_distance}")