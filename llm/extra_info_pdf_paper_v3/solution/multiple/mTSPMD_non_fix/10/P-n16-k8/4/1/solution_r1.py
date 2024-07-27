import math
import random

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Initial function to calculate the euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Simulated Annealing for solving TSP for one robot
def simulated_annealing(tour):
    temperature = 10000
    cooling_rate = 0.995
    min_temperature = 1

    current_solution = tour[:]
    current_cost = sum(distance(current_solution[i], current_solution[i+1]) for i in range(len(current_solution) - 1))

    while temperature > min_temperature:
        new_solution = current_solution[:]
        l = random.randint(1, len(new_solution) - 3)
        h = random.randint(l + 1, len(new_solution) - 2)
        new_solution[l:h] = reversed(new_solution[l:h])

        new_cost = sum(distance(new_solution[i], new_solution[i+1]) for i in range(len(new_solution) - 1))
        if new_cost < current_cost or math.exp((current_cost - new_cost) / temperature) > random.random():
            current_solution = new_solution
            current_cost = new_cost

        temperature *= cooling_rate

    return (current_solution, current_cost)

# Generate a random initial solution
def generate_initial_solution():
    cities_list = list(cities.keys())
    random.shuffle(cities_list)
    solutions = [cities_list[i:i + 2] for i in range(0, len(cities_list), 2)]  # Sampling cities in pairs
    return solutions

# Running the optimization for each robot
solutions = generate_initial_solution()
results = [simulated_annealing(tour+[tour[0]]) for tour in solutions]  # Ensuring it returns to the start depot

# Display the results
total_cost = 0
for index, result in enumerate(results):
    print(f"Robot {index} Tour: {result[0]}")
    print(f"Robot {index} Travel Cost: {result[1]:.2f}")
    total_cost += result[1]

print(f"Overall Total Travel Cost: {total_cost:.2f}")