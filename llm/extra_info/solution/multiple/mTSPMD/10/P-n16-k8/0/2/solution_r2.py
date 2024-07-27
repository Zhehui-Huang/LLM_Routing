import math
import itertools

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distance between two city indices
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize tours for each robot, each starts and ends at their respective depot
robot_tours = {i: [i] for i in range(8)}
remaining_cities = list(range(8, 16))

# Brute force method to assign cities to each robot
def find_best_routes():
    best_total_cost = float('inf')
    best_routes = None
    
    # Generate all partitions of 8 cities into 8 parts (very computationally expensive)
    for partition in set(itertools.permutations(remaining_cities)):
        parts = [list(partition[i:i+1]) for i in range(0, 8, 1)]  # Dividing cities into chunks for each robot
        local_tours = {i: [i] + parts[i] + [i] for i in range(8)}
        local_cost = 0
        
        # Calculate travel cost for each robot's tour
        for r in range(8):
            tour_cost = sum(distance(local_tours[r][j], local_tours[r][j+1]) for j in range(len(local_tours[r])-1))
            local_cost += tour_cost
        
        # If found a better division of cities, update
        if local_cost < best_total_cost:
            best_total_cost = local_cost
            best_routes = local_tours
    
    return best_routes, best_total_cost

# Execute function to find optimal solution
best_robot_tours, best_overall_cost = find_best_routes()

# Print each robot's tour and calculate and print individual and total costs
total_cost = 0
for robot in range(8):
    tour = best_robot_tours[robot]
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")