import math
from collections import defaultdict

# Coordinates of each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Demands of each city, city 0 (depot) has a demand of 0
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of robots and their capacities
num_robots = 8
capacity_per_robot = 35

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialization: greedy insertion
def greedy_insertion(capacity, demands):
    tours = []
    used_capacity = defaultdict(int)
    for robot in range(num_robots):
        tours.append([0])  # start from depot
        
    unvisited_cities = set(range(1, len(coordinates)))

    while unvisited_cities:
        found_insertion = False
        for robot in range(num_robots):
            best_cost_increase = float('inf')
            best_city = None
            best_position = None
            current_tour = tours[robot]
            for city in unvisited_cities:
                if used_capacity[robot] + demands[city] <= capacity:
                    # Try to insert city into the best position in the current tour
                    for j in range(len(current_tour)):
                        current_cost_increase = euclidean_distance(current_tour[j - 1], city) + euclidean_distance(city, current_tour[j]) - euclidean_distance(current_tour[j - 1], current_tour[j])
                        if current_cost_increase < best_cost_increase:
                            best_cost_increase = current_cost_increase
                            best_city = city
                            best_position = j
            if best_city is not None:
                used_capacity[robot] += demands[best_city]
                current_tour.insert(best_position, best_city)
                unvisited_cities.remove(best_city)
                found_insertion = True

        if not found_insertion:
            break

    # Close all tours at the depot
    for tour in tours:
        tour.append(0)
    
    return tours

# Generate initial solution
tours = greedy_insertion(capacity_per_robot, demands)

# Calculate total travel cost for each tour and overall cost
overall_cost = 0
for robot_id, tour in enumerate(tours):
    tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    overall_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")