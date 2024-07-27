import numpy as np
import math
import random

# City coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Number of robots
num_robots = 4
# Robots start at depot 0
start_depot = 0

# Distance calculation using Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize temperature and cooling factor for SA
def simulated_annealing(tour):
    T = 1000
    alpha = 0.995
    min_temp = 1
    
    current_route = tour.copy()
    current_cost = calculate_total_distance(current_route)
    
    while T > min_temp:
        new_route = current_route.copy()
        # Swap two cities randomly
        i, j = np.random.randint(1, len(new_route) - 1), np.random.randint(1, len(new_route) - 1)
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_cost = calculate_total_distance(new_route)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_route = new_route
            current_cost = new_cost
        T *= alpha

    return current_route, current_cost

# Calculate total travel distance of a tour
def calculate_total_distance(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Split cities into segments for each robot
def segment_cities(cities, num_segments):
    segments = []
    keys = list(cities.keys())[1:]  # Exclude the depot from the tour
    random.shuffle(keys)  # Shuffle to randomize initial tours
    for i in range(num_segments):
        segments.append([start_depot] + keys[i::num_segments] + [start_depot])
    return segments

# Main function to determine routes
def main():
    tours = segment_cities(cities, num_robots)
    total_overall_cost = 0

    # Optimize each tour using simulated annealing
    for idx, tour in enumerate(tours):
        optimized_tour, tour_cost = simulated_annealing(tour)
        print(f"Robot {idx} Tour: {optimized_tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")
        total_overall_cost += tour_cost

    print(f"Overall Total Travel Cost: {total_overall_cost:.2f}")

if __name__ == "__main__":
    main()