import numpy as np
import random

# City coordinates
coordinates = [
    (3, 26),  # Depot - City 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88),
    (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def total_distance(tour):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution():
    tour = [0] + random.sample(range(1, num_cities), 9)
    tour.append(0)  # Closing the tour back to the depot
    return tour

def shake(tour):
    front = tour[:1]  # Start point (Depot)
    middle = tour[1:-1]  # States to be shuffled
    end = tour[-1:]  # End point (Depot)
    
    random.shuffle(middle)
    return front + middle + end

def variable_neighborhood_descent(tour):
    best = tour
    best_cost = total_distance(tour)
    
    made_improvement = True
    while made_improvement:
        made_improvement = False
        # Swap cities
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_distance(new_tour)
                if new_cost < best_cost:
                    best, best_cost = new_tour, new_cost
                    made_improvement = True
    
    return best

# Main GVNS Function
def GVNS(max_restarts=100):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(max_restarts):
        initial_solution = generate_initial_solution()
        
        current_solution = initial_solution
        current_cost = total_distance(current_solution)
        
        improvement = True
        while improvement:
            new_solution = shake(current_solution)
            new_solution = variable_neighborhood_descent(new_solution)
            new_cost = total_distance(new_solution)
            
            if new_cost < current_cost:
                current_solution, current_cost = new_solution, new_cost
                improvement = True
            else:
                improvement = False
        
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
    
    return best_solution, best_cost

# Get the best tour and cost
best_tour, best_tour_cost = GVNS()

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)