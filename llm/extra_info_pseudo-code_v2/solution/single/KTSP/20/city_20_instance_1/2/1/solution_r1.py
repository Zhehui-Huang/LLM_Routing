import random
import math

# Constants and city coordinates
NUM_CITIES = 20
TOUR_SIZE = 7  # Including the depot
COORDINATES = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def calculate_distance(city1, city2):
    x1, y1 = COORDINATES[city1]
    x2, y2 = COORDINATES[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    cities = list(range(1, NUM_CITIES))
    random.shuffle(cities)
    initial_tour = [0] + cities[:TOUR_SIZE-1] + [0]
    return initial_tour

def shake(tour, k):
    new_tour = tour[1:-1]
    for _ in range(k):
        i, j = random.sample(range(len(new_tour)), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return [0] + new_tour + [0]

def local_search(tour):
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, TOUR_SIZE-1):
            for j in range(i+1, TOUR_SIZE):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    made_improvement = True
    return best_tour

def gvns(max_iter=100):
    best_tour = generate_initial_solution()
    best_cost = tour_cost(best_tour)
    for _ in range(max_iter):
        k = 1
        while k <= 3:
            new_tour = shake(best_tour, k)
            new_tour = local_search(new_tour)
            new_cost = tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
                k = 1  # Reset k to 1 upon finding a better solution
            else:
                k += 1
    return best_tour, best_cost

# Execute the algorithm
final_treat, total_cost = gvns()
print("Tour:", final_treat)
print("Total Travel Cost:", total_cost)