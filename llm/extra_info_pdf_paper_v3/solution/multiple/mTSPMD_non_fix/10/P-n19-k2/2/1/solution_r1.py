import random
import math

# Cities' coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial random tour for robots
def generate_initial_solution():
    all_cities = list(range(2, len(cities)))  # cities except the depots
    random.shuffle(all_cities)
    mid_point = len(all_cities) // 2
    return all_cities[:mid_point], all_cities[mid_point:]

# Simulated Annealing for finding optimal tours
def simulated_annealing(initial_solution):
    current_solution = initial_solution
    temp = 10000
    temp_min = 1
    alpha = 0.99

    while temp > temp_min:
        new_solution = get_neighbors(current_solution)
        if calculate_total_cost(new_solution) < calculate_total_cost(current_solution):
            current_solution = new_solution
        temp *= alpha

    return current_solution

# Calculate total cost for a given solution
def calculate_total_cost(solution):
    return (calculate_tour_cost([0] + solution[0] + [0]) + calculate_tour_cost([1] + solution[1] + [1]))

# Calculate cost of a single tour
def calculate_tour_cost(tour):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Create neighboring solutions
def get_neighbors(solution):
    tour1, tour2 = solution
    if random.random() > 0.5:  # Perturb tour1
        i, j = sorted(random.sample(range(len(tour1)), 2))
        tour1[i], tour1[j] = tour1[j], tour1[i]
    else:  # Perturb tour2
        i, j = sorted(random.sample(range(len(tour2)), 2))
        tour2[i], tour2[j] = tour2[j], tour2[i]
    return (tour1, tour2)

initial_solution = generate_initial_solution()
optimized_solution = simulated_annealing(initial_solution)

# Calculate individual costs
cost_robot_0 = calculate_tour_cost([0] + optimized_solution[0] + [0])
cost_robot_1 = calculate_tour_cost([1] + optimized_solution[1] + [1])
total_cost = cost_robot_0 + cost_robot_1

# Output the final tours and costs
print("Robot 0 Tour:", [0] + optimized_solution[0] + [0])
print("Robot 0 Total Travel Cost:", cost_robot_0)
print("Robot 1 Tour:", [1] + optimized_solution[1] + [1])
print("Robot 1 Total Travel Cost:", cost_robot_1)
print("Overall Total Travel Cost:", total_cost)