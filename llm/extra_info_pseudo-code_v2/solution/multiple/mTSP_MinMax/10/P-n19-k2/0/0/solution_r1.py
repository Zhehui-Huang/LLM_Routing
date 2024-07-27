import math
import random

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialization of tours (greedy heuristic based on nearest cities)
def initialize_tours(cities, num_robots):
    sorted_cities = sorted(range(1, len(cities)), key=lambda x: euclidean_distance(cities[0], cities[x]))
    tours = {i: [0] for i in range(num_robots)}
    for index, city in enumerate(sorted_cities):
        min_tour = min(tours, key=lambda k: euclidean_distance(cities[tours[k][-1]], cities[city]))
        tours[min_tour].append(city)
    for t in tours:
        tours[t].append(0)  # End the tour at the depot
    return tours

# Calculate the cost of a tour
def calculate_tour_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Shaking the solution by randomly swapping cities between tours
def shake(tours, k, cities):
    keys = list(tours.keys())
    while k > 0:
        r1, r2 = random.sample(keys, 2)
        if len(tours[r1]) > 2 and len(tours[r2]) > 2:
            i1, i2 = random.randint(1, len(tours[r1]) - 2), random.randint(1, len(tours[r2]) - 2)
            tours[r1][i1], tours[r2][i2] = tours[r2][i2], tours[r1][i1]
            k -= 1
    return tours

# Implement the GVNS method
def gvns(cities, num_robots, k_max, l_max, t_max):
    tours = initialize_tours(cities, num_robots)
    best_tours = tours.copy()
    best_max_cost = max(calculate_tour_cost(tours[t], cities) for t in tours)
    
    iteration = 0
    while iteration < t_max:
        current_tours = shake(tours.copy(), k_max, cities)
        for l in range(1, l_max + 1):
            for tour_key in list(current_tours.keys()):
                current_cost = calculate_tour_cost(current_tours[tour_key], cities)
                for i in range(1, len(current_tours[tour_key])-1):
                    for j in range(i + 2, len(current_tours[tour_key])):
                        new_tour = current_tours[tour_key][:i] + current_tours[tour_key][i:j][::-1] + current_tours[tour_key][j:]
                        new_cost = calculate_tour_cost(new_tour, cities)
                        if new_cost < current_cost:
                            current_tours[tour_key] = new_tour
                            current_cost = new_cost
        
        max_cost = max(calculate_tour_cost(current_tours[t], cities) for t in current_tours)
        if max_cost < best_max_cost:
            best_tours = current_tours.copy()
            best_max_cost = max_cost
            
        iteration += 1
    
    return best_tours

# Define cities coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Constants for the GVNS
num_robots = 2
k_max = 5
l_max = 5
t_max = 10

# Execute the algorithm
solution_tours = gvns(cities, num_robots, k_max, l_max, t_max)

# Print results
max_cost = 0
for robot_id, tour in solution_tours.items():
    cost = calculate_tour_cost(tour, cities)
    max_cost = max(max_cost, cost)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Maximum Travel Corken Costray Cost: {max_cost}")