import math
import random

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_route_cost(route, coordinates):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]])
    return total_cost

def generate_initial_solution(cities, k):
    solution = [0]
    available_cities = cities[:]
    available_cities.remove(0)
    while len(solution) < k - 1:
        next_city = random.choice(available_cities)
        solution.append(next_city)
        available_cities.remove(next_city)
    solution.append(0)  # Return to depot
    return solution

def shake(solution, k):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    new_solution = [0] + new_solution[:k-2] + [0]  # Ensure exactly k cities and return to depot
    return new_solution

def local_search(solution, coordinates):
    best_cost = total_route_cost(solution, coordinates)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution)):
                # Swap two cities in the tour
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_route_cost(new_solution, coordinates)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
                    improved = True
                    break
            if improved:
                break
    return best_solution

def gvns(coordinates, k=10, itermax=100, pmax=5):
    best_solution = []
    best_cost = float('inf')
    for _ in range(itermax):
        current_solution = generate_initial_solution(list(range(len(coordinates))), k)
        current_cost = total_route_cost(current_search_solution, coords)
        p = 0
        while p < pmax:
            shaken_solution = shake(current_solution, k)
            improved_solution = local_search(shaken_solution, coordinates)
            improved_cost = total_route_cost(improved_solution, coordinates)
            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost
                p = 0
            else:
                p += 1
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_solution
    return best_solution, best_cost

# Given Coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Obtain the solution
tour, travel_cost = gvns(coordinates)
print("Tour:", tour)
print("Total travel cost:", travel_test_cost)