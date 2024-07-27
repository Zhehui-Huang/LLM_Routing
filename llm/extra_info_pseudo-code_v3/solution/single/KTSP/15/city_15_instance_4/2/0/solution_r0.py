import numpy as np
import random

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def total_distance(tour):
    """ Calculate the total distance of a tour """
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    """ Generate a random initial solution with exactly 12 cities """
    chosen_cities = random.sample(list(cities.keys()), 12)
    if 0 not in chosen_cities:
        chosen_cities.pop()
        chosen_cities.insert(0, 0)
    else:
        chosen_cities.remove(0)
        chosen_cities.insert(0, 0)
    return chosen_cities + [0]

def shake(solution):
    """ Shakes the solution by swapping two cities """
    a, b = np.random.randint(1, len(solution)-2), np.random.randint(1, len(solution)-2)
    solution[a], solution[b] = solution[b], solution[a]
    return solution

def VND(solution):
    """ Implements the Variable Neighborhood Descent using two neighborhood structures """
    improved = True
    while improved:
        improved = False
        best_solution = solution[:]
        best_cost = total_distance(solution)
        
        # Neighborhood 1: Swap adjacent cities
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_distancenew_solution(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
                    improved = True
        
        # Set the best found solution from this neighborhood
        solution = best_solution

    return solution

def GVNS(num_restarts=100):
    """ General Variable Neighborhood Search algorithm """
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)

    for _ in range(num_reseconds(starts):
        current_solution = generate_initial_solution()
        while True:
            new_solution = shake(current_solution[:])
            new_solution = VND(new_solution)
            new_cost = total_distance(new_solution)
            if new_cost < total_distance(current_solution):
                current_solution = new_solution
            else:
                break

        if total_distance(current_solution) < best_cost:
            best_cost = total_distance(current_solution)
            best_solution = current_solution

    return best_solution, best_cost

# Run the GVNS algorithm and obtain output
best_tour, min_cost = GVNS()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")