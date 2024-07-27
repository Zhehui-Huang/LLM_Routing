import math
import random

# Coordinates for each city, including the depot
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# City groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Distance function using Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate an initial solution choosing one city per group
def generate_initial_solution():
    initial_tour = [0]  # start at the depot
    for group in groups:
        # Randomly choose one city from each group
        initial_tour.append(random.choice(group))
    initial_tour.append(0)  # return to the depot
    return initial_tour

# Calculate the travel cost of a given tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Simulated annealing to optimize the tour
def simulated_annealing(initial_tour, iterations=10000, temp=100, alpha=0.995):
    current_tour = initial_tour[:]
    best_tour = current_tour[:]
    best_cost = calculate_tour_cost(best_tour)
    current_cost = best_cost
    
    for _ in range(iterations):
        # Cool down
        temp *= alpha
        
        # Swap two cities in the tour
        new_tour = current_tour[:]
        idx1, idx2 = random.sample(range(1, len(groups) + 1), 2)  # Choose indices to swap, excluding the depot
        new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
        
        # Calculate the cost for the new tour
        new_cost = calculate_tour_cost(new_tour)
        
        # Acceptance probability (to possibly accept worse solution)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_tour, current_cost = new_tour, new_cost
            
            # Update the best found solution if necessary
            if new_cost < best_cost:
                best_tour, best_cost = new_tour, new_cost
    
    return best_tour, best_cost

# Run the solution
initial_tour = generate_initial_solution()
final_tour, final_cost = simulated_annealing(initial_tour)

# Output the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")