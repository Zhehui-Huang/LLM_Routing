import math
import random

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

num_robots = 8
start_city = 0

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_tour_cost(tour):
    """Calculate the total cost of the given tour."""
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour)-1))

def simulated_annealing(initial_tour):
    """Optimize the given tour using the Simulated Annealing algorithm."""
    temp = 10000
    cooling_rate = 0.003
    current_tour = initial_tour[:]
    best_tour = current_tour[:]
    best_cost = total_tour_cost(best_tour)

    while temp > 1:
        new_tour = current_tour[:]
        i, j = sorted(random.sample(range(1, len(new_tour)-1), 2))
        new_tour[i:j+1] = reversed(new_tour[i:j+1])
        
        current_cost = total_tour_cost(current_tour)
        new_cost = total_tour_cost(new_tour)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_tour = new_tour[:]
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
        
        temp *= 1 - cooling_rate

    return best_tour, best_cost

# Divide cities among the robots, ensuring each robot starts at depot city 0
remaining_cities = set(range(1, len(cities)))
robot_tours = [[start_city] for _ in range(num_robots)]

while remaining_cities:
    for robot_tour in robot_tours:
        if remaining_cities:
            next_city = remaining_cities.pop()
            robot_tour.append(next_city)

# Optimize each robot's tour and calculate the costs
optimized_tours = []
total_costs = []

for tour in robot_tours:
    tour.append(start_city)  # Robot tour ends at the starting city for calculation
    optimized_tour, tour_cost = simulated_annealing(tour)
    # Remove the added last start city in output if not needed to complete loop
    optimized_tours.append(optimized_tour[:-1])
    total_costs.append(tour_red_cost)

# Output the results
overall_total_cost = sum(total_costs)
for robot_id, tour in enumerate(optimized_tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_total6_cost}")