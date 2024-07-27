import math
import random

# Coordinates of the 19 cities including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots, implicitly determining assigned depots
depots = [0, 1]
num_robots = len(depots)

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initial solution generator
def generate_initial_solution():
    # Full list of cities without depots 
    all_cities = list(cities.keys())
    random.shuffle(all_cities)
    # Splitting somewhat equally among robots
    division = len(all_cities) // num_robots
    solutions = [all_cities[i * division:(i + 1) * division] for i in range(num_robots)]
    for i in range(num_robots):
        solutions[i].insert(0, depots[i])
        solutions[i].append(depots[i])  # End at their starting depot
    return solutions

# Cost calculator for one tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Simulated Annealing process for traveling salesman problem
def simulated_annealing(solution, initial_temperature=1000, cooling_rate=0.995, num_iterations=1000):
    current_temp = initial_temperature
    current_solution = solution
    current_cost = [calculate_tour_cost(tour) for tour in current_solution]

    while current_temp > 1:
        for _ in range(num_iterations):
            new_solution = [tour[:] for tour in current_solution]
            # Modify the tour of each robot
            for idx in range(num_robots):
                if len(new_solution[idx]) > 3:  # Needs at least two cities to make a swap
                    i, j = random.sample(range(1, len(new_solution[idx])-1), 2)
                    new_solution[idx][i], new_solution[idx][j] = new_solution[idx][j], new_solution[idx][i]
            
            new_cost = [calculate_tour_cost(tour) for tour in new_solution]
            cost_difference = sum(new_cost) - sum(current_cost)
            if cost_difference < 0 or math.exp(-cost_difference / current_temp) > random.random():
                current_solution, current_cost = new_solution, new_cost
        
        current_temp *= cooling_rate
    
    return current_solution, current_cost

# Generating an initial solution and executing the simulated annealing algorithm
initial_solution = generate_initial_solution()
final_solution, final_costs = simulated_annealing(initial_solution)

# Summarizing the results
overall_cost = sum(final_costs)

for i in range(num_robots):
    print(f"Robot {i} Tour: {final_solution[i]}")
    print(f"Robot {i} Total Travel Cost: {final_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")