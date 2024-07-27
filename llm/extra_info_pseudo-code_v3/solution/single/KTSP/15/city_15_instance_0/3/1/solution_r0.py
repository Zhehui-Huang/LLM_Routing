import math
import random

# Calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial random solution, with the depot always being the first and last city
def generate_initial_solution(cities, depot, k):
    selected_cities = random.sample(cities[1:], k-1)  # exclude depot and sample k-1 cities
    tour = [depot] + selected_cities + [depot]
    return tour

# Calculate the total tour distance
def calculate_tour_cost(tour, distances):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distances[tour[i]][tour[i+1]]
    return total_cost

# Shaking: Generate a new solution by swapping two cities in the tour
def shake(tour):
    new_tour = tour[1:-1]  # exclude depots at start and end for swapping
    a, b = random.sample(range(len(new_tour)), 2)
    new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
    return [tour[0]] + new_tour + [tour[0]]

# Variable Neighborhood Descent (VND) - Iterate through neighborhoods N1 and N2
def VND(tour, distances):
    improved = True
    while improved:
        improved = False
        # Checking all swaps for improvement
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = calculate_tour_cost(new_tour, distances)
                if new_cost < calculate_tour_cost(tour, distances):
                    tour = new_tour
                    improved = True
    return tour

# Main GVNS implementation
def GVNS(cities, k, nrst, max_iterations):
    depot = cities[0]
    best_tour = None
    best_cost = float('inf')
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

    for _ in range(nrst):
        # Initial solution
        tour = generate_initial_solution(cities, depot, k)
        tour_cost = calculate_tour_cost(tour, distances)
        
        # Main loop
        iterations = 0
        while iterations < max_iterations:
            new_tour = shake(tour)
            improved_tour = VND(new_tour, distances)
            improved_cost = calculate_tour_cost(improved_tour, distances)
            
            if improved_cost < tour_cost:
                tour = improved_tour
                tour_cost = improved_cost
                iterations = 0  # reset if improvement
            else:
                iterations += 1
        
        if tour_cost < best_cost:
            best_tour = tour
            best_cost = tour_libcost

    return best_tour, best_cost

# Define the cities with their coordinates
cities = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Configuration
k = 4
nrst = 20  # Number of restarts
max_iterations = 100  # Maximum number iterations without improvement

# Execute GVNS
best_tour, best_cost = GVNS(cities, k, nrst, max_iterations)
print(f"Tour: {best_tonur})
print(f"Total travel cost: {best_cost}")