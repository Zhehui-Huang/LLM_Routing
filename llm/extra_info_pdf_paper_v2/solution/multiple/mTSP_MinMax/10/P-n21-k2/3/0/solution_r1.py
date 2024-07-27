import math
import itertools

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def find_best_distribution(cities):
    n = len(cities) - 1  # Excluding the depot city
    min_max_distance = float('inf')
    best_tours = None
    
    # Generate all possible ways to distribute the cities among the robots
    for division in itertools.combinations(range(1, n + 1), n // 2):
        robot1_cities = [0] + list(division) + [0]  # Including the depot city
        robot2_cities = [0] + [i for i in range(1, n + 1) if i not in division] + [0]
        
        # Calculate the tour distance for each robot
        robot1_distance = calculate_total_distance(robot1_cities, cities)
        robot2_distance = calculate_total_distance(robot2_cities, cities)
        
        # Track the best solution based on the maximum distance of the two robots
        max_distance = max(robot1_distance, robot2_distance)
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tours = (robot1_cities, robot2_distance), (robot2_cities, robot1_distance)
    
    return best_tours, min_max_distance

best_tours, min_max_distance = find_best_distribution(cities)

# Output the results
for index, (tour, cost) in enumerate(best_tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {min_max_distance:.2f}")