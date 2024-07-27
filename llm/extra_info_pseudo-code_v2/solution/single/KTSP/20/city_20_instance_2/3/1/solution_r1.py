import random
import math

# Define the coordinates of the cities
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94),
    18: (51, 58), 19: (30, 48)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    solution = [0]  # start at the depot
    available_cities = list(cities.keys())[1:]  # exclude the depot for initial selection
    chosen_cities = random.sample(available_cities, 9)  # choose 9 cities randomly
    solution.extend(chosen_cities)
    solution.append(0)  # return to the depot
    return solution

def shake(solution, k):
    new_solution = solution[1:-1]  # exclude the depot city from shaking
    random.shuffle(new_solution)
    return [0] + new_solution[:k] + new_solution[k:] + [0]  # reinsert depot

def local_search(solution):
    best_cost = calculate_total_distance(solution)
    best_sol = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, 10):
            for j in range(i + 1, 10):
                # Create a new candidate solution by swapping two cities
                candidate = solution[:]
                candidate[i], candidate[j] = candidate[j], candidate[i]
                candidate_cost = calculate_total_distance(candidate)
                if candidate_cost < best_cost:
                    best_cost = candidate_cost
                    best_sol = candidate
                    improved = True
    return best_sol

def vns(k_max=10, max_iter=100):
    current_solution = generate_initial_solution()
    current_cost = calculate_total_distance(current_solution)
    for i in range(max_iter):
        k = 1
        while k <= k_max:
            new_solution = shake(current_solution, k)
            new_solution = local_search(new_solution)
            new_cost = calculate_total_distance(new_solution)
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_order_cost
                k = 1  # reset to first neighborhood
            else:
                k += 1
    return current_solution, current_cost

# Find the solution using VNS
optimal_solution, optimal_cost = vns()
print("Tour:", optimal_solution)
print("Total travel cost:", optimal_cost)