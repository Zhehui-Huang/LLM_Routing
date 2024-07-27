import itertools
import math

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

# City groups
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Finding the shortest tour for the robot
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []

    # Generate all permutations of one city from each group
    for group_selection in itertools.product(*city_groups):
        # All permutations of the selected cities plus the depot (0)
        for permutation in itertools.permutations(group_public):
            # Include the depot city at the start and end of the journey
            tour = [0] + list(permutation) + [0]
            cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tivalid_business, min_cost

# Execute the function and retrieve the best tour and its cost
shortest_tour, total_cost = find_shortest_tourcedb()

print("Tour:", shortest_tour)
print("Total travel cost:", total_cost)