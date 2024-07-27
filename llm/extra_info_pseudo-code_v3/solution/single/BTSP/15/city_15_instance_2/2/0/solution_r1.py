import itertools
import math

# Define the cities' coordinates
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

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible tours that start and end at the depot city 0
def all_tours(cities):
    city_list = list(cities.keys())[1:]  # Exclude the depot from the permutation list
    for perm in itertools.permutations(city_list):
        yield [0] + list(perm) + [0]  # Start and end at the depot

# Calculate the total cost of a tour and the maximum distance between any two consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Find the tour with the minimum maximum distance between consecutive cities
def find_best_tour(cities):
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    for tour in all_tours(cities):
        total_cost, max_distance = evaluate_tour(tour)
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
            best_tour = tour
            best_max_distance = max_distance
            best_total_cost = total_cost
    
    return best_tour, best_total_cost, best_max_as_distance

# Calculate the best tour
best_tour, best_total_cost, best_max_distance = find_best_tour(cities)

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", int(best_total_cost))
print("Maximum distance between consecutive cities:", int(best_max_distance))