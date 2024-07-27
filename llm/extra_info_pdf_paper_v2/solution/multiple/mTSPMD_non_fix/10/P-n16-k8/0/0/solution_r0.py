import math
import random

# City coordinates indexed by city ID
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Simulated Annealing algorithm parameters
initial_temp = 10000
cooling_rate = 0.995
min_temp = 1

# Initial random solution: each robot starts with just the depot city
num_robots = 8
depot = 0
all_cities = list(range(1, len(coordinates)))  # excluding the depot city initially
random.shuffle(all_cities)
robots_tours = [[] for _ in range(num_robots)]

# Distributing cities to robots
segment_size = len(all_cities) // num_robots + (len(all_cities) % num_robots > 0)
for i in range(num_robots):
    if all_cities:
        robots_tours[i] = [depot] + [
            all_cities.pop(0) for _ in range(min(segment_size, len(all_cities)))
        ]

def total_path_cost(tours):
    total_cost = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(tour[i], tour[i+1])
        total_cost += calculate_distance(tour[-1], tour[0])  # Return to depot cost (if needed)
    return total_cost

def simulated_annealing(tours):
    temp = initial_temp
    current_solution = tours[:]
    current_cost = total_path_cost(current_solution)
    best_solution = current_solution[:]
    best_cost = current_cost

    while temp > min_temp:
        # Create new candidate solution
        robot_id = random.randint(0, num_robots - 1)
        tour_len = len(current_solution[robot_id])
        if tour_len > 2:
            i, j = sorted(random.sample(range(1, tour_len), 2))  # Ensure there's no depot swapping
            new_solution = [tour[:] for tour in current_solution]
            new_solution[robot_id][i], new_solution[robot_id][j] = new_solution[robot_id][j], new_solution[robot_id][i]
            
            new_cost = total_path_cost(new_solution)
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_solution, current_cost = new_solution, new_cost
                if current_cost < best_cost:
                    best_solution, best_cost = current_solution, current_cost
            
        temp *= cooling_rate
    
    return best_solution, best_cost

# Execute the simulated annealing algorithm
final_tours, final_cost = simulated_annealing(robots_tours)

# Output robot tour data
for idx, tour in enumerate(final_tours):
    tour_cost = total_path_cost([tour])
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {final_cost:.2f}")