import math
import random
from itertools import permutations

# City coordinates
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
          (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
          (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
          (61, 33), (62, 63), (63, 69), (45, 35)]

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initialize tours
def initialize_tours(num_robots):
    all_cities = list(range(1, len(cities)))  # Exclude the depot city 0
    random.shuffle(all_cities)
    tours = [[] for _ in range(num_robots)]
    for i, city in enumerate(all_cities):
        tours[i % num_robots].append(city)
    # Return to depot and start from depot
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
    return tours

# Calculate tour cost
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Shaking procedure: Swap random cities between two tours
def shake(tours):
    robot1, robot2 = random.sample(range(len(tours)), 2)
    if len(tours[robot1]) > 2 and len(tours[robot2]) > 2:
        index1, index2 = random.randint(1, len(tours[robot1])-2), random.randint(1, len(tours[robot2])-2)
        tours[robot1][index1], tours[robot2][index2] = tours[robot2][index2], tours[robot1][index1]

# Optimize tour using 2-opt within each tour
def local_optimization(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+2, len(tour) - 1):
                if distance(tour[i], tour[i+1]) + distance(tour[j], tour[j+1]) > distance(tour[i], tour[j]) + distance(tour[i+1], tour[j+1]):
                    tour[i+1:j+1] = tour[j:i:-1]
                    improved = True

# Perform GVNS
def gvns(num_robots, kmax, tmax):
    tours = initialize_tours(num_robots)
    best_solution = tours.copy()
    best_max_cost = max(calculate_tour_cost(tour) for tour in tours)

    time = 0
    k = 1

    while time < tmax:
        while k < kmax:
            shaken_tours = [tour[:] for tour in tours]
            shake(shaken_tours)
            for tour in shaken_tours:
                local_optimization(tour)
            max_cost = max(calculate_tour_cost(tour) for tour in shaken_tours)
            if max_cost < best_max_cost:
                best_solution = shaken_tours.copy()
                best_max_cost = max_cost
                k = 1
            else:
                k += 1
        time += 1

    return best_solution, best_max_cost

# Simulation parameters: 2 robots, maximum of 5 shakes, and 100 units of time limit
best_solution, best_max_cost = gvns(2, 5, 100)

# Printing the results
for i, tour in enumerate(best_solution):
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Maximum Travel Cost: {best_max_cost:.2f}")