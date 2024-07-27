import math
import random

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247), 6: (146, 246),
    7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of robots and initial tour assignments
num_robots = 4
tours = {k: [0] for k in range(num_robots)}

# Distributing cities (except the depot city 0) among robots
city_ids = list(cities.keys())[1:]  # exclude the depot
random.shuffle(city_ids)
for i, city in enumerate(city_ids):
    tours[i % num_robots].append(city)

# Make sure each tour ends at the depot
for k in tours:
    tours[k].append(0)

# Calculate total travel cost for a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# VNS to improve the solution
def variable_neighborhood_search(max_iter=10000):
    best_solution = tours
    best_max_cost = max(tour_cost(tours[r]) for r in tours)
    iteration_no_improve = 0
    
    while iteration_no_improve < 1000 and iteration_no_improve < max_iter:
        # Shaking
        new_solution = {r: tours[r][:] for r in tours}
        for r in new_solution:
            if len(new_solution[r]) > 3:  # More than just the depot at start and end
                a, b = sorted(random.sample(range(1, len(new_solution[r]) - 1), 2))
                new_solution[r][a:b] = reversed(new_solution[r][a:b])
        
        # Calculate new max cost
        new_max_cost = max(tour_cost(new_solution[r]) for r in new
        # Decide if we accept the new solution
        if new_max_cost < best_max_cost:
            best_solution = new_solution
            best_max_solution = new_max_cost
            iteration_no_improve = 0
        else:
            iteration_no_improve += 1
        
        tours = best_solution
    
    return best_solution

# Perform the search
final_tours = variable_neighborhood_search()
max_cost = max(tour_cost(final_tours[r]) for r in final_tours)

# Output the solution
for r in final_tours:
    print(f"Robot {r} Tour: {final_tours[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_cost(final_tours[r])}")

print(f"Maximum Travel Cost: {max_cost}")