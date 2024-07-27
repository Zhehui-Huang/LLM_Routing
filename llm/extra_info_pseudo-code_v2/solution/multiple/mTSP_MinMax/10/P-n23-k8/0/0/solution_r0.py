import math
import random

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),
    5: (52, 33), 6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Constants
NUM_ROBOTS = 8
DEPOT = 0

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def initialization():
    sorted_cities = sorted(list(cities.keys())[1:], key=lambda x: euclidean_distance(cities[x], cities[DEPOT]))
    tours = [[] for _ in range(NUM_ROBOTS)]
    for i, city in enumerate(sorted_cities):
        tours[i % NUM_ROBOTS].append(city)
    for tour in tours:
        tour.insert(0, DEPOT)
        tour.append(DEPOT)
    return tours

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

def gvns(tours, max_iterations=100):
    best_tours = tours
    best_max_cost = max([calculate_tour_cost(tour) for tour in best_tours])
    
    for _ in range(max_iterations):
        # Shaking
        new_tours = [
            tour[1:-1].copy() for tour in best_tours
        ]
        for tour in new_tours:
            if len(tour) > 1:
                i, j = random.sample(range(len(tour)), 2)
                tour[i], tour[j] = tour[j], tour[i]
        new_tours = [([DEPOT] + tour + [DEPOT]) for tour in new_tours]
        
        # Calculate new max cost
        new_max_cost = max([calculate_tour_cost(tour) for tour in new_tours])
        
        if new_max_cost < best_max_cost:
            best_tours = new_tours
            best_max_cost = new_max_cost
            
    return best_tours, best_max_cost

def main():
    initial_tours = initialization()
    optimized_tours, max_cost = gvns(initial_tours, max_iterations=1000)
    
    for idx, tour in enumerate(optimized_tours):
        tour_cost = calculate_tour_cost(tour)
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")
        
    print(f"Maximum Travel Cost: {max_cost:.2f}")

main()