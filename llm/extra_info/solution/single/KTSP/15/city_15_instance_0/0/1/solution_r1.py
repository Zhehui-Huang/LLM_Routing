import itertools
import math

# Define the coordinates for the depot and cities
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

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find all possible tours starting and ending at city 0 and visiting exactly 3 other cities
min_cost = float('inf')
best_tour = []

for tour in itertools.combinations(range(1, 15), 3):  # Choose 3 cities apart from the depot
    full_tour = [0] + list(tour) + [0]  # Form the full tour starting and ending at the depot 0
    # Calculate the travel cost for the current tour
    cost = sum(distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))
    
    # Update the best tour if the current one has a lower cost
    if cost < min_cost:
        min_cost = cost
        best_tour = full_tour

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")