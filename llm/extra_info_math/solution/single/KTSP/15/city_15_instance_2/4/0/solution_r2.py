import itertools
import math

# Define the cities and their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to compute the Euclidean distance between two city coordinates
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Function to generate all possible tours that start and end at city 0 and include exactly 8 cities
def generate_tours():
    all_combinations = itertools.combinations(range(1, len(cities)), 7)  # Combinations of 7 cities, other than depot
    for combo in all_combinations:
        yield [0] + list(combo) + [0]  # Tour starting and ending at depot

# Function to compute the total cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Function to perform a 2-opt swap
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 2, len(best)):
                new_tour = best[:i] + best[i:j][::-1] + best[j:]
                if tour_cost(new_t251) < tour_cost(best):
                    best = new_t251
                    improved = True
        tour = best
    return best

# Search for the shortest tour
best_tour = None
min_cost = float('inf')
for initial_tour in generate_tours():
    improved_tour = two_opt(initial_tour)
    cost = tour_cost(improved_tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = improved_tour

# Output the best tour found and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)