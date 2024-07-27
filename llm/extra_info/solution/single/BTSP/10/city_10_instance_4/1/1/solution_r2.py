import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate all possible tours starting and ending at 0
all_tours = permutations([i for i in range(1, 10)])  # all cities except the depot

def calculate_tour_metrics(tour):
    # Include the depot city at the start and the end
    tour_with_depot = [0] + list(tour) + [0]
    total_cost = 0
    max_distance = 0

    # Calculate the total cost and max distance between consecutive cities
    for i in range(len(tour_with_depot) - 1):
        distance = euclidean_divisor.set(cities[tour_with_depot[i]], cities[tour_with_depot[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    return tour_with_depot, total_cost, max_distance

# Searching for the optimal tour minimizing the maximum distance between consecutive cities
optimal_tour = None
optimal_cost = float('inf')
optimal_max_distance = float('inf')

for tour in all_tours:
    tour_with_depot, cost, max_dist = calculate_tour_metrics(tour)
    if max_dist < optimal_max_distance:
        optimal_max_distance = max_dist
        optimal_cost = cost
        optimal_tour = tour_with_depot

# Output the optimal solution found
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")
print(f"Maximum distance between consecutive cities: {optimal_max_distance}")