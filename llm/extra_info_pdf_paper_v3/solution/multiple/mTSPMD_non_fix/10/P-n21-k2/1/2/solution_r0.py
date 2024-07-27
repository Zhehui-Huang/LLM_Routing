import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_cost(tours, cities):
    cost = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def create_initial_solution(depot, cities):
    others = [i for i in range(len(cities)) if i != depot]
    random.shuffle(others)
    return [depot] + others + [depot]

def simulated_annealing(depot, cities, temp, temp_min, alpha):
    current_solution = create_initial_solution(depot, cities)
    best_solution = current_solution
    best_cost = calculate_total_cost([best_solution], cities)
    current_cost = best_cost

    while temp > temp_min:
        next_solution = current_solution[:]
        # Swap two cities in the tour, excluding the depot
        idx1, idx2 = random.randint(1, len(next_solution) - 2), random.randint(1, len(next_solution) - 2)
        next_solution[idx1], next_solution[idx2] = next_solution[idx2], next_solution[idx1]
        next_cost = calculate_total_cost([next_solution], cities)

        if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / temp):
            current_solution = next_solution
            current_cost = next_cost
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

        temp *= alpha

    return best_solution, best_cost

# Environment and robot setup from the provided information
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
          (62, 63), (63, 69), (45, 35)]
depots = [0, 1]
robots = 2

# Parameters for Simulated Annealing
initial_temperature = 100
temperature_minimum = 0.01
cooling_rate = 0.99

# Running the simulated annealing for each robot
tours = []
costs = []
for depot in depots:
    tour, cost = simulated_annealing(depot, cities, initial_temperature, temperature_minimum, cooling_rate)
    tours.append(tour)
    costs.append(cost)

overall_cost = sum(costs)

# Display results
for i in range(robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")