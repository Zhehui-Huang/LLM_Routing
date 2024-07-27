import math
import itertools

# Define the cities (index: (x, y) coordinates)
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Nearest neighbor heuristic to generate initial tour
def nearest_neighbor_tour(start, cities):
    unvisited = cities[:]
    tour = [start]
    current_city = start

    while len(unvisited) > 0:
        next_city = min(unvisited, key=lambda city: calc_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # return to the depot
    return tour

# 2-opt swap to try improving the tour
def two_opt(tour, cities):
    min_change = float('inf')
    best_tour = tour[:]
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            if i != 0 or j != len(tour) - 1:
                new_tour = tour[:]
                new_tour[i:j+1] = tour[i:j+1][::-1]
                
                old_cost = calc_distance(cities[tour[i-1]], cities[tour[i]]) + calc_distance(cities[tour[j]], cities[tour[j+1]])
                new_cost = calc_distance(cities[new_tour[i-1]], cities[new_tour[i]]) + calc_distance(cities[new_tour[j]], cities[new_tour[j+1]])
                change = new_cost - old_cost

                if change < min_change:
                    min_change = change
                    best_tour = new_tour

    return best_tour

# Calculate total cost of the tour
def calculate_total_cost(tour, cities):
    return sum(calc_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Initial tour using nearest neighbor
initial_tour = nearest_neighbor_tour(0, range(len(cities)))
improved_tour = two_opt(initial_tour, cities)
total_cost = calculate_total_cost(improved_tour, cities)

# Output result
print("Tour:", improved_tour)
print("Total travel cost:", total_cost)