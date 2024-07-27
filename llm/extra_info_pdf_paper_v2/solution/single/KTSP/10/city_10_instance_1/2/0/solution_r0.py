import random
import math
from itertools import permutations

# Define the cities coordinates
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
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    """Calculate the total travel cost of the tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def all_possible_tours(depot, total_cities, k):
    """Generate all possible tours starting and ending at the depot, visiting k cities."""
    non_depot_cities = list(total_cities - {depot})
    for cities_subset in permutations(non_depot_cities, k-1):
        tour = [depot] + list(cities_subset) + [depot]
        yield tour

def find_best_tour():
    """Find the best tour that visits exactly 5 cities including the depot, using an exhaustive approach."""
    depot = 0
    all_cities = set(cities.keys())
    best_tour = None
    min_cost = float('inf')
    
    for tour in all_possible_tours(depot, all_cities, 5):
        cost = total_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
            
    return best_tour, min_cost

# Finding the best tour
best_tour, min_cost = find_best_tour()

# Output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")