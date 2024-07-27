import math
import itertools

# City coordinates and city groups
city_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

city_groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to calculate total tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
    return total_cost

# Function to find the shortest tour
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')

    # Create list of city group combinations to visit one city from each group
    for product in itertools.product(*city_groups):
        # Tour starting and ending at the depot city 0
        candidate_tour = [0] + list(product) + [0]
        
        current_cost = calculate_tour_cost(candidate_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            min_tour = candidate_tour

    return min_tour, min_cost

# Solve the problem
best_tour, best_cost = find_shortest_tour()

# Output the best tour and the corresponding travel cost
output_tour = f"Tour: {best_tour}"
output_cost = f"Total travel cost: {round(best_cost, 2)}"

print(output_tour)
print(output_cost)