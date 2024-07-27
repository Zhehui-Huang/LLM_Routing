import itertools
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x11)**2 + (y2 - y1)**2)

# Cities coordinates
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

# Generate all combinations of 4 cities (since including the depot, it makes 5 visits)
city_indices = list(range(1, 10))  # Excluding the depot which is always included
combinations = itertools.combinations(city_indices, 4)

# Function to calculate the total travel cost of the tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

# Finding the optimal tour
best_tour = None
min_cost = float('inf')

for combo in combinations:
    # Create a tour starting and ending at the depot (0)
    tour = [0] + list(combo) + [0]
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")