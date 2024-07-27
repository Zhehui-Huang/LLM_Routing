import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def create_initial_route(depot):
    non_depot_cities = [city for city in cities if city not in range(8) and city != depot]
    random.shuffle(non_depot_cities)
    return [depot] + non_depot_cities + [depot]

def compute_route_cost(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 2, len(route) - 1):
                if distance(route[i], route[i-1]) + distance(route[j+1], route[j]) > distance(route[i], route[j]) + distance(route[i-1], route[j+1]):
                    best[i:j+1] = reversed(best[i:j+1])
                    improved = True
    return best

def genetic_algorithm(depot, iterations=1000, population_size=10):
    population = [create_initial_route(depot) for _ in range(population_size)]
    scores = [compute_route_cost(route) for route in population]

    for _ in range(iterations):
        # Tournament Selection
        tournament_size = 3
        new_population = []
        for _ in range(population_size):
            selected = random.sample(list(zip(population, scores)), tournament_size)
            best_individual = min(selected, key=lambda x: x[1])[0]
            new_population.append(two_opt(best_individual[:]))
        population = new_population
        scores = [compute_route_cost(route) for route in population]

    best_score = min(scores)
    best_index = scores.index(best_score)
    best_route = population[best_index]
    return best_route, best_score

total_cost = 0
for robot_id in range(8):
    best_route, best_score = genetic_algorithm(robot_id)
    total_cost += best_score
    print(f'Robot {robot_id} Tour: {best_route}')
    print(f'Robot {robot_id} Total Travel Cost: {best_score}')

print(f'Overall Total Travel Cost: {total_cost}')