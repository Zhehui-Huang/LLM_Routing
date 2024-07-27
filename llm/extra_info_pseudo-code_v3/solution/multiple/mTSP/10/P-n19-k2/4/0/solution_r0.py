import math

# Define city coordinates (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Implement nearest neighbor algorithm to generate initial solution
def nearest_neighbor_tour(start_city):
    tour = [start_city]
    unvisited = set(range(len(coordinates)))
    unvisited.remove(start_city)
    
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # return to depot
    
    return tour

def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# 2-opt swap to optimize a tour
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip adjacent edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Split the tour into tours for each robot
def split_tour(tour, num_robots):
    # Simplified splitting: each robot gets equal number of cities. Optimization can enhance this.
    n = len(tour) - 1  # exclude the final return to depot in count
    part_size = (n // num_robots)
    robot_tours = [tour[i*part_size + 1 : (i+1)*part_size + 1] for i in range(num_robots)]
    for i in range(num_robots):
        robot_tours[i].insert(0, 0)  # start from depot
        robot_tours[i].append(0)  # return to depot
    return robot_tours

# Initial tour
initial_tour = nearest_neighbor_tour(0)

# Optimizing initial tour
optimized_tour = two_opt(initial_tour)

# Split optimized tour into 2 robot tours
robot_tours = split_tour(optimized_tour, 2)

# Output results
total_cost = 0
for i, tour in enumerate(robot_tours):
    tour_cost = calculate_tour_cost(tour)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")