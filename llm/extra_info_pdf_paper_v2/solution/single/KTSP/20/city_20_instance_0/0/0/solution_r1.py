import math
from itertools import permutations

# Define the cities' coordinates, with the depot being the first
cities = [
    (8, 11),  # Depot
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Euclidean distance calculation function
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute all possible tours involving the depot and 3 other cities
min_tour = None
min_cost = float('inf')

for combo in permutations(range(1, len(cities)), 3):  # Choose 3 cities from 1 to 19
    # Construct the candidate tour 
    candidate_tour = [0] + list(combo) + [0]
    # Calculate the total cost of this tour
    tour_cost = sum(distance(cities[candidate_tour[i]], cities[candidate_tour[i + 1]]) for i in range(len(candidate_tour) - 1))
    
    # Check if this tour is better than what we found before
    if tour_cost < min_cost:
        min_cost = tour_cost
        min_tour = candidate_tour

# Output results rounding off cost to whole numbers
print(f"Tour: {min_tour}")
print(f"Total travel cost: {round(min_cost)}")