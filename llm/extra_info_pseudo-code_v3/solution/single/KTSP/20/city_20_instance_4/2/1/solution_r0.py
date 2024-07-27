import random
import math
from itertools import permutations

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities, k):
    solution = [0] + random.sample(cities[1:], k-1)
    solution.append(0)  # to close the loop back to the depot
    return solution

def shake(solution):
    # Let's implement a simple shake: swap two cities in the solution
    city1, city2 = random.sample(range(1, len(solution)-1), 2)
    solution[city1], solution[city2] = solution[city2], solution[city1]
    return solution

def local_search(solution, n1, n2, distances):
    # Implement a very basic local search by trying all pairs of swaps (2-opt)
    improved = True
    while improved:
        improved = False
        best_cost = total_tour_cost(solution, distances)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i == 0 or j == len(solution) - 1:
                    continue  # Skip the depot
                new_solution = solution[:]
                new_solution[i:j+1] = new_solution[i:j+1][::-1]
                new_cost = total_tour_cost(new_solution, distances)
                if new_cost < best_cost:
                    solution, best_cost = new_solution, new_cost
                    improved = True
    return solution

def gvns(cities, k, distances, nrst):
    best_solution = generate_initial_solution(cities, k)
    best_cost = total_tour_cost(best_solution, distances)
    
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, k)
        while True:
            new_solution = shake(current_solution[:])
            new_solution = local_search(new_solution, 'N1', 'N2', distances)
            new_cost = total_tour_cost(new_solution, distances)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                break  # reset and restart shaking from improved solution
            else:
                # no improvement, break the loop
                break
    
    return best_solution, best_cost

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Build distance matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Apply GVNS to solve the problem
best_tour, best_cost = gvns(cities, 16, distances, 50)

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(best_cost, 2)}")