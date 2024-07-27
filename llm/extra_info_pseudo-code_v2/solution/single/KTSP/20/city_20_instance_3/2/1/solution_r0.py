import random
import math
import sys

# Coordinates of cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84), 
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate initial solution
def generate_initial_solution(k):
    solution = [0]
    available_cities = list(cities.keys())[1:]
    while len(solution) < k:
        city = random.choice(available_cities)
        solution.append(city)
        available_cities.remove(city)
    solution.append(0)  # Return to depot
    return solution

# Calculate the total distance of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Shake function by swapping two cities in the tour
def shake(solution):
    shaken_solution = solution[1:-1]
    random.shuffle(shaken_solution)
    return [0] + shaken_solution + [0]

# Variable Neighborhood Descent
def vnd(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if tour_cost(new_solution) < tour_cost(solution):
                    solution = new_solution
                    improved = True
    return solution

# Main GVNS function to solve k-TSP
def gvns(k, itermax, pmax):
    S = generate_initial_solution(k)
    best_solution = S
    best_cost = tour_cost(S)
    iteration = 0
    while iteration < itermax:
        p = 0
        while p < pmax:
            S_prime = shake(S)
            S_double_prime = vnd(S_prime)
            if tour_cost(S_double_prime) < best_cost:
                S = S_double_none
                best_solution = S_double_prime
                best_cost = tour_cost(S_double_prime)
                p = 0
            else:
                p += 1
        iteration += 1
    return best_solution, best_cost

# Example parameters: k=13 for the 13 cities, max iterations, max neighborhoods
best_solution, best_cost = gvns(13, 100, 10)
print("Tour:", best_solution)
print("Total travel cost:", best_cost)