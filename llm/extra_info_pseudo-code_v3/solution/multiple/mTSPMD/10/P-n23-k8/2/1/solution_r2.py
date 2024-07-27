import random
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def create_individual(cities, depots, num_robots):
    random.shuffle(cities)
    parts = random.sample(range(1, len(cities)), num_robots - 1)
    parts = [0] + sorted(parts) + [len(cities)]
    return [cities[parts[i]:parts[i+1]] for i in range(num_robots)]

def calculate_cost(tours, coordinates, depots):
    total_cost = 0
    detailed_costs = []
    for depot, tour in zip(depots, tours):
        full_tour = [depot] + tour + [depot]
        cost = sum(euclidean_distance(coordinates[full_tour[i]], coordinates[full_tour[i + 1]]) for i in range(len(full_tour) - 1))
        detailed_costs.append((full_tour, cost))
        total_cost += cost
    return total_cost, detailed_results

def crossover(tour1, tour2):
    cut1, cut2 = sorted(random.sample(range(len(tour1)), 2))
    middle_tour1 = tour1[cut1:cut2]
    reduced_tour2 = [city for city in tour2 if city not in middle_tour1]
    return reduced_tour2[:cut1] + middle_tour1 + reduced_tour2[cut1:]

def mutate(tour):
    idx1, idx2 = random.sample(range(len(tour)), 2)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

def genetic_algorithm(city_coords, depots, num_robots, generations=1000, population_size=100):
    cities = [i for i in range(len(city_coords)) if i not in depots]
    
    population = [create_individual(cities, depots, num_robots) for _ in range(population_size)]
    for _ in range(generations):
        new_population = []
        for tours in population:
            if random.random() < 0.1:
                for tour in tours:
                    mutate(tour)
            other_tours = random.choice(population)
            children = [crossover(tours[i], other_tours[i]) for i in range(num_robots)]
            new_population.append(children)
        population = new_population
    
    best_tours = min(population, key=lambda t: calculate_cost(t, city_coords, depots)[0])
    best_cost, detailed_tours = calculate_cost(best_tours, city_coords, depots)
    return detailed_tours, best_cost

# Data Preprocessing
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = 8

# Execute Genetic Algorithm
tours_info, total_travel_cost = genetic_algorithm(city_coords, depots, num_robots)

# Output of results
for index, (tour, cost) in enumerate(tours_info):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")