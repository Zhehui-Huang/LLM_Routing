import random
import math
from itertools import permutations

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_cost(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def initial_tour(cities, groups):
    current_city = 0
    tour = [current_city]
    visited_groups = set()
    while len(visited_groups) < len(groups):
        next_group = min((g for g in range(len(groups)) if g not in visited_groups), key=lambda g: min(distance(cities[current_city], cities[city]) for city in groups[g]))
        next_city = min(groups[next_group], key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(next_city)
        current_city = next_city
        visited_groups.add(next_group)
    tour.append(0)  # Return to depot
    return tour

def two_opt(tour, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue
                if distance(cities[tour[i]], cities[tour[i+1]]) + distance(cities[tour[j-1]], cities[tour[j]]) > distance(cities[tour[i]], cities[tour[j-1]]) + distance(cities[tour[i+1]], cities[tour[j]]):
                    tour[i+1:j] = tour[i+1:j][::-1]
                    improved = True
        if improved:
            break
    return tour

# Configuration
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}
groups = {0: [7, 9], 1: [1, 3], 2: [4, 6], 3: [8], 4: [5], 5: [2]}

# Generate initial tour
tour = initial_tour(cities, groups)
tour = two_opt(tour, cities)
cost = total_cost(tour, cities)

# Print result
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")