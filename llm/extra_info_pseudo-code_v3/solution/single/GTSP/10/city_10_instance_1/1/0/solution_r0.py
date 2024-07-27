import itertools
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities coordinates indexed by city number
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

# Groups of city indices
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Generate all possible selections of cities, taking one from each group
possible_city_selections = list(itertools.product(*groups))

# Function to compute total tour cost given a sequence of city indices
def compute_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Iterate over each possible selection and compute the tours
best_tour = None
min_cost = float('inf')

for selection in possible_city_selections:
    # Build the sequence of cities starting and ending at the depot
    tour = [0] + list(selection) + [0]
    cost = compute_total_cost(tour)
    
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)