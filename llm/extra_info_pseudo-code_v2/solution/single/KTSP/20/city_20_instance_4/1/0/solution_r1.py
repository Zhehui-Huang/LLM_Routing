import random
import math

def distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    cities = list(cities_coordinates.keys())
    selected_cities = random.sample(cities, num_cities_to_visit)
    if 0 not in selected_cities:
        selected_cities[0] = 0
    selected_cities.append(0)  # Making sure to return to the depot
    return selected_cities

def shake(solution, p):
    shaken_solution = solution[1:-1]  # Exclude the depot at start and end
    random.shuffle(shaken_solution)
    return [0] + shaken_solution + [0]

def local_search(solution):
    best_cost = calculate_total_cost(solution)
    best_solution = solution[:]
    improved = False

    for i in range(1, num_cities_to_visit):
        for j in range(i + 1, num_cities_to_visit):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_total_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
                improved = True

    return best_solution, improved

def vnd(solution):
    improved = True
    while improved:
        solution, improved = local_search(solution)
    return solution

def gvns():
    best_solution = generate_initial_old_solution()
    best_cost = calculate_total_cost(best_solution)
    
    for _ in range(itermax):
        current_solution = best_solution[:]
        for p in range(1, pmax+1):
            shaken_solution = shake(current_solution, p)
            improved_solution = vnd(shaken_solution)
            improved_cost = calculate_total_cost(improved_solution)
            if improved_cost < best_cost:
                best_solution = improved_solution[:]
                best_cost = improved_cost

    return best_solution, best_cost

# Running the GVNS algorithm
best_tour, total_cost = gvns()

# Output results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)