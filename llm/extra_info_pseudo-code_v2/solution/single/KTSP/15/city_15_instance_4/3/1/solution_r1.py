import random
import math

# Define city coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Parameters
k = 12  # Including the depot city 0
itermax = 100
pmax = 3

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Generate the initial solution
def generate_initial_solution():
    cities = list(range(1, len(coordinates)))
    random.shuffle(cities)
    solution = [0] + cities[:k-1] + [0]
    return solution

# Calculate the total cost of a solution
def total_cost(solution):
    return sum(distance(solution[i], solution[i + 1]) for i in range(len(solution) - 1))

# Local search: Swap two cities
def local_search(solution):
    best_cost = total_cost(solution)
    best_sol = solution.copy()
    for i in range(1, k-1):
        for j in range(i + 1, k):
            solution[i], solution[j] = solution[j], solution[i]
            current_cost = total_cost(solution)
            if current_cost < best_cost:
                best_cost = current_cost
                best_sol = solution.copy()
            solution[i], solution[j] = solution[j], solution[i]
    return best_sol

# Shake function: Randomly swap two cities
def shake(solution, severity):
    shaken_sol = solution.copy()
    for _ in range(severity):
        i, j = random.sample(range(1, k), 2)  # avoid swapping the depot city
        shaken_sol[i], shaken_sol[j] = shaken_sol[j], shaken_sol[i]
    return shaken_sol

# Variable Neighborhood Search
def gvns():
    best_solution = generate_initial_solution()
    best_cost = total_cost(best_solution)
    for iter in range(itermax):
        current_solution = best_solution.copy()
        p = 1
        while p <= pmax:
            shaken_solution = shake(current_solution, p)
            improved_solution = local_search(shaken_solution)
            improved_cost = total_cost(improved_solution)
            if improved_cost < best_cost:
                best_solution, best_cost = improved_solution, improved_cost
                p = 1  # Reset and explore further
            else:
                p += 1
    return best_solution, best_cost

# Run the GVNS algorithm
final_solution, minimum_cost = gvns()

# Output the results
print(f"Tour: {final_solution}")
print(f"Total travel cost: {minimum_cost:.2f}")