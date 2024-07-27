import math
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Total number of robots
num_robots = 8

# All robots start at depot 0
depot = 0

# Initial tour solution: A simple greedy approach to generate an initial feasible solution
def initial_solution(depot, num_robots):
    available_cities = list(cities.keys())
    available_cities.remove(depot)

    tours = [[depot] for _ in range(num_robots)]
    for i in range(len(available_cities)):
        tours[i % num_robots].append(available_cities[i])

    for tour in tours:
        tour.append(depot)  # Close the tour for initial evaluation; It will be handled based on problem statement next.

    return tours

# Simulated Annealing to optimize the tours
def simulated_annealing(tours):
    initial_temp = 1000
    final_temp = 1
    alpha = 0.99
    current_temp = initial_temp

    current_tours = tours
    best_tours = tours
    best_cost = calculate_total_cost(tours)

    def swap_cities(tour):
        new_tour = tour[:]
        i, j = random.sample(range(1, len(tour) - 1), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        return new_tour

    while current_temp > final_temp:
        new_tours = [swap_cities(t) for t in current_tours]
        new_cost = calculate_total_cost(new_tours)
        if new_cost < best_cost or random.uniform(0, 1) < math.exp((calculate_total_cost(current_tours) - new_cost) / current_temp):
            current_tours = new_tours
            if new_cost < best_cost:
                best_cost = new_cost
                best_tours = new_tours

        current_temp *= alpha

    return best_tours

# Calculate the total cost for a set of tours
def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        total_cost += tour_cost
    return total_cost

# Generate the initial solution and optimize
initial_tours = initial_solution(depot, num_robots)
optimized_tours = simulated_annealing(initial_tours)
total_cost = calculate_total_cost(optimized_tours)

# Print results
for idx, tour in enumerate(optimized_tours):
    tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")