import math
import numpy as np
import random
from itertools import permutations

# Calculate Euclidean distance
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Initialize cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16:(38, 46), 17: (61, 33), 
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Total number of robots
num_robots = 8

# All robots starting from depot 0
initial_city = 0

# Function to generate initial solution
def initial_solution(num_robots, cities, initial_city):
    all_cities = list(cities.keys())
    all_cities.remove(initial_city)
    random.shuffle(all_cities)
    split_size = len(all_cities) // num_robots
    tours = [all_cities[i:i + split_size] for i in range(0, len(all_cities), split_size)]
    for tour in tours:
        tour.insert(0, initial_city)
        tour.append(initial_city)
    return tours[:num_robots]

# Calculate total travel cost of a tour
def tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Tabu search definitions
def tabu_search(tours, cities, iterations=500, tabu_tenure=10):
    best_solution = tours
    best_costs = [tour_cost(tour, cities) for tour in tours]
    best_total_cost = sum(best_costs)
    tabu_list = {}

    for iteration in range(iterations):
        neighborhood = []

        # Generate neighborhood by 2-opt swap
        for idx, tour in enumerate(tours):
            for i in range(1, len(tour) - 2):
                for j in range(i + 1, len(tour) - 1):
                    if j - i == 1: continue
                    new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                    new_cost = tour_cost(new_tour, cities)
                    neighborhood.append((new_tour, new_cost, idx))

        # Select the best candidate from the neighborhood that isn't tabu or is better than the current best
        neighborhood.sort(key=lambda x: x[1])
        for new_tour, new_cost, idx in neighborhood:
            if (tuple(tours[idx]), tuple(new_tour)) not in tabu_list or new_cost < best_costs[idx]:
                tours[idx] = new_tour
                tabu_list[(tuple(new_tour), tuple(tours[idx]))] = iteration + tabu_tenure
                best_costs[idx] = new_cost
                break

        # Clean the tabu_list
        to_del = [key for key, val in tabu_list.items() if val < iteration]
        for key in to_del:
            del tabu_list[key]

        current_total_cost = sum(best_costs)
        if current_total_cost < best_total_cost:
            best_solution, best_total_cost = tours, current_total_cost

    return best_solution, best_costs, best_total_cost

# Run Tabu Search
initial_tours = initial_solution(num_robots, cities, initial_city)
final_tours, final_costs, final_total_cost = tabu_search(initial_tours, cities)

# Print results
print("Optimal tours and costs:")
for i, tour in enumerate(final_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {final_costs[i]}")
print(f"Overall Total Travel Cost: {final_total_cost}")