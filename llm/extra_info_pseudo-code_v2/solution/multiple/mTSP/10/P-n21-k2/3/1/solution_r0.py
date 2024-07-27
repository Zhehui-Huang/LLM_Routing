import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour, cities):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def solve_mTSP(cities, num_robots):
    # Initialize without the depot city for permutations
    city_indices = list(range(1, len(cities)))
    
    # Best configuration variable initialization
    best_total_cost = float('inf')
    best_tour_configuration = []
    
    # Iterate through all possible permutations of the cities (without the depot)
    for perm in permutations(city_indices):
        # Segment the cities into roughly equal parts for each robot
        segments = []
        part_size = len(perm) // num_robots
        for i in range(num_robots):
            # Determine the segment of the cities handled by each robot
            start_idx = i * part_size
            end_idx = start_idx + part_size if i != num_robots - 1 else len(perm)
            segments.append([0] + list(perm[start_idx:end_idx]) + [0])  # Adding depot at start and end of each tour
        
        # Calculate the cost of the current configuration
        current_cost = sum(total_tour_cost(tour, cities) for tour in segments)
        if current_cost < best_total_cost:
            best_total_cost = current_cost
            best_tour_configuration = segments
    
    return best_tour_configuration, best_total_cost

# Define coordinates for each city including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]
num_robots = 2

# Solve the mTSP
best_tours, best_total_cost = solve_mTSP(cities, num_robots)

# Output the results
for robot_id, tour in enumerate(best_tours):
    tour_cost = total_tour_cost(tour, cities)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {best_total_cost}")