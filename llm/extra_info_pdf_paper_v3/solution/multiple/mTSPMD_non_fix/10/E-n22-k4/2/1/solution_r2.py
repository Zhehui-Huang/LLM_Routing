import math
import random

# City coordinates
cities = {
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

def distance(city1, city2):
    """Calculates the Euclidean distance between two cities based on their coordinates."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def simulated_annealing(num_robots, depots):
    """Performs simulated annealing to find an approximate solution to the MmTSP."""
    temp = 10000
    cooling_rate = 0.995
    min_temp = 1
    tours = {robot: [depot] for robot, depot in enumerate(depots)}
    remaining_cities = list(set(cities) - set(depots))
    random.shuffle(remaining_cities)

    partitions = len(remaining_cities) // num_robots
    for i in range(num_robots):
        start = i * partitions
        if i == num_robots - 1:
            tours[i] += remaining_cities[start:]
        else:
            tours[i] += remaining_cities[start:start + partitions]

    def total_cost(tours):
        return sum(sum(distance(tours[robot][i], tours[robot][i + 1]) for i in range(len(tours[robot]) - 1))
                    for robot in tours)

    # Main loop of simulated annealing
    while temp > min_temp:
        robot_id = random.choice(list(tours.keys()))
        current_tour = tours[robot_id]
        if len(current_tour) > 2:
            i, j = sorted(random.sample(range(1, len(current_tour)), 2))
            new_tour = current_tour[:]  # create a new 
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

            # Calculate the new total cost
            new_cost = total_cost(tours)
            delta = new_cost - total_cost(tours)
            if delta < 0 or random.random() < math.exp(-delta / temp):
                tours[robot_id] = new_tour  # accept move

        temp *= cooling_rate
    
    return tours, total_cost(tours)

num_robots = 4
depots = [0, 1, 2, 3]
tours, total_travel_cost = simulated_annealing(num_robots, depots)

# Print results
for robot, tour in tours.items():
    tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")