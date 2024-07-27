import math
import random

# Given city coordinates, calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Our city coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
          (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
          (70, 95), (29, 64), (32, 79)]

# Generate initial solution
def generate_initial_solution():
    tour = [0]  # start at city 0
    remaining_cities = list(range(1, 15))
    while len(tour) < 11:
        next_city = random.choice(remaining_cities)
        tour.append(next_city)
        remaining_cities.remove(next_city)
    tour.append(0)  # end at city 0
    return tour

# Calculate total distance of the tour
def calculate_cost(tour):
    total_distance = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    return total_distance

def two_opt_swap(tour, i, k):
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

# Variable Neighborhood Descent
def vnd(solution):
    improved = True
    while improved:
        improved = False
        best_cost = calculate_cost(solution)
        for i in range(1, len(solution) - 2):
            for k in range(i+1, len(solution) - 1):
                new_solution = two_opt_swap(solution, i, k)
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    solution = new_solution
                    best_cost = new_t
                    improved = True
    return solution

# Shaking: altering some part of the tour randomly
def shake(tour):
    i = random.randint(1, 8)
    k = random.randint(i+1, 9)
    return two_opt_swap(tour, i, k)

# Wrap everything in the GVNS algorithm
def gvns(Nrst):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(Nrst):  # Number of restarts
        solution = generate_initial_solution()
        while True:
            new_solution = shake(solution)
            improved_solution = vnd(new_solution)
            cost = calculate_cost(improved_solution)
            if cost < best_cost:
                best_solution = improved_solution
                best_cost = cost
                break
    
    return best_solution, best_cost

# Use gvns with a reasonable number of restarts
final_solution, final_cost = gvns(100)
print("Tour:", final_solution)
print("Total travel cost:", final_cost)