import math
from itertools import permutations

# City coordinates
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
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible routes starting and ending at the depot city 0
def generate_all_tours():
    other_cities = list(cities.keys())[1:]  # all cities except the depot
    all_tours = []
    for perm in permutations(other_cities):
        tour = [0] + list(perm) + [0]
        all_tours.append(tour)
    return all_tours

# Function to calculate the total cost and max distance of a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Task: Minimize the longest distance between any two consecutive cities in the tour
def find_optimal_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    for tour in generate_all_tours():
        total_cost, max_distance = evaluate_tour(tour)
        if max_distance < best_max_distance:
            best_tour = tour
            best_max_distance = max_distance
            best_total_cost = total_cost
        elif max_distance == best_max_distance:
            if total_cost < best_total_cost:
                best_tour = tour
                best_total_cost = total_cost
    
    return best_tour, best_total_cost, best_max_distance

# Find the optimal tour
optimal_tour, optimal_cost, max_consecutive_distance = find_optimal_tour()

# Output the result
print(f"Tour: {optimal_tour}\nTotal travel cost: {optimal_cost: .2f}\nMaximum distance between consecutive cities: {max_consecutive_distance: .2f}")