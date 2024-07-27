import math
import random

# Define the Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of cities including depots
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Number of robots and their start location at depot 0
num_robots = 8
start_depot = 0

# Precompute distances between each pair of cities
city_count = len(cities_coordinates)
distances = [[0 for _ in range(city_count)] for _ in range(city_count)]
for i in range(city_count):
    for j in range(city_count):
        distances[i][j] = euclidean_distance(cities_coordinates[i], cities_coordinates[j])

# Simulated Annealing function
def simulated_annealing(start_tour):
    temperature = 10000
    cooling_rate = 0.003
    current_solution = start_tour[:]
    current_cost = path_cost(current_solution)
    
    while temperature > 1:
        new_solution = current_solution[:]
        l = random.randint(1, len(current_solution) - 2)
        r = random.randint(l + 1, len(current_solution) - 1)
        new_solution[l:r+1] = reversed(new_solution[l:r+1])
        new_cost = path_cost(new_solution)

        if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / temperature):
            current_solution = new_solution
            current_cost = new_cost

        temperature *= 1 - cooling_rate
    
    return current_solution, current_cost

# Calculate the travel cost of the tour
def path_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Assign initial round-robin tours starting from depot 0
robot_tours = [[] for _ in range(num_robots)]
city_assignments = list(range(1, city_count))
random.shuffle(city_assignments)

for idx, city in enumerate(city_assignments):
    robot_tours[idx % num_robots].append(city)

# Incorporate depot into each tour for starting and potentially ending
for tour in robot_tours:
    tour.insert(0, start_depot)  # Start from depot
    # tour.append(start_depot)  # If returning to depot was necessary

# Process each tour with simulated annealing and calculate costs
total_travel_cost = 0
for idx, tour in enumerate(robot_tours):
    optimized_tour, travel_cost = simulated_annealing(tour)
    total_travel_cost += travel_cost
    print(f"Robot {idx} Tour: {optimized_tour}")
    print(f"Robot {idx} Total Travel Cost: {travel_cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")