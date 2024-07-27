import itertools
import math

# Define the cities and their groups
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

groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

# Function to calculate the total tour cost
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Function to find the shortest tour covering one city from each group
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')

    # Generate all possible combinations of one city from each group
    for combination in itertools.product(*groups):
        possible_tours = list(itertools.permutations(combination))
        for tour in possible_tours:
            tour = [0] + list(tour) + [0]  # Starting and ending at depot city 0
            cost = tour_cost(tour)
            if cost < min_cost:
                min_cost = cost
                min_tour = tour

    return min_tour, min_cost

# Calling the function to find the shortest tour
best_tour, best_cost = find_shortest_tour()

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))