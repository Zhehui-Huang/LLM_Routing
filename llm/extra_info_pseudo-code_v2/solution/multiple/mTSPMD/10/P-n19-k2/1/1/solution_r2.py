import math
import random

# List of cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def initialize_pheromone(num_cities, init_trail):
    return [[init_trail for _ in range(num_cities)] for _ in range(num_cities)]

def initialize_visibility(num_cities):
    return [[0 if i == j else 1 / distance(i, j)
             for j in range(num_cities)] for i in range(num_cities)]

def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def select_next_city(probabilities):
    total = sum(p for _, p in probabilities)
    r = random.uniform(0, total)
    cum_sum = 0
    for city, p in probabilities:
        cum_sum += p
        if cum < r:
            return city
    return probabilities[-1][0]  # return the last city if not chosen by random chance

def transition_probabilities(current_city, allowed, pheromone, visibility, alpha, beta):
    denominator = sum((pheromone[current_city][j] ** alpha) * (visibility[current_city][j] ** beta) for j in allowed)
    probabilities = []
    for j in allowed:
        numerator = (pheromone[current_city][j] ** alpha) * (visibility[current_city][j] ** beta)
        probability = numerator / denominator if denominator != 0 else 0
        probabilities.append((j, probability))
    return probabilities

# Parameters
num_cities = len(cities)
antnum = 20
cyclenum = 100
init_trail = 1.0
alpha = 1
beta = 5
rho = 0.1

pheromone = initialize_pheromone(num_cities, init_trail)
visibility = initialize_visibility(num_cities)

best_cost = float('inf')
best_tour = None
best_robot_tours = []
total_best_cost = 0

for _ in range(cyclenum):
    for robot_id in [0, 1]:  # two robots
        start_city = robot_id
        all_tours = []
        all_costs = []

        for _ in range(antnum):
            tour = [start_city]
            current_city = start_city
            allowed = list(set(range(num_cities)) - {current_city})

            while allowed:
                probabilities = transition_probabilities(current_city, allowed, pheromone, visibility, alpha, beta)
                next_city = select_next_city(probabilities)
                tour.append(next_city)
                allowed.remove(next_city)
                current_city = next_city

            tour.append(start_city)  # Return to depot
            cost = calculate_tour_cost(tour)
            all_tours.append(tour)
            all_costs.append(cost)

            # Pheromone update rule
            for i in range(len(tour) - 1):
                a, b = tour[i], tour[i+1]
                pheromone[a][b] += 1 / cost
                pheromone[b][a] += 1 / cost
        
        if min(all_costs) < best_cost:
            best_cost = min(all_costs)
            best_tour = all_tours[all_costs.index(best_cost)]
            best_robot_tours.append(best_tour)
            total_best_cost += best_cost

        # Evaporation
        pheromone = [[(1 - rho) * phero for phero in row] for row in pheromone]

# Output the results for both robots
for i, tour in enumerate(best_robot_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {calculate_tour_cost(tour)}")

print(f"Overall Total Travel Cost: {total_best_cost}")