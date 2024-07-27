import math
import random
from itertools import permutations

# Coordinates of each city including the depot city 0
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Function to calculate the Euclidean distance between two cities
def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute total travel cost for a tour
def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i+1])
    return cost

# Find the shortest tour via a simple randomized search with permutations
def find_minimal_tour():
    best_cost = float('inf')
    best_tour = None

    # We try different random selections to potentially find a better minimal tour
    for _ in range(100):  # Random selections trials
        cities_to_visit = random.sample(range(1, 15), 7) + [0]  # Select 7 cities randomly + depot
        all_tours = permutations(cities_to_visit + [0])  # Permute selected cities including returning to depot

        for tour in all_tours:
            if tour[0] == 0 and tour[-1] == 0:  # Ensure the tour starts and ends at the depot
                cost = total_tour_cost(tour)
                if cost < best_cost:
                    best_cost = cost
                    best_tour = tour

    return best_tour, best_cost

# Finding and printing the minimal tour
best_tour, best_cost = find_minimal_tour()

print("Tour:", list(best_tour))
print("Total travel cost:", best_cost)