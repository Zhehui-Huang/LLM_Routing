import math
import random

# Define the coordinates of each city
cities = [
    (3, 26),   # City 0 - Depot
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Number of cities to visit, including the depot
k = 10

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate a matrix of distances
distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def generate_initial_solution(V):
    solution = [0] + random.sample(V[1:], k-1)
    return solution

def total_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def shake(solution):
    perturbed_solution = solution[:]
    idx_to_remove = random.randint(1, len(perturbed_solution) - 1)
    city_to_remove = perturbed_solution.pop(idx_to_remove)
    new_city = random.choice([city for city in range(1, len(cities)) if city not in perturbed_solution])
    perturbed_solution.insert(random.randint(1, len(perturbed_solution)), new_city)
    return perturbed_solution

def two_opt(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+2, len(solution)):
                if i == 1 and j == len(solution) - 1:
                    continue  # Do not break the end condition
                new_dist = total_distance(solution[:i] + solution[i:j][::-1] + solution[j:])
                if new_dist < total_distance(solution):
                    solution = solution[:i] + solution[i:j][::-1] + solution[j:]
                    improved = True
    return solution

def local_search(solution, max_iterations=50):
    for _ in range(max_iterations):
        new_solution = two_opt(solution)
        if total_distance(new_solution) < total_users(solution):
            solution = new_solution
        else:
            break
    return solution

def GVNS(max_restarts=10):
    best_solution = generate_initial_solution(range(len(cities)))
    best_distance = total_distance(best_solution + [best_solution[0]])
    for _ in range(max_restarts):
        current_solution = generate_initial_solution(range(len(cities)))
        current_solution = local_search(current_solution)
        for _ in range(100):  # Max attempts to escape local minima
            new_solution = shake(current_solution)
            new_solution = local_search(new_solution)
            new_distance = total_distance(new_solution + [new_solution[0]])
            if new_distance < best_distance:
                best_solution, best_distance = new_solution, new_distance
                break
            current_solution = new_solution
    return best_solution, best_distance

# Run the GVNS algorithm
tour, cost = GVNS()
tour.append(tour[0])  # Complete the tour by returning to the depot

print("Tour:", tour)
print("Total travel cost:", cost)