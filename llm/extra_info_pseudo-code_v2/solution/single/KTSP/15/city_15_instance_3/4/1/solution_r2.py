import random
import math

# Define cities coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Parameters for the algorithm
num_itermax = 100
pmax = 5
k = 10  # Number of cities to visit, including the depot

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def total_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def generate_initial_solution():
    solution = [0]  # Starting at depot city
    available_cities = list(cities.keys())[1:]  # Exclude depot initially
    chosen_cities = random.sample(available_cities, k - 1)  # Select k-1 additional cities randomly
    solution.extend(chosen_cities)
    solution.append(0)  # Return to depot
    return solution

def shake(solution, k):
    """ Simple shake function: random swap two cities in a tour """
    s_prime = solution[1:-1]  # Exclude depot cities
    city1, city2 = random.sample(range(len(s_prime)), 2)
    s_prime[city1], s_prime[city2] = s_prime[city2], s_prime[city1]
    return [0] + s_prime + [0]  # Reinclude depot cities

def local_search(solution):
    """ Simple local search using 2-opt strategy """
    best_cost = total_cost(solution)
    best_sol = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 2, len(solution) - 1):
                new_solution = solution[:i] + solution[i:j+1][::-1] + solution[j+1:]
                new_cost = total_cost(new_solution)
                if new_cost < best_cost:
                    best_sol = new_solution[:]
                    best_cost = new_cost
                    improved = True
    return best_sol

def gvns():
    best_solution = generate_initial_solution()
    best_cost = total_cost(best_solution)
    
    for _ in range(num_itermax):
        p = 1
        while p <= pmax:
            s_prime = shake(best_solution, p)
            s_double_prime = local_search(s_prime)
            current_cost = total_cost(s_double_prime)
            
            if current_cost < best_cost:
                best_solution = s_double_prime[:]
                best_cost = current_cost
                p = 1
            else:
                p += 1

    return best_solution, best_cost

# Execute the GVNS method to find the optimal solution
optimal_tour, optimal_cost = gvns()

# Print Output
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)