import math
import random

# Defining cities coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of robots
num_robots = 4

# Initialize robots' tours starting from the depot (city 0 for all)
robots_tours = [[0] for _ in range(num_robots)]

# Remaining cities to visit
remaining_cities = list(cities.keys())[1:]

# Function to perform simulated annealing
def simulated_annealing(tour):
    temp = 10000
    cooling_rate = 0.995
    while temp > 1:
        new_tour = tour[:]
        i = random.randint(1, len(tour) - 2)
        j = random.randint(1, len(tour) - 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        old_cost = sum(distance(tour[k], tour[k+1]) for k in range(len(tour)-1))
        new_cost = sum(distance(new_tour[k], new_tour[k+1]) for k in range(len(new_tour)-1))
        if new_cost < old_cost or random.random() < math.exp((old_cost - new_cost) / temp):
            tour = new_tour[:]
        temp *= cooling_rate
    return tour

# Assign cities to robots (initially random but ensuring all cities are covered)
random.shuffle(remaining_cities)
slice_size = len(remaining_cities) // num_robots
start = 0
for i in range(num_robots):
    if i == num_robots - 1:
        robots_tours[i].extend(remaining_cities[start:])
    else:
        robots_tours[i].extend(remaining_cities[start:start + slice_size])
    start += slice_size
    robots_tours[i].append(0)  # Add end point as the depot for a complete tour

# Apply Simulated Annealing to each robot's tour
for i in range(num_robots):
    robots_tours[i] = simulated_annealing(robots_tours[i])

# Output results
total_cost = 0
for i, tour in enumerate(robots_tours):
    tour_cost = sum(distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")