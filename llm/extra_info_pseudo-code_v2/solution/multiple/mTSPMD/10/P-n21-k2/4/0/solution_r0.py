import random
import math

# Define the cities and their coordinates (includes the depots as cities)
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Initialize parameters for the ACO
antnum = 10
cyclenum = 100
alpha = 1.0
beta = 2.0
rho = 0.1
inittrail = 1.0
num_cities = len(cities)

# Initialize the pheromone trails
pheromones = [[inittrail for _ in range(num_cities)] for _ in range(num_cities)]
heuristic_info = [[0 if i == j else 1/euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Solution representation
best_solution = None
best_cost = float('inf')

for cycle in range(cyclenum):
    solutions = []
    for ant in range(antnum):
        tour = []
        cost = 0
        # Randomly assign a starting depot for each ant
        starting_depot = random.choice([0, 1])
        current_city = starting_depot
        
        # Build tour for this ant
        allowed_cities = list(cities.keys())
        allowed_cities.remove(current_city)
        tour.append(current_city)
        
        while allowed_cities:
            probabilities = []
            total_prob = 0
            
            for city in allowed_cities:
                prob = (pheromones[current_city][city] ** alpha) * (heuristic_info[current_city][city] ** beta)
                probabilities.append(prob)
                total_prob += prob
            
            probabilities = [prob / total_prob for prob in probabilities]
            next_city = random.choices(allowed_cities, weights=probabilities)[0]
            cost += euclidean_distance(cities[current_city], cities[next_city])
            
            current_city = next_city
            tour.append(current_city)
            allowed_cities.remove(current_city)
        
        # Return to depot
        tour.append(starting_depot)
        cost += euclidean_distance(cities[current_city], cities[starting_depot])
        solutions.append((tour, cost))
        
        # Update best solution if found
        if cost < best_cost:
            best_cost = cost
            best_solution = tour
    
    # Update pheromone trails
    for i in range(num_cities):
        for j in range(num_cities):
            pheromones[i][j] *= (1 - rho)
    
    for tour, cost in solutions:
        for i in range(len(tour) - 1):
            pheromones[tour[i]][tour[i+1]] += 1 / cost

# Output the final results
print(f"Robot 0 Tour: {best_solution if best_solution[0] == 0 else []}")
print(f"Robot 0 Total Travel Cost: {best_cost if best_solution[0] == 0 else 0}")

print(f"Robot 1 Tour: {best_solution if best_solution[0] == 1 else []}")
print(f"Robot 1 Total Travel Cost: {best_cost if best_solution[0] == 1 else 0}")

print(f"Overall Total Travel Cost: {best_cost}")