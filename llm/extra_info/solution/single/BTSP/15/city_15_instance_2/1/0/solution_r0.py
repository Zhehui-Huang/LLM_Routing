import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of cities
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Calculate all pairs distances
n_cities = len(cities)
distances = [[0] * n_cities for _ in range(n_cities)]
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Simulated Annealing
def simulated_annealing():
    # Initial solution (random tour)
    current_solution = list(range(n_cities))
    random.shuffle(current_solution)
    current_solution.append(current_solution[0])  # return to the depot
    
    current_cost = sum(distances[current_solution[i]][current_solution[i + 1]] for i in range(n_cities))
    current_max_segment = max(distances[current_solution[i]][current_solution[i + 1]] for i in range(n_cities))
    
    best_solution = current_solution.copy()
    best_cost = current_cost
    best_max_segment = current_max_segment
    
    T = 1000  # Initial temperature
    Tmin = 1  # Minimum temperature
    alpha = 0.99  # Cooling rate
    while T > Tmin:
        for _ in range(1000):  # Number of iterations at each temperature
            # Generate a neighbor solution
            i, j = sorted(random.sample(range(1, n_cities), 2))  # ensure i < j and not selecting depot
            neighbor = current_solution[:]
            neighbor[i:j+1] = reversed(neighbor[i:j+1])  # reverse subpath
            cost = sum(distances[neighbor[k]][neighbor[k + 1]] for k in range(n_cities))
            max_segment = max(distances[neighbor[k]][neighbor[k + 1]] for k in range(n_cities))
            
            # Decide whether to accept neighbor
            if (cost < best_cost and max_segment < best_max_segment) or random.random() < math.exp((current_cost - cost) / T):
                current_solution, current_cost, current_max_segment = neighbor, cost, max_segment
                if cost < best_cost and max_segment < best_max_segment:
                    best_solution, best_cost, best_max_segment = current_solution.copy(), cost, max_segment
        
        T *= alpha  # Cool down

    return best_solution, best_cost, best_max_segment

# Run the optimization algorithm
tour, total_cost, max_distance = simulated_annealing()

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))