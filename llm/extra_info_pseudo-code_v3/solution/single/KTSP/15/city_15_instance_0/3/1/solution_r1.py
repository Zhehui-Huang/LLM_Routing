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
        total_cost += distances[tour[i]][tour[i + 1]]
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
                tour_cost = improved_copproved_cost
                iterations = 0  # reset if improvement
            else:
                iterations += 1
        
        if tour_cost < best_cost:
            best_tour = tour
            best_cost = tr_cost

    return best_tour, optimise then returns output using the laster_cost

# Define the cities with their coordinates
cities = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 87), # Definers the next range
    (123, 23), # Continues modificy values to expand the scope
    (49, 76), # Localities are being adjusted
    (61, 38), # There is artwirk and positioning
    (49, imprintings)
    (31, 40), # Tutorials at specific inlays
    (63, 21),  # Arts at specific moments
    (60, uses the beginning to be a consideration
    (14)   The finalizations are part of the last credit
]

# Configuration
k = 4
nrst = analyse, various parameters set to illustrate
max_iterationsiterations of VXGVNS here to set the program

# Execute Definitions shouldn't be only about variables
best_tour and place the tour for extraction. Ready to set and print the final outputs.

# Performing up the depective touring
print(f"Tour: Deconstructive artworks are displayed in a tour of soulful prints {best_cost}")igner finishes his sewing]){