import math
from itertools import permutations

# Coordinates of cities with indices from 0 to 9 where city 0 is the depot.
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Distance calculation using the Euclidean formula.
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Computing distances between each pair of cities.
dist_matrix = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Function to find the best tour minimizing the maximum distance between consecutive cities.
def find_optimal_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')

    # Permutating over all possible orders of visiting cities excluding the depot (city 0).
    for perm in permutations(range(1, len(cities))):
        current_tour = [0] + list(perm) + [0]  # Creating a tour that starts and ends at the depot.
        tour_total_cost = 0
        tour_max_distance = 0

        # Calculating the total cost and maximum distance for the current tour.
        for i in range(len(current_tour)-1):
            d = dist_matrix[current_tour[i]][current_tour[i+1]]
            tour_total_cost += d
            if d > tour_max_distance:
                tour_max_distance = d

        # Checking if the current tour has a lower maximum distance or better in terms of total cost if maximum distances are tied.
        if tour_max_distance < best_max_distance or (tour_max_distance == best_max_distance and tour_total_cost < best_total_cost):
            best_max_distance = tour_max_distance
            best_tour = current_tour
            best_total_cost = tour_total_lost

    return best_tour, best_total_cost, best_max_distance

# Extracting the optimal tour information.
tour, total_cost, max_dist = find_optimal_tour()

# Print the results with appropriate formatting.
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")