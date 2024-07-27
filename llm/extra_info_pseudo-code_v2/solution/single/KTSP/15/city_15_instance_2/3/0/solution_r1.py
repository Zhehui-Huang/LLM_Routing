import random
import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_distance(cities, coordinates):
    total_dist = 0
    for i in range(1, len(cities)):
        total_dist += euclidean_distance(coordinates[cities[i-1]], coordinates[cities[i]])
    total_dist += euclidean_distance(coordinates[cities[-1]], coordinates[cities[0]])  # Return to start
    return total_dist

def generate_initial_solution(coordinates, k=8):
    remaining_cities = list(range(1, len(coordinates)))
    random.shuffle(remaining_cities)
    solution = [0]  # starting at the depot
    for _ in range(k - 1):
        next_city = remaining_cities.pop()
        solution.append(next_city)
    solution.append(0)  # ending at the depot
    return solution

def shake(solution, k):
    s_prime = solution[1:-1]  # Remove depot ends
    random.shuffle(s_prime)
    return [0] + s_prime + [0]  # Reattach depot

def local_search(solution, coordinates):
    best_solution = solution[:]
    best_cost = total_distance(solution, coordinates)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != 1 or j != len(solution) - 2:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = total_distance(new_solution, coordinates)
                    if new_cost < best_cost:
                        best_solution = new_solution[:]
                        best_cost = new_cost
                        improved = True
    return best_solution

def gvns(coordinates, k, itermax=50, kmax=3):
    best_solution = generate_initial_solution(coordinates, k)
    best_cost = total_distance(best_solution, coordinates)
    for _ in range(itermax):
        p = 1
        while p <= kmax:
            s_prime = shake(best_solution, k)
            s_double_prime = local_search(s_prime, coordinates)
            s_double_prime_cost = total_distance(s_double_prime, coordinates)
            if s_double_prime_cost < best_cost:
                best_solution = s_double_prime[:]
                best_cost = s_double_prime_cost
                p = 1
            else:
                p += 1
    return best_solution, best_cost

# Coordinates from the task definition
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

best_tour, best_cost = gvns(coordinates, 8)
print('Tour:', best_tour)
print('Total travel cost:', round(best_cost, 2))