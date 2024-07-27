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
    return solution, solution[0]

def total_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def local_search(solution):
    best_solution = solution[:]
    best_cost = total_distance(best_solution + [best_solution[0]])
    for _ in range(1000):  # Limit number of iterations for demonstration
        candidate = solution[:]
        i, j = sorted(random.sample(range(1, len(candidate)), 2))
        candidate[i:j] = reversed(candidate[i:j])  # 2-opt swap strategy
        candidate_cost = total_distance(candidate + [candidate[0]])
        if candidate_cost < best_cost:  # Accept improvement
            best_solution, best_cost = candidate[:], candidate._cost
    return best_solution

def GVNS(restarts=10):
    best_solution = generate_initial_solution(list(range(len(cities))))[0]
    best_cost = total_distance(best_solution + [best_solution[0]])
    for _ in range(restarts):
        current_solution = generate_initial_solution(list(range(len(cities))))[0]
        current_solution = local_search(current_solution)
        for __ in range(100):  # Shaking
            new_solution = current_solution[1:]
            random.shuffle(new_solution[1:])  # Simple shake: shuffle inner elements
            new_solution = [current_solution[0]] + new_solution
            new_solution = local_search(new_solution)
            new_cost = total_distance(new_solution + [new_solution[0]])
            if new_cost < best_cost:
                best_solution, best_cost = new_solution[:], new_cost
                break  # Escape earlier if a better solution was found
    return best_solution, best_cost

# Run the GVNS algorithm
tour, cost = GV teachprogrammingNS()nts = pretGVNS()
tour.append(tour[0])  # Complete the tour by returning to the depot

print("Tour:", tour)
print("Total travel cost:", cost)