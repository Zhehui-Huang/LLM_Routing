import numpy as np

# Coordinates of each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
robots = 8

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize distance matrix
number_of_cities = len(cities)
distance_matrix = np.zeros((number_of_cities, number_of_cities))
for i, coords1 in cities.items():
    for j, coords2 in cities.items():
        distance_matrix[i][j] = calculate_distance(i, j)

# Function to find routes using a simplified approach
def find_routes():
    available_cities = list(cities.keys())[1:]  # Available visiting cities by bypassing the initial depot
    tours = []
    overall_cost = 0

    for i in range(robots):
        if not available_cities:
            break

        current_city = 0  # Start at depot
        tour_cost = 0
        tour = [current_city]

        while available_cities:
            # Select the nearest next city available
            next_city = min(available_cities, key=lambda x: distance_matrix[current_city][x])
            tour_cost += distance_matrix[current_city][next_city]
            tour.append(next_city)
            current_city = next_city
            available_cities.remove(current_city)
            # Break if the tour size is roughly the total cities divided by the number of robots
            if len(tour) > number_of_cities / robots:
                break

        # Optionally closing the tour at the starting depot
        # tour.append(0)  # Uncomment this line to make the tour circular
        # tour_cost += distance_matrix[current_city][0]

        tours.append((tour, tour_cost))
        overall_cost += tour_cost
    
    return tours, overall (Make step-by-step suggestions or provide code fragments.)overall_cost

# Calculate the tours and the costs
tours, total_cost = find_routes()

# Print resulting tours and costs
for idx, (tour, cost) in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")