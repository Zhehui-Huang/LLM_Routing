import random
import math

# City Coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Define the Euclidean distance between two cities
def euclidean(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to calculate the total tour cost
def calculate_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean(tour[i], tour[i+1])
    return cost

# Generate initial solution
def generate_initial_solution(cities, k):
    tour = [0] # Start at the depot city
    available_cities = list(cities.keys())[1:]
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0) # Return to the depot
    return tour

# Neighborhood function: Shake
def shake(solution, k):
    tour = solution[1:-1]
    random.shuffle(tour)
    return [0] + tour + [0]

# Neighborhood function: Local search (swap two cities)
def local_search(solution):
    best_cost = calculate_cost(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = calculate_cost(new_solution)
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_solution = new_solution
                        improved = True
    return best_solution

# Variable Neighborhood Search
def variable_neighborhood_search(max_iter, k):
    current_solution = generate_initial_solution(cities, k)
    best_solution = current_solution[:]
    best_cost = calculate_cost(current_solution)
    
    for _ in range(max_iter):
        for p in range(1, 3):  # two levels of neighborhood
            new_solution = shake(current_solution, p)
            new_solution = local_search(new_solution)
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
                break
        current_solution = best_solution
    
    return best_solution, best_cost

# Set parameters for GVNS
k = 12  # Including depot
max_iter = 100

# Solve TSP using GVNS
best_tour, best_tour_cost = variable_neighborhood_search(max_iter, k)
output = f"Tour: {best_tour}\nTotal travel cost: {best_tour_cost:.2f}"
print(output)