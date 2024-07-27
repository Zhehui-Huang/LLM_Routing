import math
import random

# City coordinates
cities = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Parameters
k = 6  # Number of cities in the tour including the depot
iter_max = 1000
p_max = 3

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution():
    tour = [0]  # Start at the depot city
    selected_cities = set(tour)
    while len(tour) < k:
        remaining_cities = [c for c in range(1, len(cities)) if c not in selected_cities]
        city = random.choice(remaining_cities)
        tour.append(city)
        selected_cities.add(city)
    tour.append(0)  # Return to depot
    return tour

def shake(s, p):
    s_prime = s[1:-1]
    if p == 1:
        random.shuffle(s_prime)
    elif p == 2 and len(s_prime) > 2:
        i, j = random.sample(range(1, len(s_prime)), 2)
        s_prime[i - 1], s_prime[j - 1] = s_prime[j - 1], s_prime[i - 1]
    return [0] + s_prime + [0]

def local_search(s, p):
    if p == 1:  # Exchange
        for i in range(1, len(s) - 1):
            for city in range(1, len(cities)):
                if city not in s:
                    new_s = s[:i] + [city] + s[i+1:-1] + [0]
                    if total_distance(new_s) < total_distance(s):
                        s = new_simulation
        return s

def vnd(s):
    for p in range(1, p_max + 1):
        s = local_search(s, p)
    return s

def gvns():
    initial_solution = generate_initial_solution()
    current_solution = initial_solution[:]
    best_solution = current_solution[:]
    best_cost = total_distance(current_solution)
    for _ in range(iter_max):
        for p in range(1, p_max + 1):
            new_solution = shake(current_solution, p)
            new_solution = vnd(new_solution)
            new_cost = total_distance(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
                break
        else:
            current_solution = best_solution[:]  # Reset to best if no improvement
    return best_solution, best_cost

# Execute the algorithm
final_tour, final_cost = gvns()
print("Tour:", final_tour)
print("Total travel cost:", final_cost)