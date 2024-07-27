import math
import random

# Define the cities' coordinates
cities_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2), 
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), 
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate Euclidean distances between all pairs of cities
def calculate_distance(i, j):
    return math.sqrt((cities_coordinates[i][0] - cities_coordinates[j][0]) ** 2 + 
                     (cities_coordinates[i][1] - cities_coordinates[j][1]) ** 2)

# Number of cities
n = len(cities_coordinates)

# Distance matrix holding distances between each pair of cities
distance_matrix = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Simulated Annealing to minimize the maximum leg distance in the tour.
def simulated_annealing():
    # Initial configuration: a random tour starting and ending at the depot (city 0)
    current_solution = [0] + random.sample(range(1, n), n - 1) + [0]
    current_cost = sum(distance_matrix[current_solution[i]][current_solution[i+1]] for i in range(n))
    current_max_leg = max(distance_matrix[current_solution[i]][current_solution[i+1]] for i in range(n))
    
    T = 1000  # Initial temperature
    T_min = 1  # Minimum temperature
    alpha = 0.99  # Cooling rate
    
    # Function to calculate the "cost" of a solution, aiming to minimize the longest tour leg
    def solution_cost(solution):
        max_leg = max(distance_matrix[solution[i]][solution[i+1]] for i in range(n))
        return max_leg
    
    # Annealing process
    while T > T_min:
        for _ in range(1000):
            # Take two cities and swap them (except depot city 0)
            i, j = random.sample(range(1, n), 2)
            new_solution = current_solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            
            # Evaluate the new solution
            new_cost = solution_cost(new_solution)
            
            # Acceptance probability to possibly accept a worse solution to escape local minima
            if new_cost < current_max_leg or random.random() < math.exp((current_max_leg - new_cost) / T):
                current_solution = new_solution
                current_max_leg = new_cost
        
        # Decrease the temperature
        T *= alpha
    
    return current_solution, current_max_leg

# Running the optimization
tour, max_distance = simulated_annealing()

# Calculating the total travel cost of the tour
total_travel_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")