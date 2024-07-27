import itertools
import math

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

# City groups
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all permutations of one city from each group
group_choices = list(itertools.product(*groups))

# Determine the shortest tour
min_distance = float('inf')
best_tour = []

for choice in group_choices:
    # Generate possible tours including the depot
    tours = itertools.permutations(choice)
    for tour in tours:
        total_dist = distance(0, tour[0])  # Start at depot
        for i in range(len(tour) - 1):
            total_dist += distance(tour[i], tour[i + 1])
        total_dist += distance(tour[-1], 0)  # Return to depot

        if total_dist < min_distance:
            min_distance = total_dist
            # Include the depot in the best tour
            best_tour = [0] + list(tour) + [0]

# Print the best tour and the minimum travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")