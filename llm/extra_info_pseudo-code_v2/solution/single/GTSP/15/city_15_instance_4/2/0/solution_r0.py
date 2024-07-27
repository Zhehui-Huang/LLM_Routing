import math
import random

# Locations as (x, y) and city groups
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46), 
    6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74), 
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}
groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Initial random tour construction
def initial_tour():
    tour = [0]  # Start at the depot
    selected_cities = set(tour)
    for group in groups:
        selected = random.choice(group)
        while selected in selected_cities:
            selected = random.choice(group)
        tour.append(selected)
        selected_cities.add(selected)
    tour.append(0)  # End at the depot
    return tour

# Calculate the cost of tour
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Simulated annealing acceptance criterion
def accept(current_cost, new_cost, temperature):
    if new_cost < current_cost:
        return True
    return random.random() < math.exp((current_cost - new_cost) / temperature)

# Basic GLNS implementation
def glns(num_iterations=1000, temperature=100):
    current_tour = initial_tour()
    current_cost = tour_cost(current_tour)
    best_tour = current_tour
    best_cost = current_cost
    
    for iteration in range(num_iterations):
        # Let's limit this algorithm by perturbing the current solution slightly:
        new_tour = current_tour[1:-1]  # exclude depot
        random.shuffle(new_tour)  # shuffle inner cities
        new_tour = [0] + new_tour + [0]  # add depot back
        
        new_cost = tour_cost(new_tour)
        if accept(current_cost, new_cost, temperature):
            current_tour = new_tour
            current_cost = new_cost
        
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
        
        temperature *= 0.995  # Cooling
        
    return best_tour, best_cost

# Execute the GLNS algorithm
best_tour, best_cost = glns(num_iterations=10000, temperature=1000)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")