import itertools
import math
from typing import List, Tuple, Dict

# Define city locations including the depot city
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36),  3: (15, 0),  4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2),   8: (47, 50), 9: (60, 29),
   10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
   15: (19, 25), 16: (75, 9),  17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def calculate_distance(city1: int, city2: int) -> float:
    """Compute Euclidean distance between two cities based on their indices."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_tour_cost(tour: List[int]) -> float:
    """Calculate the total cost of a given tour."""
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def find_shortest_tour():
    """Find the shortest tour visiting exactly 16 cities starting and ending at the depot."""
    all_cities = list(cities.keys())
    min_cost = float('inf')
    best_tour = []

    # Generate all combinations of 15 cities (beside the depot city)
    for subset in itertools.combinations(all_cities[1:], 15):
        # Include the depot city and form the tour
        current_tour = [0] + list(subset) + [0]
        cost = total_tour_cost(current_tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour

    return best_tour, min_cost

# Running the tour finding function
tour, cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", cost)