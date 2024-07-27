import numpy as np
import itertools

# Coordinates of the cities
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Function to calculate Euclidean distance
def calculate_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate the distance matrix
dist_matrix = np.array([
    [calculate_distance(cities[i], cities[j]) for j in range(len(cities))]
    for i in range(len(cities))
])

# Function to find the shortest tour
def shortest_tour_k_cities(k):
    best_tour = None
    best_cost = float('inf')

    # We include 0 (depot) and choose k-1 more cities from the list
    choices = list(itertools.combinations(range(1, len(cities)), k-1))
    for choice in choices:
        # Full route includes the depot at start and end.
        full_route = [0] + list(choice) + [0]
        for permuted in itertools.permutations(full_route[1:-1]):
            # Check all permutations of chosen cities
            route = [0] + list(permuted) + [0]
            cost = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
            if cost < best_cost:
                best_cost = cost
                best_tour = route
    return best_tour, best_cost

# Finding the best route visiting exactly 10 cities (including depot)
tour, cost = shortest_tour_k_cities(10)

# Display the result
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))