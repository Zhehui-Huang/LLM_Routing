import random

def generate_initial_solution(cities, k):
    selected_cities = [0]  # start from the depot
    while len(selected_cities) < k:
        candidate = random.choice(list(set(cities) - set(selected_cities)))
        selected_cities.append(candidate)
    selected_cities.append(0)  # return to the depot
    return selected_cities

def shake(solution, k):
    shaken = solution[1:-1]  # exclude the initial and final depot
    random.shuffle(shaken)
    return [solution[0]] + shaken + [solution[0]]  # reintegrating the depot

def local_search(solution):
    best_cost = total_travel_cost(solution)
    best_sol = solution[:]
    
    # Explore all pairs of positions to swap (exclude the depot at start/end)
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # swap
            new_cost = total_travel_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_sol = new_solution[:]
    
    return best_sol

def gvns(k, max_iter, cities):
    pmax = 2  # maximum number of neighborhoods explored
    current_solution = generate_initial_solution(cities, k)
    best_cost = total_travel_cost(current_solution)
    best_solution = current_solution[:]
    
    for iteration in range(max_iter):
        p = 1
        while p <= pmax:
            new_solution = shake(current_solution, k)
            better_solution = local_search(new_solution)
            better_cost = total_travel_cost(better_solution)
            
            if better_cost < best_cost:
                best_solution = better_solution[:]
                best_cost = better_cost
                p = 1  # improvement found, reset p
            else:
                p += 1  # no improvement, go to next neighborhood
        
        current_solution = best_solution[:]  # move to the new best_solution
    return best_solution, best_cost

# Given parameters
cities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 8  # Number of cities to include in the tour, including the depot

# Run the GVNS algorithm
final_tour, final_cost = gvns(k, 100, cities)  # Adjust iterations as required
print("Tour:", final_tour)
print("Total travel cost:", final_cost)