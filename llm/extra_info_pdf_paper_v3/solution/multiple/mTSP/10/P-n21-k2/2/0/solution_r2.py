import numpy as np

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35)
}

# Distance function
def distance(city1, city2):
    return np.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Compute the cost of a tour
def compute_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# 2-opt optimization
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 2, len(tour)):
                if distance(tour[i-1], tour[i]) + distance(tour[j], tour[j+1]) > \
                   distance(tour[i-1], tour[j]) + distance(tour[i], tour[j+1]):
                    tour[i:j] = reversed(tour[i:j])
                    improved = True
    return tour

# Divide cities between two robots
robot1_cities = [0] + list(range(1, 11)) + [0]
robot2_cities = [0] + list(range(11, 21)) + [0]

# Optimally rearrange each robot's tour using 2-opt
optimized_robot1_tour = two_opt(robot1_cities)
optimized_robot2_tour = two_opt(robot2_cities)

# Calculate the travel costs
robot1_cost = compute_cost(optimized_robot1_tour)
robot2_cost = compute_cost(optimized_robot2_tour)
total_cost = robot1_cost + robot2_cost

# Output the results
print(f"Robot 0 Tour: {optimized_robot1_tour}")
print(f"Robot 0 Total Travel Cost: {robot1_cost}")
print(f"Robot 1 Tour: {optimized_robot2_tour}")
print(f"Robot 1 Total Travel Cost: {robot2_cost}")
print(f"Overall Total Travel Cost: {total_cost}")