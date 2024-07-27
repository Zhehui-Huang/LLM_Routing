import random
import math
from copy import deepcopy

# Parameters and city coordinates
n_robots = 4
depots = [0, 1, 2, 3]
city_coords = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

city_indices = list(city_coords.keys())
non_depot_cities = [city for city in city_indices if city not in depots]

# Distance calculation function
def calc_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

# Generate initial routes (tours)
def generate_initial_routes():
    random.shuffle(non_depot_cities)
    split_portions = random.choices(range(1, len(non_depot_cities)), k=n_robots-1)
    split_portions.sort()
    routes = []
    prev_index = 0
    for index in split_portions:
        routes.append(non_depot_cities[prev_index:index])
        prev_index = index
    routes.append(non_depot_cities[prev_index:])
    return routes

# Evaluate total cost of the whole set of routes
def total_cost(routes):
    total_cost = 0
    tour_details = []
    for robot_id, route in enumerate(routes):
        depot = depots[robot_id]
        tour = [depot] + route + [depot]
        cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost += cost
        tour_details.append((tour, cost))
    return total_cost, tour_details

# Genetic operators
def crossover(route1, route2):
    cross_pt = random.randint(1, min(len(route1), len(route2)) - 1)
    child1 = route1[:cross_pt] + [city for city in route2 if city not in route1[:cross_pt]]
    child2 = route2[:cross_pt] + [city for city in route1 if city not in route2[:cross_pt]]
    return child1, child2

def mutate(route):
    idx1, idx2 = random.sample(range(len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]

# Main Genetic Algorithm execution
population = [generate_initial_routes() for _ in range(20)]
best_routes = None
min_cost = float('inf')

for _ in range(1000):  # Number of generations
    # Evaluate population
    scored_population = [(deepcopy(routes), total_cost(routes)[0]) for routes in population]
    scored_population.sort(key=lambda x: x[1])

    # Selection
    population = [x[0] for x in scored_population[:10]]  # Top fitness

    if scored_population[0][1] < min_cost:
        min_cost = scored_population[0][1]
        best_routes = scored_population[0][0]

    # Crossover and mutation
    new_population = []
    while len(new_population) < 20:
        if random.random() > 0.8:  # Mutation probability
            route = random.choice(population)
            mutate(route[random.randint(0, n_robots-1)])
            new_population.append(route)
        else:  # Crossover probability
            parent1, parent2 = random.sample(population, 2)
            for i in range(n_robots):
                child1, child2 = crossover(parent1[i], parent2[i])
                new_population.extend([[child1 if j == i else parent1[j] for j in range(n_robots)],
                                       [child2 if j == i else parent2[j] for j in range(n_robots)]])
    population = new_population[:20]

# Final output formatting
_, detailed_costs = total_cost(best_routes)
overall_cost = sum(cost for _, cost in detailed_costs)
result_output = ""
for i, (tour, cost) in enumerate(detailed_costs):
    result_output += f"Robot {i} Tour: {tour}\nRobot {i} Total Travel Cost: {cost:.2f}\n"
result_output += f"\nOverall Total Travel Cost: {overall_cost:.2f}"
print(result_output)