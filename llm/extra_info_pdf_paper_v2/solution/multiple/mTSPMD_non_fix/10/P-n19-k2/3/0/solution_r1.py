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
    tours = [list(range(i * partition_size + 1, (i + 1) * partition_size + 1)) for i in range(num_robots)]
    tours[-1].extend(range(num_robots * partition_size + 1, len(cities)))  # Append remaining cities to last robot

    # Add the depot (initial city) to each tour
    for i in range(num_robots):
        tours[i].insert(0, i)
        # Not need to return to the depot since they do not need to end at the depot

    temperature = 1000
    cooling_rate = 0.995
    min_temperature = 1
    
    while temperature > min_temperature:
        new_tours = [tour[:] for tour in tours]
        tour_idx = random.randrange(num_robots)
        if len(new_tours[tour_idx]) > 3:
            idx1, idx2 = sorted(random.sample(range(1, len(new_tours[tour_idx])), 2))
            new_tours[tour_idx][idx1], new_tours[tour_idx][idx2] = new_tours[tour_idx][idx2], new_tours[tour_idx][idx1]
        
        current_costs, current_total_cost = calculate_total_cost(tours, cities)
        new_costs, new_total_cost = calculate_total_cost(new_tours, cities)

        if new_total_cost < current_total_cost or random.random() < math.exp((current_total_cost - new_total_cost) / temperature):
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