import random
import math

# Coordinates of each city including the depot city
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Parameters for GVNS
itermax = 100
pmax = 2
k = 4  # Number of cities in the tour (including the depot)

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return cost

def generate_initial_solution():
    tour = [0] + random.sample(range(1, len(cities)), k - 1)
    return tour

def shake_solution(current_solution, p):
    new_solution = current_solution[:]
    if p == 1:
        # Swap two randomly chosen elements after the depot
        i, j = random.sample(range(1, k), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def local_search(solution, p):
    best_solution = solution[:]
    best_cost = calculate_tour_cost(best_solution)
    for i in range(1, k):
        for city in range(1, len(cities)):
            if city not in solution:
                new_solution = solution[:]
                new_solution[i] = city
                new_cost = calculate_tour_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
    return best_solution

def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)

    for iter in range(itermax):
        current_solution = best_solution[:]
        p = 1
        while p <= pmax:
            S_prime = shake_solution(current_solution, p)
            S_double_prime = local_search(S_prime, p)
            S_double_prime_cost = calculate_tour_cost(S_double_prime)
            if S_double_prime_cost < best_cost:
                best_solution = S_double_prime[:]
                best_cost = S_double_math_cost
                current_solution = S_double_prime[:]
                p = 1  # Reset p if improvement found
            else:
                p += 1

    return best_solution, best_cost

# Execute the algorithm
final_tour, final_cost = gvns()
final_tour.append(0)  # Ensure the tour is completing at the depot

print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))