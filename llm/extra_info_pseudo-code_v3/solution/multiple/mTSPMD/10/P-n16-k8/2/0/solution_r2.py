import numpy as np

# Define the cities and their coordinates
city_coords = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
])

# Number of robots and their respective depot indices
num_robots = 8
depots = list(range(num_robots))

def calculate_distances():
    """Calculate Euclidean distances between each pair of cities."""
    num_cities = len(city_coords)
    distances = np.empty((num_cities, num_cities))
    
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i, j] = np.linalg.norm(city_coords[i] - city_coords[j])
    
    return distances

def initial_solution(num_robots, depots):
    """Create an initial feasible solution by assigning each robot a loop starting and ending at their depot."""
    num_cities = len(city_coords)
    cities = list(range(num_cities))
    other_cities = [city for city in cities if city not in depots]
    tours = {depot: [depot] for depot in depots}

    # Assign cities to depots based on nearest available city
    while other_cities:
        for depot in depots:
            if not other_cities:
                break
            # Find the nearest city not already visited
            nearest_city = min(other_cities, key=lambda x: distances[depot, x])
            tours[depot].append(nearest_city)
            other_cities.remove(nearest_city)
        for depot in depots:
            if tours[depot][-1] != depot:
                tours[depot].append(depot)  # Return to depot

    return tours

def calculate_tour_cost(tour, distances):
    """Calculate the total cost of a tour."""
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Calculate distances between all cities
distances = calculate_distances()

# Create initial tours
tours = initial_solution(num_robots, depots)

# Calculate and display tours and costs
overall_total_cost = 0

for robot_id in range(num_robots):
    tour = tours[robot_id]
    cost = calculate_tour_cost(tour, distances)
    overall_total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")