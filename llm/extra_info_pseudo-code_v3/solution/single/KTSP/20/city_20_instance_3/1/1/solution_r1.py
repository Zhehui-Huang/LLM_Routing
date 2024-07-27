import math
import random

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16),
    17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total distance of a tour
def total_tour_distance(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Function to generate a random initial tour including 13 cities starting and ending at the depot city
def generate_initial_solution():
    all_cities = list(cities.keys())
    selected_cities = random.sample(all_cities[1:], 12)  # Select 12 cities randomly, excluding the depot
    tour = [0] + selected_cities + [0]  # Start and end at the depot
    return tour

# Function to generate a new solution by swapping two cities
def shake(solution, k):
    new_solution = solution[:]
    for _ in range(k):
        i, j = random.sample(range(1, len(solution) - 2), 2)  # Exclude the first and last element (depot)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Function to apply Variable Neighborhood Descent
def vnd(solution):
    best_solution = solution[:]
    best_cost = total_tour_distance(solution)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_tour_distance(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
                    improved = True
        solution = best_solution

    return solution

# General Variable Neighborhood Search algorithm
def gvns(Nrst=100):
    best_solution = generate_initial_solution()
    best_cost = total_tour_distance(best_solution)

    for _ in range(Nrst):
        current_solution = generate_initial_solution()
        for _ in range(10):  # inner loop iterations
            current_solution = shake(current_result, 2)
            current_solution = vnd(current_result)
            current_cost = total_tour_distance(current_result)
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

    return best_solution, best_cost

# Running the GVNS algorithm
best_tour, best_cost = gvns()

# Print results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")