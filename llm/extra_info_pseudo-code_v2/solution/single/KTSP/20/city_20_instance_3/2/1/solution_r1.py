import random
import math
import sys

cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84), 
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def generate_initial_solution(k):
    solution = [0]  # Start at the depot city
    available_cities = list(cities.keys())[1:]  # Exclude the depot initially for random picks
    random.shuffle(available_cities)
    solution.extend(available_cities[:k-1])  # Add k-1 other cities randomly
    solution.append(0)  # Return to the depot
    return solution

def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def shake(solution):
    middle = solution[1:-1]
    random.shuffle(middle)
    return [0] + middle + [0]

def vnd(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    if tour_cost(new_solution) < tour_cost(solution):
                        solution = new_solution
                        improved = True
    return solution

def gvns(k, itermax, pmax):
    best_solution = generate_initial_solution(k)
    best_cost = tour_cost(best_solution)
    for iteration in range(itermax):
        S = best_solution[:]
        for p in range(pmax):
            S_prime = shake(S)
            S_double_prime = vnd(S_prime)
            S_double_prime_cost = tour_cost(S_double_prime)
            if S_double_prime_cost < best_cost:
                best_solution = S_double_prime[:]
                best_cost = S_double_prime_cost
                break  # Reset p and redo shaking with improved solution found
    return best_solution, best_cost

best_solution, best_cost = gvns(13, 100, 10)
print("Tour:", best_solution)
print("Total travel cost:", int(best_cost))