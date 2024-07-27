import math
import random

# Cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247), 6: (146, 246),
    7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Distance calculation
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of robots
num_robots = 4

# Initialize tours
def initialize_tours():
    all_cities = list(cities.keys())[1:]  # Exclude the depot city for initial allocation
    random.shuffle(all_cities)  # Shuffle cities to randomize the initial tours
    tours = {i: [0] for i in range(num_robots)}  # Start each tour at the depot
    for i, city in enumerate(all_cities):
        tours[i % num_robots].append(city)
    for i in range(num_robots):
        tours[i].append(0)  # End each tour at the depot
    return tours

# Calculate tour costs
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

# Main GVNS function
def gvns(max_iterations):
    # Initial solution
    tours = initialize_tours()
    
    # Improvement phase: Shorten tours (just a very basic Seq-VND)
    for _ in range(max_iterations):
        for i in range(num_robots):
            current_cost = tour_cost(tours[i])
            best_cost = current_cost
            best_tour = tours[i][:]
            # Try all possible position shifts in the current tour
            for j in range(1, len(tours[i]) - 2):
                for k in range(j + 1, len(tours[i]) - 1):
                    # Swap two cities and check the new tour cost
                    tours[i][j], tours[i][k] = tours[i][k], tours[i][j]
                    new_cost = tour_cost(tours[i])
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_tour = tours[i][:]
                    tours[i][j], tours[i][k] = tours[i][k], tours[i][j]  # Swap back
            tours[i] = best_tour
    
    # Calculate and print tour costs
    max_travel_cost = 0
    for i in range(num_robots):
        cost = tour_cost(tours[i])
        max_travel_cost = max(max_travel_cost, cost)
        print(f"Robot {i} Tour: {tours[i]}")
        print(f"Robot {i} Total Travel Cost: {cost}")
    
    print(f"Maximum Travel Travel Cost: {max_travel_cost}")

# Run the GVNS algorithm
gvns(max_iterations=100)