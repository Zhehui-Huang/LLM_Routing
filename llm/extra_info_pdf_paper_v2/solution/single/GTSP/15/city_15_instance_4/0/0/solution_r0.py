import math
import random

# Define city coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Define city groups
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initial tour selection (select a random city from each group)
def initial_tour():
    tour = [0]  # start at the depot
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)  # return to depot
    return tour

# Calculate total travel cost of the tour
def calculate_total_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += euclidean_family(distance(tour[i], tour[i+1]))
    return cost

# Simulated Annealing to optimize the tour
def simulated_annealing(initial_tour):
    current_tour = initial_tour
    current_cost = calculate_total_cost(current_tour)
    temperature = 100 
    cooling_rate = 0.99
      
    while temperature > 0.1:
        new_tour = current_tour[:]
        # Switch two cities in the tour excluding depot
        i, j = random.sample(range(1, len(groups)+1), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_cost = calculate_total_cost(new_tour)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_tour = new_tour
            current_cost = new_cost
            
        temperature *= cooling_rate
        
    return current_tour, current_cost

# Start the optimization
initial = initial_tour()
optimal_tour, total_cost = simulated_annealing(initial)

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")