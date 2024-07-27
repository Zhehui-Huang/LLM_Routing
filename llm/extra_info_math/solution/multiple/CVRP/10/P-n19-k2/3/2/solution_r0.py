import math

# Given cities coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot information
num_robots = 2
capacity = 160

# Euclidean distance calculation
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initialize empty tours and their current capacities
tours = [[] for _ in range(num_robots)]
tour_demands = [0] * num_robots

# Cost tracking
tour_costs = [0.0] * num_robots

# Assign each city (excluding depot) to a robot tour
visited = set([0])
for r in range(num_robots):
    tours[r].append(0)  # start at depot

# Assign using a simplistic heuristic (next nearest unvisited city within capacity constraints)
for r in range(num_robots):
    current_city = 0
    while any(city not in visited for city in range(1, len(coordinates))):
        next_city = None
        min_dist = float('inf')
        
        for city in range(1, len(coordinates)):
            if city not in visited and tour_demands[r] + demands[city] <= capacity:
                d = distance(current_city, city)
                if d < min_dist:
                    min_dist = d
                    next_city = city
        
        if next_city is not None:
            tours[r].append(next_city)
            visited.add(next_city)
            tour_demands[r] += demands[next_city]
            tour_costs[r] += min_dist
            current_city = next_city
        else:
            break
    
    # Return to depot
    if tours[r][-1] != 0:
        tour_costs[r] += distance(tours[r][-1], 0)
        tours[r].append(0)

# Output results
total_cost = 0
for r in range(num_robots):
    print(f"Robot {r} Tour: {tours[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_costs[r]:.2f}")
    total_cost += tour_costs[r]

print(f"Overall Total Travel Cost: {total_cost:.2f}")