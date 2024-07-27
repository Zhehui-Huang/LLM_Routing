import numpy as np
import random

# City coordinates
CITIES = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Constants for the ACO
ALPHA = 1.0 
BETA = 5.0 
EVAPORATION_RATE = 0.5
PHEROMONE_DEPOSIT_AMOUNT = 100
NUM_ITERATIONS = 100
NUM_CITIES = len(CITIES)
NUM_ANTS = 20

def euclidean_distance(city1, city2):
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

distance_matrix = np.array([[euclidean_distance(i, j) for j in range(NUM_CITIES)] for i in range(NUM_CITIES)])
pheromones = np.ones((NUM_CITIES, NUM_CITIES))

def choose_next_city(current_city, allowable_cities, pheromoneliness):
    probabilities = []
    for next_city in allowable_cities:
        probability = (
            pheromoneliness[current_city, next_city]**ALPHA *
            ((1.0 / distance_matrix[current_city][next_city]) ** BETA)
        )
        probabilities.append(probability)

    probabilities_sum = sum(probabilities)
    probabilities = [p / probabilities_sum for p in probabilities]
    chosen_city = np.random.choice(allowable_cities, p=probabilities)
    return chosen_city

def update_pheromones(pheromoneliness, ant_tours, desirabilities):
    pheromoneliness *= (1 - EVAPORATION_RATE)
    for tour, desirability in zip(ant_tours, desirabilities):
        for i in range(len(tour) - 1):
            pheromoneliness[tour[i]][tour[i+1]] += PHEROMONE_DEPOSIT_AMOUNT / desirability

def ant_colony_optimization():
    best_route = None
    best_total_cost = np.inf

    for iteration in range(NUM_ITERATIONS):
        ant_tours = []
        tour_costs = []

        for ant in range(NUM_ANTS):
            start_city = random.randint(0, NUM_CITIES-1)
            tour = [start_city]
            current_city = start_city
            while len(tour) < NUM_CITIES:
                next_cities = [c for c in range(NUM_CITIES) if c not in tour]
                next_city = choose_next_city(current_city, next_cities, pheromones)
                tour.append(next_city)
                current_city = next_city
            tour.append(start_city)  # Complete the tour back to the start city
            tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            ant_tours.append(tour)
            tour_costs.append(tour_cost)

        update_pheromones(pheromones, ant_tours, tour_costs)

        min_cost = min(tour_costs)
        if min_cost < best_total_cost:
            best_total_cost = min_cost
            best_route = ant_tours[tour_costs.index(min_cost)]

    return best_route, best_total_cost

best_tour, best_cost = ant_colony_optimization()

print(f"Optimal tour: {best_tour}")
print(f"Total travel cost: {best_cost}")