import random
import math

# Define the coordinates of the cities
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94),
    18: (51, 58), 19: (30, 48)
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    cities_list = list(cities.keys())
    initial_solution = [0] + random.sample(cities_list[1:], 9) + [0]
    return initial_solution

def shake(solution, k=3):
    internal = solution[1:-1]
    random.shuffle(internal)
    return [0] + internal + [0]

def local_search(solution):
    best_solution = solution[:]
    best_cost = total_distance(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = total_distance(new_solution)
                    if new_cost < best_cost:
                        best_solution = new_solution[:]
                        best_cost = new_cost
                        improved = True
    return best_solution

def vns(solution, max_iterations=100, max_no_improve=10):
    best_solution = solution[:]
    best_cost = total_distance(best_solution)
    iteration = 0
    no_improve_count = 0

    while iteration < max_iterations and no_improve_count < max_no_improve:
        new_solution = shake(best_solution)
        new_solution = local_search(new_solution)
        new_cost = total_distance(new_solution)
        
        if new_cost < best_cost:
            best_solution = new_solution[:]
            best_cost = new_cost
            no_improve_count = 0
        else:
            no_improve_count += 1
        
        iteration += 1

    return best_solution, best_cost

# Running the VNS to find an optimal tour
initial_solution = generate_initial_solution()
final_solution, final_cost = vns(initial_solution)
print("Tour:", final_solution)
print("Total travel cost:", final_cost)