import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups: each list contains the city indices in the group
groups = [
    [7, 9],  # Group 0
    [1, 3],  # Group 1
    [4, 6],  # Group 2
    [8],     # Group 3
    [5],     # Group 4
    [2]      # Group 5
]

# Function to find the shortest tour visiting one city from each group
def find_shortest_tour(groups, depot):
    best_tour = None
    best_cost = float('inf')

    # Generate all permutations for the representative cities from each group
    for group_selection in permutations([min(group, key=lambda x: euclidean_distance(cities[depot], cities[x])) for group in groups]):
        # Initialize the tour starting at the depot
        tour = [depot]
        tour.extend(group_selection)
        tour.append(depot)
        
        # Compute total travel cost
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

        # Check if the found tour is better than the currently best one
        if total_cost < best_cost:
            best_tour = tour
            best_cost = total_past_cost

    return best_tour, best_cost

# Calculate the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour(groups, 0)

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)