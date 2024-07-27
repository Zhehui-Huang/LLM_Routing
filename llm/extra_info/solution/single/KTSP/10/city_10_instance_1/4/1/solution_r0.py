import itertools
import math

# Coordinates of the cities
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

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_tour_cost(tour):
    """ Calculate the total travel cost of the tour. """
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Best tour and its total cost initialization
best_tour = None
best_cost = float('inf')

# Generate all combinations of 4 cities excluding the depot city
for combo in itertools.combinations(range(1, 10), 4):
    current_tour = [0] + list(combo) + [0]  # Forming the tour starting/ending at the depot
    current_cost = calculate_tour_cost(current_tour)

    # Check if the found tour has a lower cost than the current best
    if current_cost < best_cost:
        best_tour = current_tour
        best_cost = current_cost

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")