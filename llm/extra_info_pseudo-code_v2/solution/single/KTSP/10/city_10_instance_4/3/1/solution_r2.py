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

# Generate an initial random solution starting and ending at the depot
def generate_initial_solution(k):
    selected_cities = random.sample(list(cities.keys()), k)
    if 0 not in selected_cities:
        selected_cities.pop()
        selected_cities.insert(0, 0)
    selected_cities.append(0)
    return selected_cities

# Shake the solution by random perturbations
def shake(solution, k):
    core_cities = solution[1:-1]
    random.shuffle(core_cities)
    new_solution = [0] + core_cities[:k-2] + [0]
    return new_solution

# Local search: Swap neighboring cities to find better solutions
def local_search(solution):
    best_route = solution[:]
    best_cost = path_cost(solution)
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(best_route) - 2):
            for j in range(i + 1, len(best_route) - 1):
                new_route = best_route[:]
                new_route[i], new_route[j] = new_route[j], new_route[i]
                new_cost = path_cost(new_route)
                if new_cost < best_cost:
                    best_route = new_route[:]
                    best_cost = new_cost
                    made_improvement = True
    return best_route

# Calculate the cost of the route based on the Euclidean distance
def path_cost(route):
    return sum(calc_distance(route[i], route[i+1]) for i in range(len(route)-1))

# General Variable Neighborhood Search
def GVNS(itermax, pmax, k):
    current_solution = generate_initial_solution(k)
    best_solution = current_solution
    best_cost = path_cost(current_solution)
    
    for _ in range(itermax):
        p = 1
        while p <= pmax:
            shaken_solution = shake(best_solution, k)
            improved_solution = local_search(shaken_solution)
            improved_cost = path_cost(improved_solution)
            if improved_cost < best_cost:
                best_solution = improved_solution
                best_cost = improved_cost
                p = 1
            else:
                p += 1
    return best_solution, best_cost

# Run the GVNS algorithm
k = 8
itermax = 100
pmax = 3
best_tour, total_cost = GVNS(itermax, pmax, k)

print("Tour:", best_tour)
print("Total travel cost:", total_cost)