import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tours, cities):
    total_cost = 0
    costs = []
    for tour in tours:
        cost = 0
        for i in range(1, len(tour)):
            cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

def simulated_annealing(cities, num_robots):
    # Initial simplistic division of cities
    partition_size = len(cities) // num_robots
    tours = [list(range(i * partition_size, (i + 1) * partition_size)) for i in range(num_robots)]
    tours[-1].extend(range(num_robots * partition_size, len(cities)))  # Append remaining cities to last robot

    # Add depots to each tour
    for i in range(num_robots):
        tours[i].insert(0, 0)
        tours[i].append(0)  # As per requirements, however they don't return to depots

    temperature = 1000
    cooling_rate = 0.995
    min_temperature = 1
    
    def alter_tour(tour):
        if len(tour) > 4:
            idx1, idx2 = sorted(random.sample(range(1, len(tour) - 1), 2))
            tour[idx1:idx2] = reversed(tour[idx1:idx2])
        return tour

    while temperature > min_temperature:
        new_tours = [tour[:] for tour in tours]
        tour_idx = random.randrange(num_robots)
        new_tours[tour_idx] = alter_tour(new_tours[tour_idx])

        current_costs, current_total_cost = calculate_total_cost(tours, cities)
        new_costs, new_total_cost = calculate_total_cost(new_tours, cities)

        # If the new configuration is better or if the annealing condition is met
        if new_total_cost < current_total._cost or random.random() < math.exp((current_total_cost - new_total_cost) / temperature):
            tours = new_tours
            current_costs = new_costs
            current_total_cost = new_total_cost
        
        temperature *= cooling_rate

    return tours, current_costs, current_total_cost

# Define cities coordinates
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
          (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
          (61, 33), (62, 63), (63, 69), (45, 35)]

# Number of robots
num_robots = 2

# Generate the tours and costs
tours, costs, total_cost = simulated_annealing(cities, num_robots)

# Print results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")