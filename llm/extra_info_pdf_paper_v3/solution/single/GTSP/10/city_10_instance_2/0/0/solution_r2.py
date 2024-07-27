import math

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize a basic greedy solution based on nearest city in each group from the depot
def initial_solution(cities, groups, depot):
    route = [depot]  # Start with the depot
    for group in groups:
        closest_city = min(group, key=lambda city: euclidean_distance(cities[depot], cities[city]))
        route.append(closest_city)
    route.append(depot)  # End at the depot
    return route

# Calculate total distance of the tour
def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_name_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Cities coordinates and groups definition
cities = [
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
]

groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]

# Start from the depot city 0
depot = 0

# Generate an initial solution
tour = initial_solution(cities, groups, depot)

# Calculate the total travel distance of the tour
total_distance = calculate_total_distance(tour, cities)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")