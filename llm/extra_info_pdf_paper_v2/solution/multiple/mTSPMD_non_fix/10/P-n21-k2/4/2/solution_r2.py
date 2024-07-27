import random
import math

# Coordinates of cities including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63),
    (63, 69), (45, 35)
]

# Calculate Euclidean distance between two points
def euclidean_distance(idx1, idx2):
    x1, y1 = cities[idx1]
    x2, y2 = cities[idx2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Simulated Annealing to optimize the mTSP
def simulated_annealing(tours, max_iterations=10000, initial_temp=10000, cooling_rate=0.995):
    temp = initial_temp
    current_solution = tours
    best_solution = tours
    best_cost = route_cost(best_solution)
    
    def neighbor(solution):
        """ Generate a neighbor by randomly swapping two cities in different routes """
        new_solution = [tour[:] for tour in solution]
        if len(new_solution) > 1:
            i, j = random.sample(range(len(new_solution)), 2)
            if new_solution[i] and new_solution[j]:
                city1 = random.choice(new_solution[i][1:])
                city2 = random.choice(new_solution[j][1:])
                idx1, idx2 = new_solution[i].index(city1), new_solution[j].index(city2)
                new_solution[i][idx1], new_solution[j][idx2] = new_solution[j][idx2], new_solution[i][idx1]
        return new_solution
    
    iter = 0
    while temp > 1 and iter < max_iterations:
        new_solution = neighbor(current_solution)
        current_cost = route_cost(current_solution)
        new_cost = route_cost(new_solution)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_solution = new_solution
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_result
        
        temp *= cooling_rate
        iter += 1
        
    return best_solution, best_cost

def route_cost(solution):
    total_cost = 0
    for route in solution:
        route_cost = sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1))
        total_cost += route_cost
    return total_cost

# Initial solution with basic partitioning
cities_per_robot = len(cities) // 2
robot_0_cities = [0] + random.sample(range(2, 21), cities_per_robot)  # Robot 0 starts at depot 0
robot_1_cities = [1] + [city for city in range(2, 21) if city not in robot_0_cities]  # Robot 1 starts at depot 1

# Wrap end cities to form a round trip (constraint relaxation for robots not ending in depot)
initial_tours = [
    robot_0_cities + [robot_0_cities[0]],
    robot_1_cities + [robot_1_cities[0]]
]

# Solve using simulated annealing
best_solution, best_cost = simulated_annealing([robot_0_cities, robot_1_cities])
overall_total_cost = 0

# Output summary of the results
for idx, tour in enumerate(best_solution):
    tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")