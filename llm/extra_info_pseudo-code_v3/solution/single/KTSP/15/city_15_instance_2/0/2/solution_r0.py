import random
import math

# Cities coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance
def distance(id1, id2):
    x1, y1 = cities[id1]
    x2, y2 = cities[id2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate initial random solution
def generate_initial_solution(cities, k=8):
    city_indices = list(cities.keys())
    city_indices.remove(0)
    random.shuffle(city_indices)
    tour = [0] + city_indices[:k-1] + [0]
    return tour

# Compute tour cost
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# Shake: Simple perturbation, swap two random cities in the tour
def shake(tour):
    n = len(tour) - 2  # exclude depot nodes
    idx1, idx2 = random.sample(range(1, n), 2)
    new_tour = tour[:]
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    new_tour[-1] = 0  # ensure return to depot
    return new_tour

# Variable Neighborhood Descent
def vnd(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i+1, len(tour) - 2):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if tour_cost(new_tour) < tour_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

# Main GVNS function
def gvns(max_iterations=1000, k=8):
    best_solution = generate_initial_solution(cities, k)
    best_cost = tour_cost(best_solution)
    
    for _ in range(max_iterations):
        current_solution = shake(best_solution)
        new_solution = vnd(current_solution)
        new_cost = tour_cost(new_solution)
        
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_n_COST

    return best_solution, best_cost

# Running the algorithm
best_tour, best_total_cost = gvns(max_iterations=100)

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total overdose.round()}")