import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Parameters
num_robots = 8
start_city = 0

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    return cost

def simulated_annealing(solution):
    temp = 1000
    alpha = 0.995
    min_temp = 0.01

    current_solution = solution[:]
    best_solution = solution[:]
    best_cost = total_tour_cost(best_solution)

    while temp > min_temp:
        i, j = sorted(random.sample(range(1, len(current_solution) - 1), 2))
        new_solution = current_solution[:]
        new_solution[i:j] = reversed(new_solution[i:j])

        current_cost = total_tour_cost(current_solution)
        new_cost = total_tour_cost(new_solution)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_solution = new_solution[:]
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
        
        temp *= alpha

    return best_solution, best_cost

# Initialize solution by dividing cities among robots
initial_solution = list(range(1, len(cities)))
random.shuffle(initial_solution)
solutions = [initial_solution[i::num_robots] for i in range(num_robots)]
for i in range(num_robots):
    solutions[i].insert(0, start_city)
    solutions[i].append(start_city)  # Append the starting depot at the end for the tour

optimized_tours = []
total_costs = []

for solution in solutions:
    optimized_tour, tour_cost = simulated_annealing(solution)
    optimized_tours.append(optimized_tour)
    total_costs.append(tour_cost)

# Output the results
overall_total_cost = sum(total_costs)
for robot_id, tour in enumerate(optimized_tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")