import math

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Nearest neighbor algorithm for generating a tour from a starting city
def nearest_neighbor_tour(starting_city, cities):
    unvisited = set(cities)
    unvisited.remove(starting_city)
    tour = [starting_city]
    current_city = starting_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(starting_city)  # Return to the starting depot
    return tour

# Create tours for each robot
cities_robot_0 = list(range(0, 11))  # Cities from 0 to 10
cities_robot_1 = list(range(11, 21))  # Cities from 11 to 20

tour_robot_0 = nearest_neighbor_tour(0, cities_robot_0)
tour_robot_1 = nearest_neighbor_tour(1, cities_robot_1)

# Calculate the total travel cost for given tours
def calculate_travel_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

cost_tour_robot_0 = calculate_travel_cost(tour_robot_0)
cost_tour_robot_1 = calculate_travel_cost(tour_robot_1)
overall_total_travel_cost = cost_tour_robot_0 + cost_tour_robot_1

# Output the results
print("Robot 0 Tour:", tour_robot_0)
print("Robot 0 Total Travel Cost:", cost_tour_robot_0)
print()
print("Robot 1 Tour:", tour_robot_1)
print("Robot 1 Total Travel Cost:", cost_tour_robot_1)
print()
print("Overall Total Travel Cost:", overall_total_travel_cost)