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

# Number of robots
num_robots = 4
tours = {k: [0] for k in range(num_robots)}

# Distribute cities among robots, excluding depot city 0
city_ids = list(cities.keys())[1:]  # exclude depot
random.shuffle(city_ids)

for i, city in enumerate(city_ids):
    tours[i % num_robots].append(city)

# Close each robot's tour at the depot
for k in tours:
    tours[k].append(0)

# Function to calculate total travel cost of a tour
def tour_cost(tour):
    total = 0
    for i in range(len(tour)-1):
        total += distance(tour[i], tour[i+1])
    return total

# Variable Neighborhood Search optimized function
def variable_neighborhood_search(tours, max_iterations=10000):
    best_solution = tours.copy()
    best_max_cost = max(tour_cost(tours[r]) for r in tours)

    for _ in range(max_iterations):
        # Shaking: slightly modify the solution
        new_solution = {r: tours[r][:] for r in tours}
        for r in new_solution:
            if len(new_solution[r]) > 3: # More than just depot back and forth
                a, b = sorted(random.sample(range(1, len(new_solution[r]) - 1), 2))
                new_solution[r][a:b+1] = new_solution[r][a:b+1][::-1]

        # Acceptance criterion: if new solution has a lower max tour cost
        new_max_cost = max(tour_cost(new_solution[r]) for r in new_solution)
        if new_max_cost < best_max_cost:
            best_solution = new_solution.copy()
            best_max_cost = new_max_cost

    return best_solution

optimized_tours = variable_neighborhood_search(tours)

# Reporting results
for r in optimized_tours:
    robot_tour = optimized_tours[r]
    cost = tour-a_cost(robot_tour)
    print(f"Robot {r} Tour: {robot_tour}")
    print(f"Robot {r} Total Travel Cost: {cost}")

max_travel_cost = max(tour_cost(optimized_tours[r]) for r in optimized_tours)
print(f"Maximum Travel Cost: {max_travel_cost}")