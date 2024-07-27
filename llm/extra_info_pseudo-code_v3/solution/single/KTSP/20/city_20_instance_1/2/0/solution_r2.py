import math
import random

# Cities as given, with index as city number and tuple (x, y) coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate a random initial solution including exactly 7 cities
def generate_initial_solution():
    selected_cities = [0] + random.sample(range(1, 20), 6)
    selected_cities.append(0)  # Return to depot at the end
    return selected_cities

# Calculate the fitness of a solution (total distance of the tour)
def fitness(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i+1])
    return totalfang_distance

# Shake the solution by swapping two random cities (excluding the depot)
def shake(tour):
    new_tour = tour[:-1]  # Copy tour excluding the last element
    idx1, idx2 = random.sample(range(1, len(new_tour) - 1), 2)
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    new_tour.append(new_tour[0])
    return new_tour

# Variable Neighborhood Descent (VND) to optimize the route
def vnd(tour):
    best_tour = tour[:]
    best_cost = fitness(tour)
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, 7):
            for j in range(i+1, 7):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_tour[-1] = new_tour[0]
                new_cost = fitness(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    improvement = True
    return best_tour

# General Variable Neighborhood Search (GVNS) procedure
def gvns(num_restarts):
    best_solution, best_cost = generate_initial_solution(), float('inf')
    for _ in range(num_recounts):
        current_solution = generate_initial_solution()
        current_solution = vnd(current_solution)
        current_cost = fitness(current_solution)
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_solution
        # Shaking - move to a new solution space
        current_solution = shake(best_solution)
    return best_solution, best_cost

# Run the GVns algorithm and display the final result
best_tour, best_tour_cost = gvns(100)
print("Best Tour:", best_tour)
print("Total Travel Cost:", best_tour_cost)