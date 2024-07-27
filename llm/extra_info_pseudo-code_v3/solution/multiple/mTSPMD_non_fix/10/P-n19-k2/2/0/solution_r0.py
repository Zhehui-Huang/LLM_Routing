import math
import random
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

num_robots = 2
depots = [0, 1]

def calculate_total_cost(tour):
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return tour_cost
    
def nearest_neighborhood_solution():
    tours = [[] for _ in range(num_robots)]
    remaining_cities = list(range(2, len(cities)))  # Excluding depot cities
    
    # Start each tour from a depot
    for i in range(num_robots):
        tours[i].append(depots[i])

    # Allocate cities to tours
    while remaining_cities:
        for tour in tours:
            if not remaining_cities:
                break
            nearest_city_index = min(remaining_cities, key=lambda x: euclidean_distance(cities[tour[-1]], cities[x]))
            tour.append(nearest_city_index)
            remaining_cities.remove(nearest_city_index)

    return tours

# Generate initial solution
tours = nearest_neighborhood_solution()

# Initial Tabu list configuration and parameters
tabu_list = []
tabu_tenure = 10
max_iterations = 100
max_consecutive_nonimprovements = 50
best_solution = tours
best_cost = sum(calculate_total_cost(tour) for tour in tours)
consecutive_nonimprovements = 0

def is_tabu(move):
    return move in tabu_list

def make_move(tours, move):
    # Details of the move need to be implemented based on the problem and move type
    # Placeholder for real make_move function
    pass

for iteration in range(max_iterations):
    if consecutive_nonimprovements > max_consecutive_nonimprovements:
        break
    move = None  # Determine the best move
    if move and not is_tabu(move):
        make_move(tours, move)
        # Update Tabu list
        tabu_list.append(move)
        if len(tabu_list) > tabu_tenure:
            tabu_list.pop(0)
    else:
        consecutive_nonimprovements += 1

# Outputting the result
tour_costs = [calculate_total_cost(tour) for tour in tours]
overall_cost = sum(tour_costs)

print("Tours and Costs for Robots:")
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")
print(f"Overall Total Travel Cost: {overall_cost}")