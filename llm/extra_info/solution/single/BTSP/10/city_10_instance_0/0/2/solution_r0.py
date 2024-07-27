import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69), 
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_bo[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Compute the distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])
       
# Function to calculate the complete tour cost and maximum leg
def evaluate_tour(tour):
    total_cost = 0
    max_leg = 0
    for i in range(len(tour)-1):
        leg = distances[(tour[i], tour[i+1])]
        total_cost += leg
        if leg > max_leg:
            max_leg = leg
    return total_cost, max_leg

# Generate all possible permutations of the cities (excluding the depot)
city_list = list(cities.keys())[1:]
min_max_leg = float('inf')
best_tour = None

# Generate and evaluate tours
for perm in permutations(city_list):
    tour = [0] + list(perm) + [0]
    _, max_leg = evaluate_tour(tour)
    if max_leg < min_max_leg:
        min_max_leg = max_leg
        best_tour = tour

# If the search completes, best_tour should contain the tour with minimum longest leg
if best_tour:
    tour_total_cost, tour_max_leg = evaluate_tour(best_tour)
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {tour_total_tst:.2f}")
    print(f"Maximum distance between consecutive cities: {tour_max_leg:.2f}")
else:
    print("Failed to find a suitable tour")