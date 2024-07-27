import itertools
import math
from scipy.spatial.distance import euclidean

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return euclidean(city_coordinates[city1], city_coordinates[city2])

# Number of robots and cities
num_robots = 8
num_cities = len(city_coordinates)  # this includes the depot

# Generate all possible tours
def generate_tours(start, num_robots, cities):
    if len(cities) < num_robots:
        return []

    if num_robots == 1:
        yield [start] + cities + [start]
    else:
        for chosen_cities in itertools.combinations(cities, len(cities) - num_robots + 1):
            remaining_cities = [city for city in cities if city not in chosen_cities]
            for sub_tour in generate_tours(start, num_robots - 1, remaining_cities):
                yield [start] + list(chosen_cities) + [start] + sub_tour

# Calculate the cost of all tours
def calculate_cost(tours):
    total_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(tour[i], tour[i + 1])
        total_costs.append(cost)
    return total_costs

# Evaluate division of cities based on the robot tours
def evaluate_tours():
    cities = list(range(1, num_cities))  # excluding the depot
    best_max_cost = float('inf')
    best_tours = None

    for tours in generate_tours(0, num_robots, cities):
        # Split the tour based on depot occurrences which simulate different robots
        split_indexes = [i for i, value in enumerate(tours) if value == 0]
        robot_tours = [tours[split_indexes[i]:split_indexes[i + 1] + 1]
                       for i in range(len(split_indexes) - 1)]
        costs = calculate_cost(robot_tours)

        max_cost = max(costs)
        if max_cost < best_max_cost:
            best_max_cost = max_cost
            best_tours = robot_tours
        
        # Break early if we've found an ideal division early for testing purposes
        if best_max_cost <= 300:
            break

    return best_tours, best_max_cost

# Calculate the best tour and output the result
tours, max_cost = evaluate_tours()

for i, tour in enumerate(tours):
    cost = calculate_cost([tour])[0]
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {int(cost)}")

print(f"Maximum Travel Plan Cost: {int(max_cost)}")