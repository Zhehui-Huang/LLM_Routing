import math
import random

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to compute the total cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate an initial feasible solution
def generate_initial_solution(k=6):
    available_cities = list(cities.keys())[1:]  # exclude the depot initially
    selected_cities = random.sample(available_cities, k-1)
    solution = [0] + selected_cities + [0]  # start and end at depot
    return solution

# Shake the solution to generate a new neighborhood
def shake(solution):
    middle = solution[1:-1]  # Exclude the depot for modifications
    random.shuffle(middle)
    return [solution[0]] + middle + [solution[-1]]

# Improve the solution using a simple swap-based local search
def local_search(solution):
    best_cost = tour_cost(solution)
    best_solution = solution[:]
    for i in range(1, len(solution) - 2):
        for j in range(i+1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = tour_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
    return best_solution

# Perform the General Variable Neighborhood Search
def gvns(itermax=1000, k=6):
    best_solution = generate_initial_solution(k)
    best_cost = tour_cost(best_solution)
    for _ in range(itermax):
        current_solution = shake(best_solution)
        current_solution = local_search(current_comment_solution)
        current_cost = tour_cost(current_solution)
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
    return best_solution, best_cost

# Running GVNS to solve the problem
final_solution, final_cost = gvns()
print("Tour:", final_solution)
print("Total travel cost:", final_cost)