import random
import math
import itertools

# City coordinates indexed by city number
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate a random initial solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 3)
    tour.append(0) # to return to the start
    return tour

# Calculate the total distance of the tour
def calculate_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Performing VND by exploring neighborhoods N1 and N2
def VND(solution):
    improvements = True
    while improvements:
        improvements = False
        best_distance = calculate_distance(solution)

        # N1: Permutation neighborhood
        for i in range(1, 4):
            for j in range(i+1, 4):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = calculate_distance(new_solution)
                if new_distance < best_distance:
                    solution = new_solution
                    best_distance = new_distance
                    improvements = True

    return solution

# Shaking procedure: randomly swap two cities
def shake(solution):
    new_solution = solution[:]
    i, j = random.sample(range(1, 4), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# GVNS algorithm
def GVNS(num_restarts):
    best_solution = generate_initial_solution()
    best_total_distance = calculate_distance(best_solution)

    for _ in range(num_restarts):
        current_solution = generate_initial_solution()
        while True:
            new_solution = shake(current_solution)
            improved_solution = VND(new_solution)
            improved_distance = calculate_distance(improved_solution)
            if improved_distance < best_total_distance:
                best_solution = improved_solution
                best_total_distance = improved_distance
                break
            current_solution = improved_solution

    return best_solution, best_total_distance

# Main execution with specified number of restarts
best_solution, best_cost = GVNS(1000)
output_tour = best_solution
output_cost = best_cost

# Printing the results
print("Tour:", output_tour)
print("Total travel cost:", output_cost)