import math
import random

# Define the coordinates of each city
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Function to calculate the total cost of a tour and the maximum distance between consecutive cities
def evaluate_tour(tour):
    total_dist = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_dist += dist
        max_dist = max(max_dist, dist)
    return total_dist, max_dist

# Simulated Annealing settings
def simulated_annealing():
    temp = 1000
    cooling_rate = 0.995
    current_solution = list(range(1, len(cities)))
    random.shuffle(current_solution)
    current_solution = [0] + current_solution + [0]
    current_cost, current_max = evaluate_tour(current_solution)
    
    best_solution = current_solution
    best_cost, best_max = current_cost, current_max
    
    while temp > 1:
        # Create new solution by swapping two cities
        new_solution = current_solution[:]
        left, right = random.randint(1, len(cities) - 2), random.randint(1, len(cities) - 2)
        new_solution[left], new_solution[right] = new_solution[right], new_solution[left]
        
        new_cost, new_max = evaluate_tour(new_solution)
        
        # Decide whether to accept the new solution
        if new_max < current_max or random.random() < math.exp((current_max - new_max) / temp):
            current_solution, current_cost, current_max = new_solution, new_cost, new_max
        
        # Update best solution found
        if current_max < best_max:
            best_solution, best_cost, best_max = current_solution, current_cost, current_max
        
        temp *= cooling_rate
    
    return best_solution, best_cost, best_max

# Run the optimization
final_tour, total_cost, max_distance = simulated_annealing()

# Display the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")