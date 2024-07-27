import random
from math import sqrt, inf

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), 
    (18, 61), (40, 57), (57, 30), (36, 12),
    (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

def generate_initial_solution():
    selected_cities = [0] + random.sample(range(1, 15), 5)
    selected_cities.append(0)
    return selected_cities

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def shake(solution, k):
    new_solution = solution[1:-1]  # remove depot start and end
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

def local_search(solution):
    best_cost = calculate_total_cost(solution)
    best_solution = solution
    for i in range(1, len(solution) - 2):
        for j in range(i+1, len(solution) - 1):
            if i != j:
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
    return best_solution

def VND(solution):
    return local_search(solution)

def gvns(max_iters):
    solution = generate_initial_solution()
    best_solution = solution
    best_cost = calculate_total_path(solution)
    
    for _ in range(max_iters):
        shaken_solution = shake(solution, 1)
        new_solution = VND(shaken_solution)
        new_cost = calculate_total_cost(new_solution)
        
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost
            solution = best_solution  # reset the base solution for new shakings
        else:
            break  # early termination if no improvement

    return best_solution, best_cost

# Execute the algorithm
final_solution, final_cost = gvns(100)
print("Tour:", final_solution)
print("Total travel cost:", final_cost)