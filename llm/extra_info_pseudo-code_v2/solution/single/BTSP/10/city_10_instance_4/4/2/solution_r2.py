import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

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

# Calculate distances between each pair of cities
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Function to calculate the cost of a given tour
def calculate_tour_cost(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Function to calculate the max distance in a given tour
def calculate_max_distance(tour):
    return max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Generate all permutations of the cities (excluding the depot, which is city 0)
city_indices = list(cities.keys())[1:]
all_tours = permutations(city_indices)
best_tour = None
best_cost = float('inf')
best_max_distance = float('inf')

# Evaluate each possible tour and find the one with the minimum maximum distance
for tour in all_tours:
    complete_tour = [0] + list(tour) + [0]
    total_cost = calculate_tour_cost(complete_tour)
    max_distance = calculate_max_distance(complete_tour)
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_cost = total_cost
        best_tour = complete_tour

# Output the best found solution
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
print("Maximum distance between consecutive cities:", best_max_distance)