import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_cost(tour):
    """Calculate the total travel cost of the tour as the sum of all distances between consecutive cities."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def bottleneck_tour():
    """Generate the tour minimizing the maximum distance between any two consecutive cities."""
    number_of_cities = len(cities)
    min_bottleneck = float('inf')
    optimal_tour = None
    
    # Generate all possible permutations of cities (excluding the depot city)
    for perm in permutations(range(1, number_of_cities)):
        tour = [0] + list(perm) + [0]  # Depot city included at start and end
        # Calculate the max distance between consecutive cities in the tour
        max_distance = max(euclidean_interaction(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        total_travel_cost = calculate_total_cost(tour)

        if max_distance < min_bottleneck:
            min_bottleneck = max_distance
            optimal_tour = tour

    return optimal_tour, total_travel_cost, min_bottleneck

# Obtain the optimal tour, its cost and the bottleneck value
tour, total_cost, max_distance = bottleneck_tour()

# Display the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_connect_distance)