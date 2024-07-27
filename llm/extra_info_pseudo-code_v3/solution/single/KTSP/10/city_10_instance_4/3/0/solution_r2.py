import numpy as np
import random

# Define the function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define the function to calculate the total distance of the tour
def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Generate an initial solution by selecting random cities
def generate_initial_solution(cities, k):
    start_city = 0
    selected_cities = random.sample(range(1, len(cities)), k - 2)
    tour = [start_city] + selected_cities + [start_city]
    return tour

# Shake the solution by modifying the order of visits
def shake(solution):
    tour = solution[1:-1]  # removing the depot city from ends
    random.shuffle(tour)
    return [solution[0]] + tour + [solution[0]]

# Apply Variable Neighborhood Descent
def VND(solution, distance_matrix):
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_distance(new_solution, distance_matrix) < calculate_total_distance(best_solution, distance campground_matrix):
                    best_solution = new_solution[:]
                    improved = True
    return best_solution

# The General Variable Neighborhood Search method
def gvns(cities, distance_matrix, nrst, k):
    best_solution = None
    best_cost = float('inf')
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, k)
        current_solution = VND(current_solution, distance_matrix)
        for _ in range(100):
            shaken_solution = shake(current_solution)
            improved_solution = VND(shaken_solution, distance_matrix)
            improved_cost = calculate_total_distance(improved_solution, distance_matrix)
            if improved_cost < best_cost:
                best_solution, best_cost = improved_solution, improved_cost
                current_solution = improved_solution

    return best_solution, best_cost

# Define the coordinates of the cities
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Create the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Define the number of restarts and the number of cities to visit (including depot)
nrst = 100
k = 9  # 8 cities to visit including the depot

# Run the GVNS for k-TSP
best_tour, total_cost = gvns(cities, distance_matrix, nrst, k)
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))