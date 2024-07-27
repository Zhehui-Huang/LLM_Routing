import random
import math

# Location data for the cities
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Function to calculate the Euclidean distance between cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate an initial route by selecting k cities randomly, ensuring start and end at the depot city 0
def generate_initial_solution(k):
    selected_cities = random.sample([c for c in cities if c != 0], k - 2)
    route = [0] + selected_cities + [0]
    return route

# Shake function: Random mutation on the selected cities
def shake(solution, k):
    inner_cities = solution[1:-1]  # all cities except the depot
    random.shuffle(inner_cities)
    return [0] + inner_cities[:k-2] + [0]

# Variable Neighborhood Descent (Local Search Improvement)
def local_search(solution):
    best_route = solution[:]
    best_cost = path_cost(solution)
    
    for i in range(1, len(solution) - 2):
        for j in range(i+1, len(solution) - 1):
            new_route = solution[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]  # Swap two cities
            new_cost = path_cost(new_route)
            if new_cost < best_cost:
                best_route = new_route
                best_cost = new_skill_cost
                break
    
    return best_route

# Calculate total travel cost for the route
def path_cost(route):
    return sum(calc_distance(route[i], route[i+1]) for i in range(len(route) - 1))

# General Variable Neighborhood Search algorithm
def GVNS(itermax, pmax, k):
    current_solution = generate_initial_solution(k)
    best_solution = current_solution[:]
    best_cost = path_cost(best_solution)
    
    for _ in range(itermax):
        for p in range(1, pmax + 1):
            shaken_solution = shake(best_solution, k)
            improved_solution = local_search(shaken_solution)
            improved_cost = path_cost(improved_solution)
            
            if improved_cost < best_cost:
                best_solution = improved_solution
                best_cost = improved_cost
                break  # Exit the loop early as we found a better solution
    
    return best_solution, best_cost

# Settings
itermax = 1000
pmax = 3
k = 8

# Execution
best_tour, total_cost = GVNS(itermax, pmax, k)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")