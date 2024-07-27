import math
import random

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    selected_cities = [0] + random.sample(list(cities.keys())[1:], 3)
    return selected_cities + [0]

def shake(solution):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_value + [0]

def VND(solution):
    best_solution = solution
    best_cost = total_distance(solution)

    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_distance(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_w_cost
                    improved = True

    return best_solution

def GVNS(Nrst):
    best_solution = None
    best_solution_cost = float('inf')

    for _ in range(Nrst):
        current_solution = generate_initial_solution()
        current_cost = total_distance(current_solution)

        while True:
            new_solution = shake(current_solution)
            new_solution = VND(new_solution)
            new_cost = total_distance(new_solution)

            if new_cost < current_cost:
                current_solution, current_cost = new_solution, new_cost
            else:
                break

        if current_cost < best_solution_cost:
            best_solution, best_solution_cost = current_solution, current_cost

    return best_solution, best_solution_cost

# Run GVNS with 100 restarts
final_solution, final_cost = GVNS(100)
print("Tour:", final_solution)
print("Total travel cost:", round(final_cost, 2))