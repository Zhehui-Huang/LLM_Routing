import itertools
import math

# Cities coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of cities to visit, including the depot
k = 4

# Find all the subsets of three cities excluding the depot city
subsets = list(itertools.combinations(range(1, 20), k - 2))

# Best tour initialization
best_tour = None
best_cost = float('inf')

# For each subset, calculate the tour starting and ending at the depot city
for subset in subsets:
    # Create full route including the depot
    full_tour = [0] + list(subset) + [0]

    # Find all permutations of the chosen cities
    for perm in itertools.permutations(subset):
        current_tour = [0] + list(perm) + [0]
        
        # Calculate the total cost of the current tour
        current_cost = 0
        for i in range(len(current_tour) - 1):
            current_cost += distance(current_tour[i], current_tour[i + 1])
        
        # Check if the current cost is better; if yes, update best cost and tour
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour

# Output tour and cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")