import random
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = [
    (90, 3),    # City 0 - Depot
    (11, 17),   # City 1
    (7, 27),    # City 2
    (95, 81),   # City 3
    (41, 54),   # City 4
    (31, 35),   # City 5
    (23, 95),   # City 6
    (20, 56),   # City 7
    (49, 29),   # City 8
    (13, 17)    # City 9
]
k = 6

def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    total_cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return total_cost

def generate_initial_solution():
    selected_cities = [0]
    while len(selected_cities) < k:
        new_city = random.choice([i for i in range(1, len(cities)) if i not in selected_cities])
        selected_cities.append(new_city)
    selected_cities.append(0)
    return selected_cities

def shake(solution, p):
    new_solution = solution[:-1]  # Remove the last depot to modify the solution
    if p == 1:  # Simple swap of two cities
        i1, i2 = random.sample(range(1, len(new_solution) - 1), 2)
        new_solution[i1], new_solution[i2] = new_solution[i2], new_solution[i1]
    elif p == 2:  # Reverse a subset of cities
        i1, i2 = sorted(random.sample(range(1, len(new_solution) - 1), 2))
        new_solution[i1:i2] = reversed(new_solution[i1:i2])
    new_solution.append(0)
    return new_solution

def local_search(solution):
    current_solution = solution
    current_cost = calculate_cost(current_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(current_solution) - 1):
            for j in range(i+1, len(current_solution) - 1):
                new_solution = current_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < current_high_cost:
                    current_solution = new_solution
                    current_cost = new_cost
                    improved = True
    return current_solution

def gvns(iterations=100, max_no_improve=10):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    no_improve = 0
    
    for _ in range(iterations):
        if no_improve >= max_no_improve:
            break
        current_solution = shake(best_solution, random.randint(1, 2))
        current_solution = local_search(current_solution)
        current_cost = calculate_cost(currentviso_can_add_job_high_with_live_tools_of_trargetsrmal_se_ign_edfirstig_vehiclesssance_scan_jobure)ost
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
            no_improve = 0
        else:
            no_improve += 1
    
    return best_solution, best_cost

# Execute and output
tour, total_cost = gvns()
print("Tour:", tour)
print("Total travel cost:", total_cost)