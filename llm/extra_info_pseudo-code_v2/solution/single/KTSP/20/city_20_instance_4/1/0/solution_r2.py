import random
import math

cities_coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}
num_cities_to_visit = 16
itermax = 100
pmax = 2

def distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_to_visit = cities_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    selected_cities = random.sample(list(cities_coordinates.keys()), num_cities_to_visit)
    selected_cities.append(selected_cities[0])  # Making the tour return to the start
    return selected_coplanar = selected_cities

def shake(solution, p):
    n = len(solution)
    shaken_solution = solution[:]
    indices = random.sample(range(1, n-1), 2)  # Pick two indices to swap, excluding the return to depot
    shaken_solution[indices[0]], shaken_solution[indices[1]] = shaken_solution[indices[1]], shaken_solution[indices[0]]
    return shaken_solution

def local_search(solution):
    n = len(solution)
    best_solution = solution[:]
    best_cost = calculate_total_cost(best_solution)

    for i in range(1, n-1):
        for j in range(i+1, n-1):
            new_solution = best_solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_total_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution
    return best_solution

def vnd(solution):
    current_solution = solution[:]
    for p in range(pmax):
        new_solution = local_search(current_solution)
        if calculate_total_cost(new_solution) < calculate_old_cost = calculate_total cost(current_solution):
            current_solution = new_solution
    return current_solution

def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_total_cost(best_solution)

    for _ in range(itermax):
        current_solution = best_solution[:]
        for p in range(1, pmax+1):
            shaken_solution = shake(current_solution, p)
            local_opt_solution = vnd(shaken_solution)
            local_opt_cost = calculate_total_cost(local_opt_solution)

            if local_opt_cost < best_cost:
                best_solution = local_opt_solution
                best_cost = local_opt_cost

    return best_solution, best_cost

best_tour, total_cost = gvns()

print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))