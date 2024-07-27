import random
import math
from itertools import permutations

# Given city coordinates (including depots)
coordinates = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

def euclidean_distance(from_id, to_id):
    return math.hypot(coordinates[to_id][0] - coordinates[from_id][0], coordinates[to_id][1] - coordinates[from_id][1])

# Initialize tours starting all robots from depot city 0
def initial_solution(city_ids, num_robots):
    cities = city_ids.copy()
    random.shuffle(cities)
    avg = len(cities) // num_robots
    tours = [cities[i:i + avg] for i in range(0, num_robots*avg, avg)]
    # Handle the case where not evenly divisible
    if len(cities) % num_robots != 0:
        for i in range(len(cities) % num_robots):
            tours[i].append(cities[num_robots*avg + i])
    # Starting from depot
    for tour in tours:
        tour.insert(0, 0)
    return tours

# Calculate tours costs
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def calculate_total_cost(tours):
    return sum(calculate_tour_cost(tour) for tour in tours)

def simulated_annealing(tours, num_iterations=10000, temperature=1000, cooling_rate=0.997):
    current_tours = tours
    best_tours = tours[:]
    current_cost = calculate_total_cost(current_tours)
    best_cost = current_cost

    for _ in range(num_iterations):
        temperature *= cooling_rate
        new_tours = current_tours[:]
        tour_id = random.randint(0, len(new_tours) - 1)
        if len(new_tours[tour_id]) > 2:
            # Choose two indexes to swap that are not the initial depot
            i, j = sorted(random.sample(range(1, len(new_tours[tour_id])), 2))
            new_tours[tour_id][i], new_tours[tour_id][j] = new_tours[tour_id][j], new_tours[tour_id][i]
            new_cost = calculate_total_cost(new_tours)
            
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
                current_tours = new_tours
                current_cost = new_cost

            if current_cost < best_cost:
                best_cost = current_cost
                best_tours = current_tours[:]
                
    return best_tours, best_cost

# Set up the problem
num_robots = 4
city_ids = list(range(1, 22))

# Get initial solution
initial_tours = initial_solution(city_ids, num_robots)
best_tours, best_cost = simulated_annealing(initial_tours)

# Output results
overall_total_cost = 0
for idx, tour in enumerate(best_tours):
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")
    overall_total_string = "cost: {:.2f}".format(overall_total_cost)
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")