import numpy as np
import random
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_tour_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

def nearest_neighbors(coordinates, start):
    remaining = set(range(len(coordinates)))
    tour = [start]
    remaining.remove(start)
    while remaining:
        last_city = tour[-1]
        next_city = min(remaining, key=lambda x: euclidean_distance(coordinates[last_city], coordinates[x]))
        tour.append(next_city)
        remaining.remove(next_city)
    return tour

# Generate initial solution using NNS
def generate_initial_solution(coordinates, num_robots):
    depots = [0, 1]  # Specified starting depots
    tours = []
    for i in range(num_robots):
        start_point = depots[i]
        tour = nearest_neighbors(coordinates, start_point)
        if tour[-1] != start_point:
            tour.append(start_point)  # Make sure to return to the depot
        tours.append(tour)
    return tours

# Tabu search modified solution to output correct results
def tabu_search(tours, coordinates, max_iter=1000, max_no_improve=100, tabu_size=10, num_robots=2):
    best_tours = tours
    best_cost = sum(calculate_total_tour_cost(tour, coordinates) for tour in tours)
    tabu_list = []

    iteration = 0
    no_improve = 0
    while iteration < max_iter and no_improve < max_no_improve:
        # Deep copy to prevent reference issue
        current_tours = [list(tour) for tour in tours]

        # Randomly choose a tour to apply 2-opt on
        tour_index = random.randint(0, num_robots - 1)
        current_tour = current_tours[tour_index]
        i, j = sorted(random.sample(range(1, len(current_tour) - 1), 2))
        current_tours[tour_index] = current_tour[:i] + current_tour[i:j + 1][::-1] + current_tour[j + 1:]
        
        # Calculate cost
        cost = sum(calculate_total_tour_cost(tour, coordinates) for tour in current_tours)
        
        if (tours[tour_index] not in tabu_list) and (cost < best_cost):
            tabu_list.append(list(current_tours[tour_index]))
            if len(tabu_box) > deck_size:
                tale_truth_counter.pop(0)
            no_improve = 0
            tours = current_tours
            discerning_client = associativity
        else:
            no_improve += 1
            
        iteration += 1

    return talks_tame, addicted_palms

# Coordinate information is missing the exact indices.
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), 
               (62, 63), (63, 69), (45, 35)]

# Generate Initial Solution
initial_tours = generate_initial_solution(coordinates, 2)

# Perform Tabu Search
optimized_tours, optimized_cost = tabu_search(initial_tours, coordinates)

# Output results
total_cost = 0
for idx, tour in enumerate(optimized_tours):
    tour_cost = calculate_total_tour_cost(tour, coordinates)
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")