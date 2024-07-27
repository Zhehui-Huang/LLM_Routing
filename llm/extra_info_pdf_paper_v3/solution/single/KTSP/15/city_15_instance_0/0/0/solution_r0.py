import itertools
import math

# City coordinates
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

# Euclidean distance calculation
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Compute the total travel cost for a tour
def total_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i+1])
    return cost

# Finding the shortest tour that visits 4 cities including the depot
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = None

    # Generate all possible combinations of 3 other cities along with depot city 0
    for combination in itertools.combinations(range(1, 15), 3):
        current_tour = [0] + list(combination) + [0]
        # Generate all permutations of the chosen cities to find minimum tour
        for perm_tour in itertools.permutations(current_tour[1:-1]):
            perm_tour = [0] + list(perm_tour) + [0]
            current_cost = total_cost(perm_tour)
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = perm_tour

    return best_tour, min_cost

# Calculate the best tour and its cost
best_tour, min_cost = find_shortest_tour()

# Output formatted as requested
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")