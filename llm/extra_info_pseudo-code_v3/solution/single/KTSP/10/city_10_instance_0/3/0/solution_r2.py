import random
import math

# Define the city coordinates indexed by city number
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to generate a random tour of exactly 4 cities starting and ending at the depot (city 0)
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 3)
    tour.append(0) # return to the starting city
    return tour

# Compute the total distance for a given tour
def calculate_distance(tour):
    total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_distance

# Variable Neighborhood Descent function
def VND(solution):
    best_solution = solution[:]
    best_distance = calculate_distance(best_solution)
    improved = True

    while improved:
        improved = False
        # Explore the neighborhood by two-city swaps
        for i in range(1, len(best_solution) - 2):
            for j in range(i + 1, len(best_solution) - 1):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = calculate_distance(new_solution)
                
                if new_distance < best_distance:
                    best_solution = new_solution
                    best_distance = new_distance
                    improved = True

    return best_solution

# Shaking the solution by swapping two random cities
def shake(solution):
    city1, city2 = random.sample(range(1, 4), 2)  # indices 1 to 3 are the ones we change (not the depot)
    new_solution = solution[:]
    new_solution[city1], new_solution[city2] = new_solution[city2], new_solution[city1]
    return new_solution

# General Variable Neighborhood Search algorithm
def GVNS(num_restarts):
    best_solution = generate_initial_solution()
    best_distance = calculate_distance(best_solution)

    for _ in range(num_restarts):
        current_solution = best_solution[:]
        current_distance = best_distance

        # Shake and apply VND
        for _ in range(10):  # 10 shakings per restart
            new_solution = shake(current_solution)
            improved_solution = VND(new_solution)
            improved_distance = calculate_distance(improved_solution)

            if improved_distance < current_distance:
                current_solution = improved_solution
                current_distance = improved_distance
            
            if current_distance < best_distance:
                best_solution = current_solution
                best_distance = current_distance

    return best_solution, best_distance

# Execute the GVNS algorithm
solution, total_distance = GVNS(100)
print("Tour:", solution)
print("Total travel cost:", total_distance)