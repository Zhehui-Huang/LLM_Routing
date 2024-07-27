import random
import math

# Coordinates of cities indexed from 0 up to 9
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Prepare distance matrix
num_cities = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in cities] for i in cities]

def generate_initial_solution():
    solution = [0] + random.sample(range(1, num_cities), 4)
    solution.append(0)  # Return to depot
    return solution

def calculate_total_distance(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def local_search(solution):
    best_solution = solution[:]
    best_cost = calculate_total_distance(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, 4):
            for j in range(i + 1, 5):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_distance(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
        solution = best_solution[:]
    return best_solution

def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_total_distance(best_solution)
    iterations = 0
    max_iterations = 1000  # Total GVNS iterations to perform
    while iterations < max_iterations:
        new_solution = local_search(best_solution)
        new_solution[random.randint(1, 4)], new_solution[random.randint(1, 4)] = new_solution[random.randint(1, 4)], new_solution[random.randint(1, 4)]
        new_solution = local_search(new_solution)
        new_cost = calculate_total_distance(new_solution)
        if new_cost < best_cost:
            best_solution = new_solution[:]
            best_cost = new_cost
        iterations += 1
    return best_solution, best_cost

# Run the GVNS algorithm
tour, total_cost = gvns()

print("Tour:", tour)
print("Total travel cost:", total_cost)