import itertools
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Data input
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Generate combinations of 7 cities excluding depot (0) to visit (select from cities 1 to 9)
combinations = itertools.combinations(range(1, 10), 7)

# Function to calculate total tour cost for a given path
def calculate_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Find the best tour with the smallest cost
best_tour = None
min_cost = float('inf')

for combination in combinations:
    # Initial tour path (start and end at the depot)
    tour = [0] + list(combination) + [0]

    # Find the best sequence within this combination using a simple 2-opt approach
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < min_cost:
                    best_tour = new_tour
                    min_cost = new_cost
                    improved = True

# Output the results
if best_tour:
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {min_cost:.2f}")
else:
    print("No valid tour was found.")