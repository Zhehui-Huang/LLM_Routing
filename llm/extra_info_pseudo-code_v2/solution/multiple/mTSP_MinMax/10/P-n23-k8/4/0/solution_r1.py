import math
import random

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Calculate distances between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate initial feasible solution
def initial_solution():
    ordered_cities = sorted(list(cities.keys())[1:], key=lambda x: calculate_distance(0, x))
    tours = [[] for _ in range(num_robots)]
    for index, city in enumerate(ordered_cities):
        tours[index % num_robots].append(city)
    return tours

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = calculate_distance(0, tour[0]) + calculate_distance(tour[-1], 0)
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i + 1])
    return cost

# Perform the shaking procedure
def shake(tours, k):
    for _ in range(k):
        tour_from = random.randint(0, num_robots - 1)
        if not tours[tour_from]:
            continue
        tour_to = random.randint(0, num_robots - 1)
        while tour_from == tour_to:
            tour_to = random.randint(0, num_robots - 1)
        city = random.choice(tours[tour_from])
        tours[tour_from].remove(city)
        tours[tour_to].append(city)
    return tours

# Main Variable Neighborhood Search
def variable_neighborhood_search(max_iterations=1000, k_max=10):
    tours = initial_solution()
    best_solution = tours
    best_cost = max([calculate_tour_cost(tour) for tour in tours])
    
    iterations = 0
    while iterations < max_iterations:
        k = 1
        while k <= k_max:
            new_tours = shake(tours, k)
            new_cost = max([calculate_tour_cost(tour) for tour in new_tours])
            if new_cost < best_cost:
                best_solution, best_cost = new_tours, new_cost
                k = 1  # Reset k if improvement found
            else:
                k += 1
        iterations += 1
    return best_solution, best_cost

# Calculate solution
best_tours, min_max_cost = variable_neighborhood_search()

# Output final tours and their travel costs
for i, tour in enumerate(best_tours):
    full_tour = [0] + tour + [0]
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {i} Tour: {full_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Travel Cost: {min_max_cost}")