import numpy as np

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Total number of cities including the depot
num_cities = len(coordinates)

# Distance function
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Precompute the distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Initialize tours for robots
def init_tours(num_robots, cities):
    tours = [[] for _ in range(num_robots)]
    for index, city in enumerate(cities):
        tours[index % num_robots].append(city)
    return tours

# Creating an initial feasible tour using the Nearest Neighbor heuristic
def create_tour(cities):
    tour = [0]  # Start at the depot
    available_cities = set(cities)
    current_city = 0
    while available_cities:
        next_city = min(available_cities, key=lambda x: distance_matrix[current_city, x])
        tour.append(next_city)
        current_city = next_city
        available_cities.remove(next_city)
    tour.append(0)  # Return to depot
    return tour

# Apply 2-opt optimization to the tour
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                # Perform 2-opt swap
                if j-i == 1: continue  # Skip consecutive nodes
                new_route = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if tour_cost(new_route) < tour_cost(tour):
                    tour = new_route
                    improved = True
    return tour

# Calculate the cost of a tour
def tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Initialize for 8 robots
n_robots = 8
tour_assignment = init_tours(n_robots, list(range(1, num_cities)))  # Exclude depot city 0
constructed_tours = [create_tour(tour) for tour in tour_assignment]
optimized_tours = [optimize_tour(tour) for tour in constructed_tours]

# Calculate and display the results
total_cost = 0
for idx, tour in enumerate(optimized_tours):
    cost = tour_cost(tour)
    total_cost += cost
    print(f"Robot {idx} Tour:", tour)
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print("Overall Total Travel Cost:", total_cost)