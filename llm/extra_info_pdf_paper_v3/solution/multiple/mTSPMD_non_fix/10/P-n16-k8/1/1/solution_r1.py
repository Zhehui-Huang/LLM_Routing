import math
import random

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_path_cost(path, cities):
    total_cost = 0
    for i in range(1, len(path)):
        total_cost += euclidean_distance(cities[path[i-1]], cities[path[i]])
    if len(path) > 1:
        total_cost += euclidean_distance(cities[path[-1]], cities[path[0]])  # Return to starting depot
    return total_cost

def simulated_annealing(cities, num_robots, initial_temp, cooling_rate, stopping_temp):
    # Initial paths where each robot starts at its start point (all start at depot 0)
    paths = [[0] for _ in range(num_robots)]
    remaining_cities = list(range(1, len(cities)))  # Remaining cities to distribute
    random.shuffle(remaining_cities)
    
    # Distribute remaining cities somewhat evenly
    for i, city in enumerate(remaining_cities):
        paths[i % num_robots].append(city)
    
    current_cost = sum(total_path_cost(path, cities) for path in paths)
    temperature = initial_temp

    while temperature > stopping_temp:
        # Select two paths at random and swap a random city between them (if possible)
        i, j = random.sample(range(num_robots), 2)
        if len(paths[i]) > 1 and len(paths[j]) > 1:  # Ensure paths have extra cities to swap
            a, b = random.choice(paths[i][1:]), random.choice(paths[j][1:])
            ia, ib = paths[i].index(a), paths[j].index(b)
            paths[i][ia], paths[j][ib] = paths[j][ib], paths[i][ia]

            new_cost = sum(total_path_cost(path, cities) for path in paths)
            cost_difference = new_cost - current_cost

            if cost_difference < 0 or random.random() < math.exp(-cost_difference / temperature):
                current_cost = new_cost
            else:
                # Swap back if not accepted
                paths[i][ia], paths[j][ib] = paths[j][ib], paths[i][ia]

        temperature *= cooling_rate

    return paths, current_cost

# Parameters
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),  
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]
num_robots = 8
initial_temp = 10000
cooling_rate = 0.98
stopping_temp = 1

# Running the algorithm
tours, total_cost = simulated_annealing(cities, num_robots, initial_temp, cooling_rate, stopping_temp)

# Printing results
overall_total_cost = 0
for idx, tour in enumerate(tours):
    tour_cost = total_path_cost(tour, cities)
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour + [tour[0]]}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"\nOverall Total Travel Cost: {overall_total_cost}")