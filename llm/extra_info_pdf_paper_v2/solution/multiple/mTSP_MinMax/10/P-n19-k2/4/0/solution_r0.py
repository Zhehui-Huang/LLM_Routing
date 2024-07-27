import math
import random

# Define the coordinates for each city
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 
                     + (city_coords[city1][1] - city_coords[city2][1])**2)

# Number of robots
num_robots = 2

# Simulated Annealing to optimize the solution
def simulated_annealing(tours):
    T = 100.0  # Initial temperature
    Tmin = 1.0  # Minimum temperature
    alpha = 0.9  # Cooling rate

    while T > Tmin:
        for _ in range(100):  # Number of iterations at each temperature
            # Select a random robot and two cities (not the depot) to swap in its tour
            robot_id = random.randint(0, num_robots - 1)
            tour_length = len(tours[robot_id])
            if tour_length <= 4:
                continue
            i, j = random.sample(range(1, tour_length - 1), 2)
            # Swap cities and calculate new cost
            new_tour = tours[robot_id][:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = sum(distance(new_tour[k], new_tour[k + 1]) for k in range(len(new_tour) - 1))
            old_cost = sum(distance(tours[robot_id][k], tours[robot_id][k + 1]) for k in range(len(tours[robot_id]) - 1))
            # Accept the new tour if it reduces the maximum travel distance, or with a probability depending on the temperature
            max_old_cost = max(sum(distance(tours[id][k], tours[id][k + 1]) for k in range(len(tours[id]) - 1)) for id in range(num_robots))
            tours[robot_id] = new_tour
            max_new_cost = max(sum(distance(tours[id][k], tours[id][k + 1]) for k in range(len(tours[id]) - 1)) for id in range(num_robots))
            if max_new_cost < max_old_cost or random.random() < math.exp((max_old_cost - max_new_cost) / T):
                tours[robot_id] = new_tour
            else:
                tours[robot_id] = tours[robot_id]  # revert to the old tour

        T *= alpha  # Reduce the temperature

    return tours

# Distribute cities (simple greedy by closest next city, needs further sophistication for better optimization)
cities = list(range(1, len(city_coords)))
tours = [[0] for _ in range(num_robots)]
current_cities = [0] * num_robots

while cities:
    for r in range(num_robots):
        if not cities:
            break
        nearest_city = min(cities, key=lambda x: distance(current_cities[r], x))
        tours[r].append(nearest_city)
        current_cities[r] = nearest_city
        cities.remove(nearest_city)

# Append the depot at the end of each tour
for tour in tours:
    tour.append(0)

# Optimize the initial solution with Simulated Annealing
tours = simulated_annealing(tours)

# Calculate costs and maximum cost
costs = [sum(distance(tours[r][i], tours[r][i + 1]) for i in range(len(tours[r]) - 1)) for r in range(num_robots)]
max_cost = max(costs)

# Output results
for r in range(num_robots):
    print(f"Robot {r} Tour: {tours[r]}")
    print(f"Robot {r} Total Travel Cost: {costs[r]}")
print(f"Maximum Travel Cost: {max_cost}")