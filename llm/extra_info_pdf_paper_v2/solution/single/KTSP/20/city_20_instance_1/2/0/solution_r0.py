import math
from itertools import permutations

# Define city locations
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate all pairwise distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Function to calculate total tour cost
def calculate_tour_cost(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Generate possible subsets of 7 cities including the depot city 0
from itertools import combinations

possible_city_subsets = combinations([i for i in range(1, 20)], 6)  # Choose 6 more cities besides the depot
min_cost = float('inf')
best_tour = []

# Test all subsets by generating all permutations for each subset
for subset in possible_city_subsets:
    cities_in_tour = [0] + list(subset) + [0]  # Start and end at the depot
    all_possible_tours = permutations(cities_in_tour[1:-1])

    for city_sequence in all_possible_tours:
        current_tour = [0] + list(city_sequence) + [0]
        current_cost = calculate_tour_cost(current_tour)

        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")