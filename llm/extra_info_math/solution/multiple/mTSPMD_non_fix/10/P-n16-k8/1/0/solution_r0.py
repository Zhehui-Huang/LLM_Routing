import numpy as np
from itertools import permutations

# Coordinates of each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
robots = 8

# Starting depot city for all robots
starting_depot = 0

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize distance matrix
number_of_cities = len(cities)
distance_matrix = np.zeros((number_of_cities, number_of_cities))

for i in range(number_of_cities):
    for j in range(number_of_cities):
        distance_matrix[i, j] = calculate_distance(i, j)

# Functionality to find routes
def find_routes():
    # Using a simple greedy algorithm for demonstration. This should be replaced by an algorithm
    # that can realistically solve the TSP or an approximation (e.g., Genetic Algorithms, etc.)

    tours = []
    total_cost = 0

    available_cities = set(cities.keys())
    for robot in range(robots):
        current_city = starting_depot
        tour = [current_city]
        trip_cost = 0
        available_cities.remove(current_city)

        while available_cities:
            # Find the nearest next city
            next_city = min(available_cities, key=lambda x: distance_matrix[current_city, x])
            trip_cost += distance_matrix[current_city, next_city]
            tour.append(next_city)
            current_city = next_city
            available_cities.remove(current_city)

            # Check if it's sensible to stop the tour (based on some condition, here for simplicity)
            if len(tour) > (number_of_cities / robots) * 1.2:  # or any other more meaningful condition
                break

        total_cost += trip_cost
        tour.append(starting_depot)  # Assuming if robot needs to return
        trip_cost += distance_matrix[current_city, starting_depot]
        tours.append((tour, trip_cost))
    
    return tours, total_cost

# Execute the function to find routes
tours, overall_cost = find_routes()

# Output the results
for idx, tour_data in enumerate(tours):
    print(f"Robot {idx} Tour: {tour_data[0]}")
    print(f"Robot {idx} Total Travel Cost: {tour_data[1]}")

print(f"Overall Total Travel Cost: {overall_cost}")