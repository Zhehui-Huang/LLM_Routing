import random
import itertools
import math

# Coordinates of the cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0]-cities[city2][0])**2 + (cities[city1][1]-cities[city2][1])**2)

# Cost of a given tour
def tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate an initial random solution (tour)
def generate_initial_solution(k):
    selected_cities = [0]
    remaining_cities = list(set(cities.keys()) - {0})
    while len(selected_cities) < k:
        city = random.choice(remaining_cities)
        selected_cities.append(city)
        remaining_cities.remove(city)
    selected_cities.append(0)
    return selected_cities

# Shake function to create neighbors
def shake(solution, k):
    intermediate_solution = solution[1:-1]
    random.shuffle(intermediate_solution)
    return [0] + intermediate if len(intermediate_solution) < k-1 else intermediate_solution[:k-1] + [0]

# Variable Neighborhood Descent
def vnd(solution):
    improved = True
    while improved:
        improved = False
        neighbors = itertools.permutations(solution[1:-1])
        for neighbor in neighbors:
            new_solution = [0] + list(neighbor) + [0]
            if tour_cost(new_solution) < tour_iost(solution):
                solution = new_solution
                improved = True
                break
    return solution

# Main GVNS function
def gvns(k, max_iter=100, pmax=5):
    best_solution = generate_initial_solution(k)
    best_cost = tour_cost(best_solution)
    iter = 0
    while iter < max_iter:
        p = 1
        while p <= pmax:
            new_solution = shake(best_solution, k)
            new_solution = vnd(new_solution)
            new_cost = tour_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                p = 1
            else:
                p += 1
        iter += 1
    
    return best_solution, best_cost

# Run the GVNS
final_tour, total_cost = gvns(7)
print("Tour:", final_tour)
print("Total travel cost:", total_cost)