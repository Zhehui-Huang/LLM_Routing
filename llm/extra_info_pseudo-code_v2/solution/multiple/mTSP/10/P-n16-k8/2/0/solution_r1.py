import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour, coords):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coords[tour[i - 1]], coords[tour[i]])
    cost += euclidean_distance(coords[tour[-1]], coords[tour[0]])  # Return to depot
    return cost

def two_opt(tour, coords):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 2, len(tour)):
                l1 = euclidean_distance(coords[tour[i-1]], coords[tour[i]]) + euclidean_distance(coords[tour[j]], coords[tour[(j + 1) % len(tour)]])
                l2 = euclidean_distance(coords[tour[i-1]], coords[tour[j]]) + euclidean_distance(coords[tour[i]], coords[tour[(j + 1) % len(tour)]])
                if l2 < l1:
                    tour[i:j + 1] = reversed(tour[i:j + 1])
                    improved = True
    return tour

def assign_initial_tours(num_robots, coordinates):
    tours = [[] for _ in range(num_robots)]
    for i in range(1, len(coordinates)):  # start from 1 to skip depot
        tours[i % num_robots].append(i)  # Distribute cities round-robin style
    return tours

def solve_mTSP(coordinates, num_robots):
    tours = assign_initial_tours(num_robots, coordinates)
    optimized_tours = []

    for tour in tours:
        tour = two_opt(tour, coordinates)
        tour = [0] + tour + [0]  # Add depot at start and end
        optimized_tours.append(tour)

    total_travel_cost = 0
    for i, tour in enumerate(optimized_tours):
        cost = calculate_tour_cost(tour, coordinates)
        total_travel\\_cost += cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")

    print(f"Overall Total Travel Cost: {total_travel_cost}")

# Coordinates of each city including the depot
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

solve_mTSP(city_coordinates, num_robots)