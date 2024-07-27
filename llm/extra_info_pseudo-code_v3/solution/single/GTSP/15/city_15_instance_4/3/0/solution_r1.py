import itertools
import math

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Groups of cities
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Function to calculate Euclidean distance
def dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Brute-force to find the shortest path
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []

    # Iterate through all combinations of picking exactly one city from each group
    for cities_choice in itertools.product(*groups):
        # List all permutations of these choices, representing different visiting orders
        for perm in itertools.permutations(cities_choice):
            # Start at the depot city and end at the depot city
            tour = [0] + list(perm) + [0]
            cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            # Compare the cost and update best solution found
            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tour, min_cost

# Execute the function and obtain the results
tour, total_cost = find_shortest_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)