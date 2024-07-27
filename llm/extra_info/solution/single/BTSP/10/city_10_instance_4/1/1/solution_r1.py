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
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate all possible tours starting and ending at 0
all_tours = permutations([i for i in range(1, 10)])  # possible tours excluding the depot

def calculate_tour_metrics(tour):
    tour_with_depot = [0] + list(tour) + [0]  # adding the depot at the start and end
    total_cost = 0
    max_distance = 0
    distances = []

    for i in range(len(tour_with_depot) - 1):
        distance = euclidean_distance(cities[tour_with_depot[i]], cities[tour_with_depot[i + 1]])
        distances.append(distance)
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    return tour_with_depot, total_cost, max_distance

# Search for the optimal tour minimizing the maximum distance between consecutive cities
optimal_tour = None
optimal_cost = float('inf')
optimal_max_distance = float('inf')

for tour in all_tours:
    tour_with_depot, cost, max_dist = calculate_tour_metrics(tour)
    if max_dist < optimal_maxn_distance:
        optimal_max_distance = max_dist
        optimal_cost = cost
        optimal_tour = tour_with_depot

# Output the optimal solution found
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {round(optimal_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(optimal_max_distance, 2)}")