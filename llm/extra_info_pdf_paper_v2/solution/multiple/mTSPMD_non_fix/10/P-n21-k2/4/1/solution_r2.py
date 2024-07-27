import math
import random

# Calculate Euclidean distance between two city coordinates
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Calculate total distance of a tour
def total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Simulated Annealing algorithm implementation 
def simulated_annealing(coordinates, initial_tour, temperature, cooling_rate, stop_temperature):
    current_tour = initial_tour[:]
    current_cost = total_distance(current_tour, coordinates)
    best_tour = current_tour[:]
    best_cost = current_cost
    
    while temperature > stop_temperature:
        next_tour = current_tour[:]
        l = len(next_tour)
        i, j = random.sample(range(1, l - 1), 2)
        next_tour[i], next_tour[j] = next_tour[j], next_tour[i]
        next_cost = total_distance(next_tour, coordinates)

        if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / temperature):
            current_tour = next_tour
            current_cost = next_cost
            
            if current_cost < best_cost:
                best_tour = current_tour[:]
                best_cost = current_cost
        
        temperature *= cooling_rate
    
    return best_tour, best_cost

# Initialize cities and coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

n_robots = 2
depots = [0, 1]

# Assign initial tours among the depots
def assign_initial_tours(depots, coordinates, n_robots):
    cities = list(range(len(coordinates)))
    random.shuffle(cities)
    tours = [[depots[i % n_robots]] for i in range(n_robots)]
    split_size = len(cities) // n_robots

    for i in range(n_robots):
        tour_cities = cities[i * split_size:(i + 1) * split_size if i < n_robots - 1 else None]
        tours[i] += tour_cities + [tours[i][0]]  # Complete the loop for initial estimation

    return tours

initial_tours = assign_initial_tours(depots, coordinates, n_robots)

# Simulated Annealing parameters
initial_temperature = 1000
cooling_rate = 0.995
stop_temperature = 1

# Optimization with Simulated Annealing
final_tours = []
costs = []
overall_cost = 0

for tour in initial_tours:
    optimized_tour, tour_cost = simulated_annealing(coordinates, tour, initial_temperature, cooling_rate, stop_temperature)
    final_tours.append(optimized_tour)
    costs.append(tour_cost)
    overall_cost += tour_cost

# Print results
for idx, tour in enumerate(final_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print(f"Overall Total Travel Cost: {overall_cost}")