import random
import math

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the initial solution
def generate_initial_solution(V, k):
    solution = [0]  # Start at the depot city
    available_cities = list(range(1, len(V)))
    while len(solution) < k:
        city = random.choice(available_cities)
        solution.append(city)
        available_cities.remove(city)
    solution.append(0)  # Return to the depot city
    return solution

# Calculate the tour cost
def calculate_tour_cost(solution, V):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += euclidean_distance(V[solution[i]], V[solution[i+1]])
    return total_cost

# Shaking: Generate a neighbor solution
def shake(solution, V, k):
    new_solution = solution[:]
    num_swaps = random.randint(1, 3)
    for _ in range(num_swaps):
        a, b = random.sample(range(1, k), 2)  # Avoid depot city at index 0
        new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
    return new_solution

# Variable Neighborhood Descent
def vnd(solution, V, k):
    improved = True
    while improved:
        improved = False
        current_cost = calculate_tour_cost(solution, V)
        for i in range(1, k):
            for j in range(i+1, k):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_tour_cost(new_solution, V)
                if new_cost < current_cost:
                    solution = new_solution[:]
                    current_cost = new_cost
                    improved = True
    return solution

# GVNS for k-TSP
def gvns(V, k, nrst):
    best_solution = None
    best_cost = float('inf')
    for _ in range(nrst):
        # Initial solution
        S = generate_initial_solution(V, k)
        current_solution = S[:]
        
        while True:
            # Shaking stage
            S_prime = shake(current_solution, V, k)
            # VND stage
            S_double_prime = vnd(S_prime, V, k)
            S_double_prime_cost = calculate_tour_cost(S_double_prime, V)
            
            if S_double_prime_cost < best_cost:
                best_solution = S_double_prime[:]
                best_cost = S_double_prime_cost
                break
            else:
                current_solution = S_double_prime[:]
    
    return best_solution, best_cost

# Define the cities
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
          (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
          (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Number of cities to visit including the depot: k = 7
k = 7

# Number of restarts
nrst = 100

# Execute GVNS
best_tour, best_cost = gvns(cities, k, nrst)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(best_cost, 2)}")