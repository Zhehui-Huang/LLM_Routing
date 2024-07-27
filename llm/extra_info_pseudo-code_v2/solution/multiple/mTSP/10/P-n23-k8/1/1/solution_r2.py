import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Initialize and distribute cities to each robot
def distribute_cities(num_robots, cities):
    # Equally distribute cities to each robot
    n = len(cities)
    return [cities[i::num_robots] for i in range(num_robots)]

# Create initial tour for each robot using nearest neighbor heuristic
def create_initial_tour(start, assigned_cities, coordinates):
    tour = [start]
    current = start
    
    while assigned_cities:
        next_city = min(assigned_cities, key=lambda x: euclidean_distance(coordinates[current], coordinates[x]))
        tour.append(next_city)
        current = next_city
        assigned_cities.remove(next_city)
    tour.append(start)  # Complete the loop by returning to the depot
    return tour

# 2-opt Algorithm to improve the tour
def two_opt(tour, coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]]) + euclidean_distance(coordinates[tour[j]], coordinates[tour[j + 1]]) > euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[j]]) + euclidean_distance(coordinates[tour[i]], coordinates[tour[j + 1]]):
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    return tour

# Calculate the travel cost of the tour
def calculate_cost(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Define coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
depot = 0
robots = 8
cities = list(range(1, 23))

# Step 1: Distribute cities among robots
city_segments = distribute_cities(robots, cities)

# Step 2: Construct tours
tours = []
total_cost = 0
for i in range(robots):
    assigned = city_segments[i][:]  # Make a copy to preserve original
    initial_tour = create_initial_tour(depot, assigned, coordinates)
    optimized_tour = two_opt(initial_tour, coordinates)
    tour_cost = calculate_cost(optimized_tour, coordinates)
    tours.append((optimized_tour, tour_cost))
    total_cost += tour_cost

    print(f"Robot {i} Tour: {optimized_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_paramanager_cost}")

print(f"Overall Total Travel Cost: {total_cost}")