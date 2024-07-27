import itertools
import math

# Coordinate of each city, where index represents the city number
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(city_a, city_b):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_best_route():
    min_tour_cost = float('inf')
    best_tour = []

    # Select combinations of 4 cities excluding the depot, since we start and end at depot city 0
    for combo in itertools.combinations(range(1, 10), 4):
        # Create tour by starting and ending at the depot
        current_tour = [0] + list(combo) + [0]

        # Calculate the total cost of the current tour
        tour_cost = 0
        for i in range(len(current_tour) - 1):
            tour_cost += euclidean_distance(current_tour[i], current_tour[i+1])

        # Check if the current tour has a lesser cost than the found solution
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            best_tour = current_tour

    return best_tour, min_tour_cost

best_tour, min_tour_cost = find_best_route()

# Print results
print("Tour:", best_tour)
print("Total travel cost:", min_tour_cost)