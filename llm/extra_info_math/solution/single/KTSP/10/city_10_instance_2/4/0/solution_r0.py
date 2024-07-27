import math
from itertools import combinations

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to generate all k-combinations of the cities, including the depot city
def generate_city_combinations(k, starting_city=0):
    other_cities = list(cities.keys())
    other_cities.remove(starting_city)
    return [tuple([starting_city] + list(comb)) for comb in combinations(other_cities, k-1)]

# Greedy function to find the shortest tour starting from a combination of cities
def find_greedy_tour(city_set):
    unvisited = list(city_set)
    tour = [unvisited.pop(0)]  # Start from the depot city
    current_city = tour[0]

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(tour[0])  # Return to the starting city
    return tour

# Calculate tour cost based on the given route
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Main algorithm to find the shortest tour visiting exactly k cities
def k_tsp_shortest_tour(k):
    min_cost = float('inf')
    best_tour = None

    for city_comb in generate_city_combinations(k, 0):  # Always include the depot city 0
        tour = find_greedy_tour(list(city_comb))
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_tour, min_cost

# Find the shortest possible tour visiting exactly 6 cities
best_tour, min_cost = k_tsp_shortest_tour(6)
print("Tour:", best_tour)
print("Total travel cost:", min_cost)