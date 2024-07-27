import random
import math
import numpy as np

# Calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Right now, we'll encode the cities' coordinates.
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Create distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Generate a random initial k-TSP solution
def generate_initial_solution(k):
    solution = [0]  # Start at the depot city, index 0
    remaining_cities = list(range(1, n))
    for _ in range(k - 1):
        city = random.choice(remaining_cities)
        remaining_cities.remove(city)
        solution.append(city)
    solution.append(0)  # Return to the depot city
    return solution

# Function to calculate the cost of the tour
def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Variable Neighborhood Descent (VND)
def vnd(solution, distances, k):
    improved = True
    while improved:
        improved = False
        # Try exchanging each pair of cities and see if it improves the solution
        for i in range(1, k):
            for j in range(i + 1, k):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_tour_cost(new_solution, distances)
                if new_cost < calculate_tour_cost(solution, distances):
                    solution = new_solution
                    improved = True
    return solution

# The Shaking routine to escape local minima
def shake(solution, k):
    shaken_solution = solution[1:-1]  # remove depot start/end
    random.shuffle(shaken_solution)
    return [0] + shaken_solution + [0]

# GVNS algorithm
def gvns(k, cities, distances, max_restarts=100):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_tour_cost(best_solution, distances)

    for _ in range(max_restarts):
        current_solution = shake(best_solution, k)
        current_solution = vnd(current_solution, distances, k)
        current_cost = calculate_tour_cost(current_solution, distances)
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
            
    return best_solution, best_cost

# Set the number of cities to visit to 16
k = 16
best_tour, best_tour_cost = gvns(k, cities, distance_matrix)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)