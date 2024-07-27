import math
import random

# Define cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

# Distance calculation function
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the total distance of a tour
def calculate_total_distance(tour):
    total_distance = distance(cities[tour[0]], cities[tour[-1]])  # Close the loop
    for i in range(len(tour) - 1):
        total_distance += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Simulated Annealing algorithm
def simulated_annealing(tour, initial_temp, cooling_rate, min_temp):
    current_temp = initial_temp
    current_tour = tour[:]
    current_distance = calculate_total_distance(current_tour)

    while current_temp > min_temp:
        i = random.randint(1, len(current_tour) - 3)
        j = random.randint(i + 1, len(current_tour) - 2)

        # Create new tour with two nodes swapped
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_distance = calculate_total_distance(new_tour)

        # Accept new tour if the distance is shorter or by probability condition
        if new_distance < current_distance or math.exp((current_distance - new_distance) / current_temp) > random.random():
            current_tour = new_tour
            current_distance = new_distance

        current_temp *= cooling_rate

    return current_tour, current_distance

# Assign cities evenly to the robots
def assign_cities_to_robots():
    shuffled_cities = list(range(1, len(cities)))  # ignore the main depot initially
    random.shuffle(shuffled_cities)
    strips = [shuffled_cities[i::num_robots] for i in range(num_robots)]

    return [[0] + strip for strip in strips]  # Assign each robot to start from depot

def find_optimal_tours():
    assigned_routes = assign_cities_to_robots()
    total_cost = 0
    
    for i, route in enumerate(assigned_routes):
        route.append(0)  # Make sure to close the loop back to depot
        optimized_route, route_cost = simulated_annealing(route, 10000, 0.995, 1)
        print(f"Robot {i} Tour: {optimized_route}")
        print(f"Robot {i} Total Travel Cost: {route_cost}")
        total_cost += route_cost

    print("Overall Total Travel Cost:", total_cost)

# Run the optimization function
find_optimal_tours()