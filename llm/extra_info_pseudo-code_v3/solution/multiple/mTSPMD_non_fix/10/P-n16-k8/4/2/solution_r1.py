import numpy as np

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Using a simple heuristic to generate initial tours using Nearest Neighbors
def nearest_neighbor_tours(num_robots, start_depot):
    # Initialize tours and tracking remaining cities
    tours = {i: [start_depot] for i in range(num_robots)}
    remaining_cities = set(cities.keys()) - {start_depot}
    current_position = [start_depot] * num_robots
    assignments = [[] for _ in range(num_robots)]
    
    while remaining_cities:
        for i in range(num_robots):
            if remaining_cities:
                nearest = min(remaining_cities, key=lambda x: calculate_distance(current_position[i], x))
                tours[i].append(nearest)
                current_position[i] = nearest
                remaining_cities.remove(nearest)
    
    return tours

# Calculate tour cost
def tour_cost(tour):
    total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    return total_cost

# Main execution to get and print results
def main():
    num_robots = 8
    start_depot = 0
    tours = nearest_neighbor_tours(num_robots, start_depot)
    total_cost = 0

    for i, tour in tours.items():
        cost = tour_cost(tour)
        total_cost += cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

main()