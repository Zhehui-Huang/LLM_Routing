import random
import math

# Define the coordinates of the cities
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

# Calculate the Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate an initial feasible solution
def generate_initial_solution(k):
    solution = [0]  # Start at the depot
    available_cities = list(cities.keys())[1:]  # Exclude depot initially for random selection
    solution.extend(random.sample(available_cities, k-2))
    solution.append(0)  # End at the depot
    return solution

# Shake the solution by swapping two random non-depot cities
def shake(solution):
    new_solution = solution[:]
    idx1, idx2 = random.sample(range(1, len(solution)-2), 2)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# Variable Neighborhood Descent
def vnd(solution):
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if tour_cost(new_solution) < tour_cost(best_solution):
                    best_solution = new_solution[:]
                    improved = True
    return best_solution

# Calculate the total cost of the tour
def tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Main GVNS algorithm
def gvns(max_iter, k, p_max):
    best_solution = generate_initial_solution(k)
    best_cost = tour_cost(best_solution)
    iter = 0
    while iter < max_iter:
        p = 0
        while p < p_max:
            new_solution = shake(best_solution)
            new_solution = vnd(new_solution)
            new_cost = tour_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                p = 0
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Run the algorithm
final_solution, final_cost = gvns(100, 7, 5)
print("Tour:", final_solution)
print("Total travel cost:", final_cost)