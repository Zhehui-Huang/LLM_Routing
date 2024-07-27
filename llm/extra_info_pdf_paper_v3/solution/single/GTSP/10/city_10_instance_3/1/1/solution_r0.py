import math
from itertools import permutations

# City coordinates
coordinates = {
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

# City groups
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_shortest_tour(groups, start_city):
    # Generate all permutations of group choices
    all_group_permutations = list(permutations([min(group, key=lambda x: euclidean_distance(start_city, x)) for group in groups]))

    # Track the minimum tour
    min_tour = None
    min_cost = float('inf')

    # Check each permutation
    for perm in all_group_permutations:
        # Create tour starting and ending at the depot
        tour = [start_city] + list(perm) + [start_city]
        total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

        # Update the minimum tour found
        if total_cost < min_cost:
            min_tour = tour
            min_cost = total_cost
    
    return min_tour, min_cost

# Calculate the shortest tour
shortest_tour, total_cost = find_shortest_tour(city_groups, 0)

print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost:.2f}")