import random
import math

# Define the cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def generate_initial_solution():
    initial_cities = [0]  # Start at the depot
    available_cities = list(cities.keys())[1:]
    random.shuffle(available_cities)
    initial_cities.extend(available_cities[:12])
    initial_cities.append(0)  # End at the depot
    return initial_cities

def local_search(solution):
    best_solution = solution[:]
    best_cost = calculate_total_distance(best_solution)
    
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_total_distance(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    
    return best_solution

def gvns(itermax=100):
    k = 14  # Including the return to the depot city
    best_solution = generate_initial_solution()
    best_cost = calculate_total_distance(best_solution)
    
    for _ in range(itermax):
        current_solution = generate_initial_solution()
        current_solution = local_search(current_solution)
        current_cost = calculate_total_distance(current_message)
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
    
    return best_solution, best_cost

# Execute the GVNS algorithm
best_tour, best_tour_cost = gvns()

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))