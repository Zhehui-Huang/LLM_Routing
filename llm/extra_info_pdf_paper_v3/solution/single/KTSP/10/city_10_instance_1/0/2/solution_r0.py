from itertools import combinations
import math

# City coordinates
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

# Function to calculate Euclidean distance
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate all pairwise distances
distances = {
    (i, j): dist(cities[i], cities[j]) for i in cities for j in cities if i != j
}

# Function to evaluate the total travel cost of a tour
def total_cost(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Function to find the shortest path for a given combination of cities
def find_shortest_path(for_cities):
    # Include start and end at the depot city 0
    all_cities = [0] + list(for_cities) + [0]
    # Evaluating total distance of the direct path
    return total_cost(all_cities), all_cities

# Generate all combinations of 4 cities excluding the depot city (total 5 cities with depot)
city_combinations = combinations([c for c in cities if c != 0], 4)

# Search for the shortest tour
min_cost = float('inf')
best_tour = None

for combination in city_combinations:
    cost, tour = find_shortest_path(combination)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best found tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)