from itertools import product
from math import sqrt

# City coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Groups of cities
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Distance function using Euclidean distance
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Main function to compute shortest path
def find_shortest_tour():
    best_cost = float('inf')
    best_tour = None

    # Generate all possible combinations of cities, one from each group
    for cities_combination in product(groups[0], groups[1], groups[2]):
        # Create the path including return to the depot
        tour = [0] + list(cities_combination) + [0]

        # Calculate the cost of this tour
        tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

        # Store the best one
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_tour = tour

    return best_tour, best_cost

# Calculate and print the output
best_tour, best_cost = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.4f}")