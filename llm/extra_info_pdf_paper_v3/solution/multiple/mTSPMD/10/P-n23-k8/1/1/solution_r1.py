import math
import random

# Define city coordinates for 23 cities indexed from 0 to 22
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Robot start/end locations (depot cities)
depots = [0, 1, 2, 3, 4, 5, 6, 7]

def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_route_cost(route):
    return sum(calc_distance(route[i], route[i+1]) for i in range(len(route)-1))

# Assign cities to nearest depot
def assign_cities_to_depots():
    assignments = {depot: [] for depot in depots}
    for city_idx in range(len(cities)):
        if city_idx in depots:
            assignments[city_idx].append(city_idx)
        else:
            nearest_depot = min(depots, key=lambda d: calc_distance(city_idx, d))
            assignments[nearest_depot].append(city_idx)
    return assignments

# Apply a genetic algorithm approach to solve each depot's routing problem
def genetic_algorithm(depot, assigned_cities, population_size=100, generations=1000, mutation_rate=0.01):
    population = [[city for city in assigned_cities] for _ in range(population_size)]
    for _ in range(generations):
        population = sorted(population, key=total_route_cost)
        next_gen = population[:2]  # Elitism: carry the best solutions to the next generation
        while len(next_gen) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)
            child1, child2 = pmx(parent1, parent2)
            next_gen.append(mutate(child1, mutation_rate))
            if len(next_gen) < population_size:
                next_gen.append(mutate(child2, mutation_rate))
        population = next_gen
    best_solution = min(population, key=total_route_cost)
    return best_solution

def solve_mmTSP():
    city_assignments = assign_cities_to_depots()
    total_cost = 0
    results = {}
    
    for depot, cities in city_assignments.items():
        if cities:
            route = [depot] + genetic_algorithm(depot, cities[1:]) + [depot]
            cost = total_route_cost(route)
            total_cost += cost
            results[depot] = (route, cost)
    
    return results, total_cost

# Executing the above-defined solution
if __name__ == "__main__":
    results, overall_cost = solve_mmTSP()
    for robot_id, (tour, cost) in results.items():
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}\n")
    print(f"Overall Total Travel Cost: {overall_cost:.2f}")