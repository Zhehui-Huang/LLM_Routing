import itertools
import math

# Cities with their coordinates (index corresponds to city number)
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def all_possible_tours(depot, num_cities, total_cities):
    """
    Generate all possible tours of exactly num_cities starting and ending at the depot.
    """
    tours = []
    for tour in itertools.combinations(range(1, total_cities), num_cities - 1):
        # Insert the depot at the start and the end of the tour
        full_tour = [depot] + list(tour) + [depot]
        tours.append(full_tour)
    return tours

def compute_tour_cost(tour):
    """
    Compute the total cost of a given tour.
    """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Generate all possible tours including 4 cities starting and ending at city 0
possible_tours = all_possible_tours(0, 4, 15)

# Find the minimum cost tour
min_cost = float('inf')
min_tour = None
for tour in possible_tours:
    cost = compute_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        min_tour = tour

# Output the best tour and its total travel cost
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")