import math
from itertools import permutations

# Provided city coordinates
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

# Function to calculate Euclidean distance between two cities
def dist(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to calculate the total travel cost of a tour
def total_cost(tour):
    return sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Function to generate all possible tours visiting exactly k cities out of the given cities,
# starting and ending at the depot city 0.
def k_tsp_tours(k):
    best_tour = None
    best_cost = float('inf')

    # Exclude depot city and generate all possible combinations of k-1 other cities because depot will be start and end
    for subset in permutations([city for city in cities if city != 0], k - 1):
        current_tour = [0] + list(subset) + [0]  # Start and end at the depot
        cost = total_cost(current_tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = current_tour

    return best_tour, best_cost

# Seeking the shortest possible tour that visits exactly 8 cities (including depot)
optimal_tour, min_cost = k_tsp_tours(8)

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_cost}")