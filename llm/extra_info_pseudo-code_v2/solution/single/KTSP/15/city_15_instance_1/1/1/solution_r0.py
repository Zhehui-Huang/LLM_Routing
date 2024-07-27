import random
import math
from itertools import permutations

# Coordinates of cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to compute the total cost of a tour
def compute_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# GenerateInitialSolution function
def generate_initial_solution(k):
    tour = [0]  # start at the depot city 0
    available_cities = list(cities.keys())[1:]  # exclude the depot city
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0)  # end at the depot
    return tour

# Generate all possible tours of k cities including the depot
def get_all_possible_tours(k):
    tours = []
    for combo in permutations(list(cities.keys())[1:], k-1):
        tour = [0] + list(combo) + [0]
        tours.append(tour)
    return tours

# Find the shortest tour using total brute force (for small k)
def find_shortest_tour(k):
    all_tours = get_all_possible_tours(k)
    best_tour = None
    min_cost = float('inf')
    for tour in all_tours:
        cost = compute_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Here we use k=6 as we include 5 other cities plus the depot
best_tour, total_cost = find_shortest_tour(6)
print("Tour:", best_tour)
print("Total travel cost:", total_cost)