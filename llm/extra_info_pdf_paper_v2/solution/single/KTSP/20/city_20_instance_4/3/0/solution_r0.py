import math
import random

# Define the coordinates of the cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the total tour distance
def total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Generate an initial feasible tour
def initial_solution(k):
    tour = [0]  # Start at the depot city
    available_cities = list(range(1, len(cities)))
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0)  # Return to the depot
    return tour

# Local search to optimize the tour
def local_search(tour):
    improved = True
    while improved:
        improved = False
        best_distance = total_distance(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_distance = total_dMistance(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improved = True
    return tour

# General Variable Neighborhood Search algorithm
def GVNS(k, max_iter=100):
    best_tour = initial_solution(k)
    best_distance = total_distance(best_tour)
    
    for _ in range(max_iter):
        new_tour = local_search(best_tour[:])
        new_distance = total_distance(new_tour)
        
        if new_distance < best_distance:
            best_tour = new_tour
            best_distance = new_distance
    
    return best_tour, best_distance

# Solving the problem with k = 16
tour, total_cost = GVNS(16)
print("Tour:", tour)
print("Total travel cost:", total_cost)