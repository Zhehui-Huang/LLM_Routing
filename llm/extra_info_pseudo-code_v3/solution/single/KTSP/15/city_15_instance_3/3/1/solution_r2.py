import math
import random

# City coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
          (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
          (70, 95), (29, 64), (32, 79)]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate initial random tour with exactly 10 cities including the depot
def generate_initial_solution():
    tour = [0]  # start from depot
    chosen_cities = random.sample(range(1, 15), 9)  # select 9 random cities, excluding depot
    tour += chosen_cities + [0]  # return to depot
    return tour

# Calculate the total travel distance of the tour
def calculate_cost(tour):
    total_cost = sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    return total_cost

# Implement the Two_opt_swap
def two_opt_swap(tour, i, k):
    new_tour = tour[:i] + tour[i:k + 1][::-1] + tour[k + 1:]
    return new_tour

# Variable Neighborhood Descent (VND) using two neighborhoods
def vnd(solution):
    improvement = True
    while improvement:
        improvement = False
        best_cost = calculate_cost(solution)
        for i in range(1, len(solution) - 1):
            for k in range(i + 1, len(solution)):
                new_solution = two_opt_swap(solution, i, k)
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    solution = new_solution
                    best_cost = new_cost
                    improvement = True
    return solution

# Shaking function: randomly perturb the solution
def shake(solution):
    i = random.randint(1, len(solution) - 4)
    k = random.randint(i + 1, len(solution) - 1)
    return two_opt_swap(solution, i, k)

# GVNS implementation
def gvns(num_restarts):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(num_restarts):
        solution = generate_initial_solution()
        solution = vnd(solution)
        for _ in range(10):  # applying shaking and VND iteratively
            new_solution = shake(solution)
            new_solution = vnd(new_solution)
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
        # After shaking-VND loops, check with previous best
        final_cost = calculate_cost(solution)
        if final_cost < best_cost:
            best_solution = solution
            best_cost = final_cost

    return best_solution, best_cost

# Perform GVNS with 50 restarts
final_solution, final_cost = gvns(50)

print("Tour:", final_solution)
print("Total travel cost:", final_cost)