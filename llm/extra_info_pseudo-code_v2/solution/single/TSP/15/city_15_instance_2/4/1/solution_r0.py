import math
from itertools import permutations

# Define cities coordinates
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

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a function to calculate the total travel cost of a tour
def total_travel_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate an initial tour (greedy approach for simplicity, not part of Lin-Kernighan)
def initial_tour():
    remaining_cities = list(cities.keys())[1:]  # excluding depot initially
    tour = [0]  # start at depot
    current_city = 0
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # return to depot
    return tour

# 2-opt heuristic improvement
def improve_tour(tour):
    improved = True
    best_tour = tour[:]
    best_cost = total_travel_cost(best_tour)
    
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue  # these are consecutive edges and already optimal
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = total_travel_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
        
        tour = best_tour
    
    return best_tour, best_cost

# Find an improved tour from an initial solution
initial_solution = initial_tour()
improved_solution, improved_cost = improve_tour(initial_solution)

# Output the tour and the total travel cost
print(f"Tour: {improved_solution}")
print(f"Total travel cost: {improved_cost:.2f}")